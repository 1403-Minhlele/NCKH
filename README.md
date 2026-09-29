# COTVD REPO ANALYSIS - Phân Tích Theo Bài Báo COTVD Và Cấu Trúc Repo

## I. Kết Luận Ngắn Gọn Sau Khi Đọc Bài Báo PDF

### Workflow tổng quan của repo CoTVD

```text
COTVD Research Workflow
├── 1. Thu thập dữ liệu gốc
│   ├── originData/Devign.json
│   ├── originData/Reveal-vulnerables.json
│   └── originData/Reveal-non-vulnerables.json
│
├── 2. Chuẩn hóa dữ liệu
│   └── code/merge.py
│       └── tạo ra data/cotvd.json
│
├── 3. Lọc sample có hàm nhạy cảm
│   └── code/joern.py
│       ├── target_list / dangerous function list
│       └── chỉ giữ các function có security-sensitive call
│
├── 4. Trích dependency slice bằng Joern
│   ├── code/joern.sc
│   ├── code/output.py
│   └── mỗi sample có field slice
│
├── 5. Chia dataset
│   └── code/split.py
│       ├── train.json
│       ├── valid.json
│       └── test.json
│
├── 6. Tạo prompt cho LLM
│   ├── code/get_slice.py
│   └── code/prompt.py
│       └── source code + dependency slice + instruction -> prompt
│
├── 7. LLM phân tích và suy luận theo Chain-of-Thought
│   └── Label: 0 / Label: 1
│
├── 8. Đánh giá hiệu năng
│   ├── Precision, Recall, F1
│   ├── so sánh với baseline Devign
│   └── so sánh với baseline ReVeal / Vuld_SySe
│
└── 9. Kết luận nghiên cứu
    └── CoTVD là pipeline reasoning với LLM, không phải repo train model end-to-end thuần túy
```

Sau khi đối chiếu với bài báo gốc, repo này không phải là một repo huấn luyện mô hình deep learning thuần túy; nó là một môi trường tái tạo pipeline của bài báo COTVD, tập trung vào:

- trích xuất dependency slice bằng Joern,
- xây dựng prompt cho LLM theo kiểu Chain-of-Thought,
- phân tích function-level vulnerability dựa trên các security-sensitive library calls,
- so sánh hiệu năng với các baseline như Devign, ReVeal và một số mô hình LLM.

Nội dung khoa học cốt lõi của bài báo là: **CoTVD dùng Joern để trích ra data dependency và control dependency từ các function C/C++ liên quan đến library calls nguy hiểm, sau đó đưa vào prompt cho LLM để đánh giá xem có vulnerability hay không.**

## II. Mục Tiêu Của Repo Theo Bài Báo

Repo này nằm trong nhánh mã nguồn của nghiên cứu COTVD. Mục tiêu cụ thể của repo là:

1. Chuẩn bị tập dữ liệu từ Devign và Reveal.
2. Lọc các sample có chứa C/C++ library function calls nhạy cảm.
3. Dùng Joern để xây code property graph và trích dependency slice liên quan.
4. Tạo prompt có cấu trúc gồm: global prompt, source code, dependency slice, instructions và label prompt.
5. Cho LLM phân tích và kết luận Label: 0 hoặc Label: 1.
6. So sánh với các baseline truyền thống và các mô hình LLM khác.

**Điểm quan trọng:** CoTVD không tập trung vào việc huấn luyện một mạng học sâu trực tiếp trên mã nguồn. Nó chủ yếu dựa trên static analysis + prompting reasoning của LLM.

## III. Những Vấn Đề Bài Báo Cốt Lõi Cần Nhớ

### 1. Dữ Liệu Nghiên Cứu

- Nguồn dữ liệu: Devign và Reveal.
- Cả hai đều là tập dữ liệu C/C++ từ các dự án open-source thực tế.
- Bài báo chỉ giữ lại các sample có chứa security-sensitive library/API calls.
- Điều này phù hợp với repo hiện có: các file target_list, dangerous function list và logic lọc trong code/joern.py.

### 2. Security-Sensitive Function List

Bài báo liệt kê các hàm nhạy cảm như:

- getenv, strcpy, strncpy, memcpy, malloc, free, printf, scanf, sprintf, strlen, strcat,...

Đây chính là danh sách tương ứng với target_list trong file code/joern.py.

### 3. Dependency Slice Extraction

Bài báo nói rõ:

- Dùng Joern để lấy backward data dependency và control dependency của các argument variable của security-sensitive function calls.
- Tất cả dependency statements được sắp xếp theo thứ tự thực thi rồi tạo thành dependency slice.
- Đây chính là mục đích của `joern.py`, `output.py`, và `joern.sc` trong repo.

### 4. Prompt Design

Bài báo mô tả prompt gồm 4 phần chủ yếu:

- Global prompt
- Dependency slice
- Instructions (CoT reasoning)
- Label prompt

Đây rất khớp với nội dung trong `code/prompt.py` và `code/get_slice.py`.

### 5. Đánh Giá Hiệu Năng

Theo bài báo:

- CoTVD dựa trên GPT-4o-128K đạt **Precision 39.09%, Recall 94.77%, F1 0.553**.
- Đây là mô hình tốt nhất trong thí nghiệm.
- Bài báo cũng chỉ ra rằng CoTVD có xu hướng tạo nhiều false positive vì nó nhạy với nhiều rủi ro bảo mật, không chỉ vulnerability truyền thống mà cả information leakage.

## IV. Cấu Trúc Repo Chính Xác Theo Thực Tế

### Thư mục `code/`

- **merge.py**: Hợp nhất dữ liệu từ Devign và Reveal thành `cotvd.json`. Đây là bước chuẩn hóa định dạng cho pipeline.

- **joern.py**: Script quan trọng nhất trong repo. Duyệt từng sample, nếu code chứa security-sensitive function, tạo file .c tạm, chạy `joern-parse` và `joern --script`. Kết quả parse được lưu vào `slice` field.

- **output.py**: Bộ parser tập hợp kết quả Joern trả về. Chuyển output thô thành cấu trúc có thể dùng trong Python.

- **prompt.py**: Tạo prompt cho LLM theo thiết kế CoTVD. Tích hợp: source code + dangerous function list + dependency slice + reasoning instructions.

- **get_slice.py**: Tạo hoặc xuất slice theo dạng text phục vụ prompt.

- **split.py**: Chia dữ liệu thành train/valid/test theo tỉ lệ 8:1:1, đồng thời giữ balance label.

- **rm_no_slice.py**: Loại bỏ các sample không có slice hoặc không chứa target function hợp lệ.

- **count.py**: Thống kê quantity và kiểm tra tỉ lệ sample theo label.

### Thư mục `data/`

- **cotvd.json**: Là tập dữ liệu trung tâm của pipeline.

- **train.json / valid.json / test.json**: Tập dữ liệu sau khi chia.

- **SourceSlice.txt / test_slice.txt / train_0_slice.txt / train_1_slice.txt**: Có thể dùng để lưu slice hoặc prompt đã được chuẩn hóa sẵn.

### Thư mục `originData/`

- Devign.json
- Reveal-vulnerables.json
- Reveal-non-vulnerables.json

Đây là dữ liệu gốc, trước khi được chuẩn hóa hoặc hợp nhất.

### Thư mục `baselines/`

- **baselines/devign-master/**: Baseline của Devign. Có cấu trúc pipeline tạo CPG, embedding, training.

- **baselines/ReVeal-master/**: Baseline Reveal và các thành phần Vuld_SySe, code-slicer. Dùng để so sánh với CoTVD trong bài báo.

## V. Luồng Dữ Liệu Đúng Theo Bài Báo

Chuỗi đúng trong repo là:

1. Lấy dữ liệu từ Devign và Reveal.
2. Lọc các sample có chứa security-sensitive library calls.
3. Gọi Joern xây code property graph.
4. Trích data dependency + control dependency quanh target function.
5. Đưa dependency slice + source code vào prompt.
6. LLM phân tích theo CoT và trả về Label:0/1.
7. So sánh kết quả với baseline deep learning.

Đây là luồng đúng hơn so với cách hiểu "huấn luyện model trực tiếp từ cotvd.json".

## VI. Cấu Trúc Prompt Của CoTVD

Bài báo mô tả prompt được xây dựng như sau:

1. **Global Prompt**: "You are a code auditor ..."
2. **Dependency Slice**: Chứa các statements liên quan đến data-flow và control-flow.
3. **Instructions**: Yêu cầu model tập trung vào `func_list` trong slice. Xem xét data passage và control flow.
4. **Label Prompt**: "You must first thoroughly analyze the code. Only after completing the analysis should you provide your detection result."

Đây là đúng với prompt.py trong repo.

## VII. Những Chỉnh Sửa Quan Trọng So Với Nhìn Thô

Nếu nhìn theo bài báo, cần sửa vài hiểu nhầm sau:

- Repo không chỉ là "training pipeline" đơn thuần.
- Repo không mô tả toàn bộ deep learning training của CoTVD; nó chủ yếu cung cấp code preprocessing + prompt generation + Joern slicing.
- Baselines trong `baselines/` là cho comparison experiment, không phải phần cốt lõi của framework CoTVD.
- **Tập trung của CoTVD là reasoning with LLM, không phải train one model from scratch on source code.**

## VIII. Tóm Tắt Về Kết Quả Thí Nghiệm Trong Bài Báo

Theo PDF:

- Tổng số sample sau lọc: **3435 positive và 6018 negative**.
- Chọn 1/10 làm test: **344 positive và 602 negative**.
- Mô hình tốt nhất: **GPT-4o-128K**.
  - Precision: 39.09%
  - Recall: 94.77%
  - F1: 0.553
  - Phát hiện: 326 positive samples

Đây là dữ kiện rất quan trọng để hiểu repo được dùng cho mục đích gì: **run experiment và reproduce CoTVD evaluation, không phải train mô hình end-to-end.**

## IX. Kết Luận Cuối Cùng

Repo COTVD trong workspace là repo mã nguồn hỗ trợ việc tái tạo và nghiên cứu framework CoTVD theo bài báo. Nó tập trung vào ba cột mốc chính:

1. chuẩn hóa dataset Devign + Reveal,
2. xây dựng dependency slice bằng Joern,
3. tạo prompt và cho LLM phân tích theo hướng Chain-of-Thought.

**Nói ngắn gọn:** đây là một công cụ / pipeline để tái hiện nghiên cứu CoTVD chứ không phải một repo deep-learning model hoàn chỉnh như Devign hay ReVeal thuần túy.

## X. Một Số File Quan Trọng Để Đọc Thêm

- [README.md](README.md)
- [code/merge.py](code/merge.py)
- [code/joern.py](code/joern.py)
- [code/output.py](code/output.py)
- [code/prompt.py](code/prompt.py)
- [code/split.py](code/split.py)
- [COTVD Paper PDF](COTVD-%20A%20function-level%20vulnerability%20detection%20framework%20using%20chain-of-thought%20reasoning%20with%20LLMs.pdf)

Dựa trên nội dung bài báo PDF, bản phân tích này đã được chỉnh lại để phản ánh đúng bản chất của repo và nghiên cứu CoTVD.

## XI. Chi Tiết Xử Lý Dữ Liệu

### Split Dataset

Script split.py thực hiện như sau:

- tách theo label 0 và 1,
- sắp xếp ngẫu nhiên,
- chia 80/10/10 theo từng label,
- kết hợp lại để tạo tập train/valid/test.

### Sinh Prompt Nếu Dùng Pipeline Prompt-Based

```bash
python code/prompt.py
```

hoặc

```bash
python code/get_slice.py
```

Mục tiêu: tạo file prompt text từ code + slice, kèm line numbers và nhãn.

## XII. Huấn Luyện Baseline

### a) Devign Baseline

Dùng script trong baselines/devign-master:

```bash
cd baselines/devign-master
python main.py -c  # tạo CPG từ code
python main.py -e  # embed token / embedding
python main.py -p  # train process
```

### b) ReVeal/Vuld_SySe Baseline

Ví dụ training model attention:

```bash
mkdir -p outputs
python baselines/ReVeal-master/Vuld_SySe/attention_main.py \
  --job train \
  --train_file data/train.json \
  --model_path outputs/attn_model.pt \
  --cuda_device -1 \
  --num_epochs 50
```

Nếu sử dụng GPU:

```bash
--cuda_device 0
```

Khi cần generate hoặc đánh giá:

```bash
python baselines/ReVeal-master/Vuld_SySe/attention_main.py \
  --job generate \
  --test_file data/test.json \
  --model_path outputs/attn_model.pt \
  --test_output_path outputs/test_predictions.json
```

## XIII. Những Vấn Đề Thường Gặp Khi Tái Hiện

### 1. Joern không có trong PATH

- Cài Joern và đặt PATH đúng.
- Hoặc chỉnh đường dẫn trong script code/joern.py.

### 2. Tập dữ liệu không tồn tại

- Kiểm tra các file trong data/ và originData/.
- Nếu thiếu file gốc, chạy merge.py hoặc đảm bảo đường dẫn đúng.

### 3. Lỗi version PyTorch / CUDA

- Cài lại torch phù hợp với GPU hoặc dùng CPU-only version.

### 4. Dữ liệu slice bị rỗng

- Có thể vì target_list không match với function body.
- Cần kiểm tra target_list trong joern.py và sample function code.

### 5. Lỗi parse output từ Joern

- output.py cần parse đúng format output của joern.sc.
- Nếu format output thay đổi, cần chỉnh parser tương ứng.

### 6. File path sai trong baseline

- Kiểm tra baselines/devign-master/configs.py hoặc configs.json.
- Nhiều baseline phụ thuộc vào cấu trúc đường dẫn cứng.

## XIV. Quy Trình Tái Hiện Hoàn Chỉnh

Repo COTVD là một pipeline hoàn chỉnh cho phát hiện lỗ hổng mức function-level, bao gồm các bước:

- thu thập dữ liệu từ nguồn Devign/Reveal,
- hợp nhất dữ liệu,
- trích dependency slice bằng Joern,
- lọc sample không hợp lệ,
- chia dữ liệu train/valid/test,
- tạo prompt/feature,
- chạy baseline để đánh giá hiệu năng.

Đây không chỉ là repo để chạy một model đơn lẻ mà là một quy trình nghiên cứu dữ liệu và preprocessing bắt buộc để tái tạo kết quả COTVD.

**Nếu muốn tái hiện tốt nhất, nên thực hiện đúng thứ tự:**

1. merge.py
2. joern.py
3. rm_no_slice.py
4. split.py
5. prompt.py (nếu cần)
6. baseline training

Đây là đường đi chuẩn để xây dựng lại toàn bộ quy trình training và đánh giá từ repo này.

## XV. Bảng Tóm Tắt Các File Quan Trọng

| File/Thư mục                                        | Mô tả                   |
| --------------------------------------------------- | ----------------------- |
| README.md                                           | Mô tả tổng quan repo    |
| code/merge.py                                       | Hợp nhất dữ liệu        |
| code/joern.py                                       | Trích slice bằng Joern  |
| code/output.py                                      | Parse kết quả Joern     |
| code/split.py                                       | Chia train/valid/test   |
| code/prompt.py                                      | Tạo prompt              |
| data/cotvd.json                                     | Dataset sau merge       |
| data/train.json                                     | Training set            |
| data/valid.json                                     | Validation set          |
| data/test.json                                      | Test set                |
| baselines/devign-master/main.py                     | Chạy pipeline Devign    |
| baselines/ReVeal-master/Vuld_SySe/attention_main.py | Chạy baseline attention |

## XVI. Gợi Ý Để Tái Hiện Đúng Hơn

- Khuyến nghị lưu một file requirements.txt cố định cho môi trường.
- Nên viết một shell script chạy tuần tự để giảm sai sót: merge → joern → split → train.
- Nên ghi rõ đường dẫn Joern, đường dẫn dữ liệu gốc và version torch trước khi chạy.
- Nếu chạy trên Windows, ưu tiên WSL2 để ít lỗi với Joern và script Linux-like.

## XVII. Hướng Dẫn Chạy Workflow Chi Tiết Từng Bước

### Chuẩn Bị Môi Trường

```bash
# Vào thư mục COTVD
cd /mnt/q/nckh/COTVD

# Kiểm tra cấu trúc
ls -la
ls -la data/
ls -la code/
```

### Bước 1: Hợp Nhất Dữ Liệu (Merge)

**Mục đích:** Kết hợp Devign.json và Reveal-\*.json thành một tệp cotvd.json duy nhất với định dạng đồng nhất.

```bash
cd /mnt/q/nckh/COTVD
python code/merge.py
```

**Output:** `data/cotvd.json`

**Kiểm tra:**

```bash
ls -lh data/cotvd.json
head data/cotvd.json | jq '.[0]'
```

---

### Bước 2: Lọc Hàm Nhạy Cảm (Optional - Count)

**Mục đích:** Thống kê hoặc lọc các sample chứa security-sensitive function calls từ dữ liệu gốc.

```bash
cd /mnt/q/nckh/COTVD
python code/count.py
```

**Output:** Xuất các sample lọc được theo target functions.

---

### Bước 3: Trích Dependency Slice Bằng Joern

**Mục đích:** Dùng Joern để xây dựng code property graph và trích data dependency + control dependency cho mỗi sample.

**Yêu cầu:** Joern phải được cài đặt và ở trong PATH.

```bash
# Kiểm tra Joern
which joern
joern --version

# Nếu chưa cài, cần cài trước
# Ví dụ: apt-get install joern (trên Linux) hoặc tải từ https://github.com/joernio/joern
```

**Chạy trích slice:**

```bash
cd /mnt/q/nckh/COTVD
python code/joern.py
```

**Output:**

- `data/Devign_func.json` - được cập nhật thêm field `slice`
- `data/log_location.txt` - ghi lại tiến độ
- `data/output.txt` - output tạm từ Joern

**Lưu ý:**

- Script này có thể chạy rất lâu (tùy số lượng sample)
- Nếu bị gián đoạn, có thể resume từ vị trí cuối (xem `log_location.txt`)

---

### Bước 4: Loại Bỏ Sample Không Hợp Lệ

**Mục đích:** Xóa các sample không có slice hoặc slice rỗng.

```bash
cd /mnt/q/nckh/COTVD
python code/rm_no_slice.py
```

**Output:** Cập nhật `data/Devign_func.json` (loại bỏ invalid samples)

**Kiểm tra:**

```bash
cd /mnt/q/nckh/COTVD
python -c "import json; data=json.load(open('data/Devign_func.json')); print(f'Remaining samples: {len(data)}')"
```

---

### Bước 5: Chia Dataset Train/Valid/Test

**Mục đích:** Chia cotvd.json theo tỉ lệ 8:1:1 (train:valid:test), giữ cân bằng label.

```bash
cd /mnt/q/nckh/COTVD
python code/split.py
```

**Output:**

- `data/train.json`
- `data/valid.json`
- `data/test.json`

**Kiểm tra:**

```bash
cd /mnt/q/nckh/COTVD
python -c "
import json
train = json.load(open('data/train.json'))
valid = json.load(open('data/valid.json'))
test = json.load(open('data/test.json'))
print(f'Train: {len(train)} samples')
print(f'Valid: {len(valid)} samples')
print(f'Test: {len(test)} samples')
"
```

---

### Bước 6: Tạo Prompt Cho LLM (Optional)

#### Cách 6a: Dùng prompt.py (Full Prompt Format)

**Mục đích:** Tạo prompt định dạng cho mô hình LLM (bao gồm code, slice, instructions).

```bash
cd /mnt/q/nckh/COTVD
python code/prompt.py
```

**Output:** `data/cotvd_prompts_slice.txt`

**Format của mỗi prompt:**

```
<1> code line 1
<2> code line 2
...
<N> code line N

Dependencies:
<line_num> dependency statement 1
<line_num> dependency statement 2
...

label: 0 (hoặc 1)
```

#### Cách 6b: Dùng get_slice.py (Slice Only)

**Mục đích:** Chỉ trích slice từ training set (ưu tiên positive samples).

```bash
cd /mnt/q/nckh/COTVD
python code/get_slice.py
```

**Output:**

- `data/train_1_slice.txt` - chỉ slice của positive samples

---

### Bước 7: Chạy Baseline Để So Sánh

#### Option 7a: Chạy Devign Baseline

```bash
cd /mnt/q/nckh/COTVD/baselines/devign-master

# Kiểm tra configs
cat configs.json

# Tạo CPG từ code
python main.py -c

# Embedding
python main.py -e

# Training
python main.py -p
```

#### Option 7b: Chạy ReVeal/Vuld_SySe Baseline

```bash
cd /mnt/q/nckh/COTVD

# Training
python -c "
import sys
sys.path.insert(0, 'baselines/ReVeal-master/Vuld_SySe')
from attention_main import train_model
train_model(
    train_file='data/train.json',
    model_path='outputs/model_attn.pt',
    num_epochs=50,
    cuda_device=-1  # Sử dụng CPU, nếu có GPU thay bằng 0
)
"
```

---

### Bước 8: Đánh Giá Kết Quả

**Mục đích:** Tính Precision, Recall, F1-Score trên test set.

Tạo file `eval.py`:

```python
import json
from sklearn.metrics import precision_score, recall_score, f1_score

# Load predictions và labels
test_data = json.load(open('data/test.json'))
y_true = [sample['label'] for sample in test_data]

# Giả sử model output predictions
y_pred = [...] # Predictions từ model

# Tính metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
```

Chạy:

```bash
cd /mnt/q/nckh/COTVD
python eval.py
```

---

### Tóm Tắt Lệnh Chạy Toàn Bộ Workflow

```bash
#!/bin/bash
# Full workflow script

cd /mnt/q/nckh/COTVD

echo "=== Step 1: Merge datasets ==="
python code/merge.py

echo "=== Step 2: Extract slices with Joern ==="
# Lưu ý: bước này tốn thời gian
python code/joern.py

echo "=== Step 3: Remove invalid samples ==="
python code/rm_no_slice.py

echo "=== Step 4: Split into train/valid/test ==="
python code/split.py

echo "=== Step 5: Generate prompts (optional) ==="
python code/prompt.py

echo "=== Step 6: Extract slices for training ==="
python code/get_slice.py

echo "=== Workflow completed! ==="
echo "Check data/ folder for generated files"
ls -lh data/
```

Lưu script này thành `run_workflow.sh` và chạy:

```bash
chmod +x run_workflow.sh
./run_workflow.sh
```

---

### Ghi Chú Về Đường Dẫn

Tất cả các script đã được cập nhật để:

- Chạy từ thư mục `COTVD` root
- Tự động xác định thư mục `data` tương đối
- Không cần phải `cd` vào `data/` trước khi chạy

Ví dụ, bạn có thể chạy từ bất kỳ đâu:

```bash
cd /mnt/q/nckh/COTVD
python code/merge.py  # Sẽ tự tìm data/ folder
```

---
