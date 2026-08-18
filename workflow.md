# Workflow tái hiện CoTVD

Tài liệu này mô tả workflow được suy ra từ mã nguồn và dữ liệu hiện có trong `COTVD`. Mục tiêu là tái tạo **dataset CoTVD, dependency slice, prompt và bước đánh giá LLM**; không sửa các tệp nguồn hiện có.

## 1. Bức tranh tổng thể

```text
Devign + ReVeal dữ liệu thô
        │
        ├─ lọc hàm có API nhạy cảm
        ├─ Joern tạo CPG và Program Dependence Graph (PDG)
        ├─ trích dependency slice theo từng API
        ├─ loại mẫu không có slice
        ▼
chuẩn hoá + gộp thành cotvd.json (code, slice, label)
        │
        ├─ chia train / valid / test theo nhãn (8 : 1 : 1)
        └─ tạo prompt CoTVD
                 │
                 ▼
       gửi từng prompt tới LLM → đọc `Label:0|1` → tính P/R/F1
```

`label = 0` nghĩa là không có lỗ hổng; `label = 1` nghĩa là có lỗ hổng.

## 2. Hiện trạng dữ liệu trong repository

| Artifact | Số mẫu | Vai trò |
| --- | ---: | --- |
| `originData/Devign.json` | 27,318 | Devign thô (`func`, `target`) |
| `originData/Reveal-non-vulnerables.json` | 20,494 | ReVeal âm tính thô (`code`) |
| `originData/Reveal-vulnerables.json` | 2,240 | ReVeal dương tính thô (`code`) |
| `data/Devign_func.json` | 5,647 | Mẫu Devign đã có slice |
| `data/Reveal_non_vul_func.json` | 3,315 | Mẫu ReVeal âm đã có slice |
| `data/Reveal_vul_func.json` | 491 | Mẫu ReVeal dương đã có slice |
| `data/cotvd.json` | 9,453 | Dataset gộp: 6,018 nhãn 0 và 3,435 nhãn 1 |
| `data/train.json` / `valid.json` / `test.json` | 7,562 / 945 / 946 | Split hiện có |

Các con số này khớp với mô tả trong bài báo: 3,435 mẫu dương, 6,018 mẫu âm và tập test gồm 344 dương, 602 âm.

## 3. Chuẩn bị môi trường

Khuyến nghị tái hiện trên Linux hoặc WSL/Ubuntu, vì pipeline gọi Joern qua shell. Bài báo dùng Ubuntu 20.04 và Python 3.7. Các script xử lý dữ liệu chủ yếu chỉ dùng Python standard library; `get_slice.py` có import thừa `torch` và `numpy`.

Cần có:

1. Python 3.7+ và lệnh `python`.
2. Java phù hợp với phiên bản Joern bạn chọn.
3. Joern có hai executable trên `PATH`: `joern` và `joern-parse`.
4. Dung lượng đĩa và thời gian đáng kể: `joern.py` tạo CPG cho từng hàm.
5. Khóa API hoặc dịch vụ cho LLM nếu muốn tái hiện phần kết quả. Repository **không chứa mã gọi API LLM**.

Chạy các script từ thư mục `COTVD/code` vì phần lớn đường dẫn trong mã là tương đối:

```powershell
Set-Location Q:\nckh\COTVD\code
```

## 4. Pha A — xây dựng dữ liệu có slice

### A1. Lọc hàm có API nhạy cảm

Danh sách API nhạy cảm nằm trong `code/count.py` và cũng được lặp lại trong `code/joern.py` (ví dụ `gets`, `strcpy`/`strncpy`, `memcpy`, `printf`, `malloc`, `recv`). Ý tưởng là chỉ giữ hàm C/C++ chứa ít nhất một chuỗi API trong danh sách.

`count.py` hiện chỉ đọc trường `code`:

```python
filtered_samples = [sample for sample in data if 'code' in sample and contains_functions(sample['code'])]
```

Do đó script dùng trực tiếp cho hai file ReVeal. Với Devign cần đổi nguồn code từ `sample['code']` sang `sample['func']`, hoặc tạo một bản chuyển đổi tạm thời. Trước mỗi lần chạy, chỉnh biến cuối file:

```python
json_file_path = '../originData/Reveal-non-vulnerables.json'
output_file_path = '../data/Reveal_non_vul_func.json'
```

Lặp cho `Reveal-vulnerables.json`; với Devign, dùng `../originData/Devign.json` và tạo `../data/Devign_func.json` với trường `func` được giữ nguyên. Không nên ghi đè trực tiếp lên dữ liệu gốc.

Lưu ý audit: việc kiểm tra là phép tìm chuỗi, không phải phân tích cú pháp. Nó có thể giữ lại `memcpy` trong comment, chuỗi ký tự hoặc tên hàm dài hơn.

### A2. Trích slice bằng Joern

`code/joern.py` là trình điều phối. Với mỗi record, nó:

1. Ghi nội dung hàm ra `temp_code_<idx>.c`.
2. Gọi `joern-parse` để tạo `cpg.bin`.
3. Gọi `joern.sc` với CPG và API mục tiêu tìm thấy.
4. `joern.sc` lấy `dotPdg` của method chứa call target và ghi DOT vào `output.txt`.
5. `output.py:parse_output()` đọc DOT, thu node liên quan và chuyển thành tập số dòng.
6. `joern.py` ánh xạ số dòng sang `(line_number, source_line)`, thêm trường `slice` vào record và lưu JSON sau từng mẫu.

Schema slice kết quả:

```json
"slice": {
  "<target-api>": [/* các dòng liên quan */],
  "result": [[12, "char buf[8];\\n"], [13, "gets(buf);\\n"]]
}
```

Trước khi chạy cần chỉnh các cấu hình hard-code ở đáy `joern.py`:

- `json_file`: chọn một file đã lọc trong `../data/`;
- `code_block = entry.get("func", "")`: đổi thành `entry.get("code", "")` cho ReVeal;
- `if idx < 7738: continue`: đặt về `if idx < 0: continue` cho lượt chạy mới. Giá trị 7738 là checkpoint dang dở, không phù hợp tái tạo từ đầu;
- `joern_script_path`: từ thư mục `COTVD/code`, dùng `joern.sc`; đường dẫn hiện tại `COTVD/code/joern.sc` chỉ đúng nếu chạy từ thư mục gốc;
- `out_file` và `log_location`: dùng đường dẫn riêng theo dataset để tránh ghi đè.

Sau đó chạy:

```powershell
python .\joern.py
```

Chạy tuần tự cho Devign, ReVeal không lỗ hổng, ReVeal có lỗ hổng. `joern.py` ghi lại JSON sau từng sample, nên có thể tiếp tục sau gián đoạn bằng cách đặt checkpoint `idx` theo `log_location.txt`.

Điểm cần kiểm chứng: `joern.sc` gọi `cpg.method(cpg.call(target).method.name.l(0)).dotPdg`, tức lấy PDG ở mức method cho lần call khớp đầu tiên. Phiên bản Joern mới có thể thay đổi cú pháp/query hoặc định dạng DOT, làm `output.py` không còn parse được. Hãy test 1–3 record trước khi chạy toàn bộ.

### A3. Loại mẫu không trích được slice

`code/rm_no_slice.py` chỉ giữ record có `slice.result` không rỗng. Script hiện ghi đè input, nên hãy đặt `input_file` thành một bản sao hoặc chủ động chấp nhận việc đó.

```powershell
python .\rm_no_slice.py
```

Kết quả cần có ba file trong `COTVD/data`: `Devign_func.json`, `Reveal_non_vul_func.json`, `Reveal_vul_func.json`.

## 5. Pha B — chuẩn hoá, gộp và chia dữ liệu

### B1. Merge

`code/merge.py` tạo record đồng nhất:

```json
{"code": "...", "slice": {"...": "..."}, "label": 0}
```

Nó lấy `func` của Devign, lấy `code` của ReVeal, rồi gán nhãn:

- ReVeal non-vulnerable → `0`;
- ReVeal vulnerable → `1`;
- Devign `target == 1` → `0`, còn lại → `1`.

Chạy từ thư mục `COTVD/data`, vì `merge.py` dùng tên file trần:

```powershell
Set-Location Q:\nckh\COTVD\data
python ..\code\merge.py
```

**Bắt buộc xác nhận ý nghĩa nhãn Devign trước khi công bố kết quả.** Script đang đảo `target` của Devign để khớp quy ước CoTVD. Nếu nguồn Devign của bạn định nghĩa `target=1` là vulnerable thay vì non-vulnerable, phải sửa mapping; nếu không toàn bộ nhãn Devign sẽ bị đảo.

### B2. Split stratified 8:1:1

`code/split.py` tách từng lớp nhãn, shuffle rồi split 80% train, 10% valid, 10% test, sau đó nối hai lớp. Chạy trong `data`:

```powershell
python ..\code\split.py
```

Script không đặt random seed và không shuffle lại sau khi nối lớp 0 rồi lớp 1. Vì vậy không thể tái lập đúng split hiện có chỉ bằng lệnh này. Để có workflow tái lập, cần đặt `random.seed(<seed>)` trước các lần `random.shuffle()` và shuffle từng split sau khi ghép nhãn.

Nếu mục tiêu là so sánh trực tiếp với báo cáo/dataset đã kèm theo, hãy dùng nguyên các file `data/train.json`, `data/valid.json`, `data/test.json` thay vì chạy lại split.

## 6. Pha C — tạo prompt và suy luận LLM

`code/prompt.py` tạo một prompt cho mỗi mẫu gồm:

1. Vai trò: code auditor;
2. full source code có đánh số dòng `<n>`;
3. dependency slice;
4. danh sách API nhạy cảm và hướng dẫn theo dõi data/control flow;
5. quy định đầu ra cuối cùng là `Label:0` hoặc `Label:1`.

Lưu ý một lỗi hiển thị nhỏ: prompt hiện chèn biến `dependencies` (một list Python) thay vì `combined_dependencies` (chuỗi các dòng). Nếu muốn prompt giống ý định của tác giả, thay `{dependencies}` bằng `{combined_dependencies}` trong template.

Để xuất prompt của test set, sửa phần `__main__` của `prompt.py` thành:

```python
json_file = "test.json"
output_file = "test_prompts.txt"
```

Rồi chạy từ `data`:

```powershell
python ..\code\prompt.py
```

File xuất không phải JSONL/API payload: nó escape ký tự xuống dòng thành `\\n`, rồi thêm nhãn ground-truth `label:` cho đánh giá offline. Khi gọi LLM, không gửi ground-truth `label`; giữ ID record, prompt nguyên bản, raw response, label dự đoán và metadata model ở một file kết quả riêng.

Repository không có client LLM, parser `Label:` từ response, retry/rate-limit handling, hay metric evaluator. Phần này cần được bổ sung bên ngoài repo. Theo bài báo, dùng nhiệt độ `0.7`; evaluation chính trên test set 946 record và expected output phải được parse nghiêm ngặt bằng regex, ví dụ `(?im)^\\s*Label\\s*:\\s*([01])\\s*$`.

Sau suy luận, tính:

```text
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
F1        = 2 × precision × recall / (precision + recall)
```

Không đánh giá response không có `Label:0`/`Label:1` như một dự đoán âm mặc định; hãy ghi nhận là format error hoặc retry, nếu không chỉ số sẽ bị méo.

## 7. Ablation và baselines

- **Full CoTVD**: code + dependency slice + reasoning instructions + label prompt.
- **w/o Slice**: bỏ dependency slice và phần hướng dẫn gắn với slice.
- **w/o CoT**: giữ slice nhưng bỏ hướng dẫn suy luận theo data/control flow.
- Baseline code có tại `baselines/devign-master` và `baselines/ReVeal-master`; đây là các dự án riêng với README, dependencies và preprocessing riêng. Không coi chúng là một bước chạy trực tiếp của pipeline `code/`.

`data/SourceSlice.txt` và `data/Ablation.txt` là artifact kết quả/prompt phục vụ thí nghiệm, không phải script tự động chạy evaluation.

## 8. Checklist tái hiện đáng tin cậy

- [ ] Lưu version Joern, Java, Python, OS và commit/hash dữ liệu.
- [ ] Test one-sample cho cả Devign và ReVeal, xác nhận `slice.result` có dòng mã hợp lý.
- [ ] Xác minh semantic của `Devign.target` trước merge.
- [ ] Không ghi đè origin data; lưu artifact từng pha với tên/phiên bản riêng.
- [ ] Đặt seed cho split và log seed đó.
- [ ] Lưu model name/version, temperature, request template, timestamp, raw LLM responses và cách parse label.
- [ ] Báo cáo format errors, token truncation, các sample Joern fail và số sample bị loại, ngoài P/R/F1.

## 9. Ranh giới tái hiện

Phần dataset/slice/prompt có thể tái tạo từ repository sau khi chỉnh cấu hình nêu trên. Kết quả số học của bài báo không thể được tái tạo bit-for-bit chỉ với repo vì: Joern và LLM có thể khác phiên bản, split script không seed, không có mã gọi LLM, và các dịch vụ LLM thương mại thay đổi theo thời gian. Dùng các artifact kèm sẵn nếu cần so sánh với kết quả gốc.
