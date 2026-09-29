# DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection

**Tác giả:** Mingyang Sun, Guozhu Meng  
**Nguồn:** arXiv:2607.13439v1, đăng ngày 15/07/2026  
**Lĩnh vực:** Phát hiện lỗ hổng phần mềm bằng LLM agent, phân tích repository-level, đánh giá độ đúng của lập luận bảo mật.

---

# PHẦN 1: TƯ DUY & PHÂN TÍCH TỪNG BƯỚC

## 1. Bối cảnh và vấn đề nghiên cứu

### 1.1. Vì sao phân tích riêng một hàm thường chưa đủ?

Nhiều phương pháp phát hiện lỗ hổng bằng học sâu và LLM nhận đầu vào là một hàm riêng lẻ. Một số phương pháp bổ sung ngữ cảnh như caller, callee hoặc đoạn mã phụ thuộc, nhưng thường lấy ngữ cảnh theo quy tắc cố định. Cả hai cách đều có thể bỏ sót thông tin bảo mật nằm ở nơi khác trong repository:

- dữ liệu đi qua nhiều hàm hoặc nhiều tệp trước khi tới thao tác nguy hiểm;
- kiểm tra xác thực, làm sạch dữ liệu hoặc phân quyền được thực hiện ở hàm khác;
- cấu hình hoặc chính sách của dự án làm thay đổi ý nghĩa của một lời gọi;
- lỗi nằm ở sự thiếu vắng một kiểm tra cần thiết, nên khó kết luận chỉ bằng cách tìm mẫu mã nguy hiểm.

Ví dụ minh họa của bài báo là một hàm `publish` gọi kiểm tra quyền trước khi xuất bản bản nháp. Nhìn riêng hàm này có vẻ đã được bảo vệ. Nhưng ở phiên bản lỗi, phép kiểm tra chỉ xác nhận người dùng có quyền chung, không gắn kiểm tra quyền với đúng đối tượng draft được chọn. Bản vá truyền chính đối tượng đó vào kiểm tra quyền. Muốn giải thích chính xác nguyên nhân, cần xem thêm cách các hàm liên quan trong repository thực hiện kiểm tra quyền và chính sách mặc định.

### 1.2. Khoảng trống mà bài báo nhắm tới

Các cách bổ sung ngữ cảnh cố định có hai vấn đề. Thứ nhất, chúng không biết trước bằng chứng nào liên quan tới giả thuyết bảo mật đang được xét. Thứ hai, nạp thật nhiều mã nguồn không đồng nghĩa với hiểu đúng; mô hình có thể bị quá tải, chú ý vào chi tiết không liên quan, hoặc báo động giả.

DREA đặt câu hỏi: thay vì truy xuất cùng một loại ngữ cảnh cho mọi hàm, liệu LLM có thể hình thành giả thuyết về lỗi rồi chủ động yêu cầu tìm đúng bằng chứng để xác nhận hoặc bác bỏ giả thuyết đó không?

## 2. Đóng góp của bài báo

Bài báo đưa ra ba đóng góp chính:

1. **DREA:** framework hai agent tách việc suy luận bảo mật khỏi việc điều hướng repository.
2. **RepoPairBench:** benchmark gồm các cặp hàm vulnerable/patched từ dự án Python thực tế, đi kèm repository snapshot phù hợp với từng phiên bản.
3. **Đánh giá reasoning correctness:** quy trình kiểm tra lời giải thích có khớp cơ chế lỗ hổng đã ghi nhận hay không, qua đó phát hiện các dự đoán đúng nhãn nhưng sai lý do, được bài báo gọi là **Lucky Hits**.

Điểm quan trọng là bài báo không chỉ hỏi “mô hình có gán đúng nhãn không?”, mà còn hỏi “mô hình có nêu đúng nguyên nhân và đường khai thác không?”.

## 3. Framework DREA — cơ chế hoạt động chi tiết

### 3.1. Đầu vào và đầu ra của hệ thống

Một lượt phân tích DREA nhận ba đầu vào chính:

1. **Hàm mục tiêu** cần kiểm tra.
2. **Đường dẫn của hàm trong dự án**, để Explorer biết cần bắt đầu tìm ở đâu.
3. **Repository snapshot tương ứng với phiên bản đang xét**, gồm toàn bộ mã nguồn có thể tra cứu ở trạng thái vulnerable hoặc patched.

Trong thực nghiệm, dữ liệu benchmark còn có metadata như CVE, CWE, diff và commit message để xây dựng nhãn chuẩn và chấm lời giải thích. Quy trình phát hiện của agent được mô tả bắt đầu từ hàm mục tiêu và repository; không nên hiểu rằng Planner luôn được cung cấp trước đáp án CVE.

Đầu ra không chỉ là một nhãn nhị phân. DREA yêu cầu:

- **Vulnerable:** nêu được đường kích hoạt hợp lý từ đầu vào có thể bị đối thủ kiểm soát tới thao tác nguy hiểm hoặc ranh giới bảo mật bị vi phạm.
- **Benign:** đưa ra bằng chứng cho thấy thao tác liên quan được bảo vệ đầy đủ, chẳng hạn dữ liệu đã được kiểm tra hoặc quyền đã được ràng buộc đúng đối tượng.

### 3.2. Vì sao tách thành Planner và Explorer?

DREA chia công việc theo bản chất của hai loại nhiệm vụ:

| Thành phần | Vai trò | Việc thực hiện | Việc không chịu trách nhiệm |
| --- | --- | --- | --- |
| **Planner** | Điều phối và suy luận bảo mật | Xem hàm, hình thành giả thuyết, xác định bằng chứng cần tìm, đánh giá kết quả, quyết định tiếp tục/dừng và kết luận | Không tự nhận toàn bộ việc duyệt mã repository quy mô lớn |
| **Explorer** | Điều hướng mã và truy xuất thông tin | Tìm tệp, tìm định nghĩa/điểm gọi, đọc đoạn mã và báo lại dữ kiện theo cấu trúc | Không đưa ra phán quyết vulnerable/benign cuối cùng |

Lý do tách vai trò là khi một mô hình mạnh vừa duyệt hàng trăm tệp vừa suy luận bảo mật, lượng token có thể rất lớn và phần ngữ cảnh gửi vào Planner dễ bị loãng. Explorer nhẹ chạy cục bộ đảm nhiệm công việc tốn token; Planner chỉ nhận các kết quả liên quan đến giả thuyết hiện tại. Đây là cách giảm phần token phải gửi qua API, không có nghĩa tổng lượng tính toán hay tổng chi phí hệ thống bằng không.

### 3.3. Planner làm gì ở từng giai đoạn?

**Giai đoạn A — đọc và khởi tạo giả thuyết.** Planner đọc hàm mục tiêu, xác định thao tác đáng chú ý như đọc dữ liệu, gọi API nhạy cảm, truy cập tài nguyên hoặc thay đổi trạng thái bảo mật. Từ đó nó tạo giả thuyết ban đầu `H₀`. Ví dụ: “giá trị `id` từ đầu vào có thể chọn một đối tượng, nhưng kiểm tra quyền có thể không áp dụng cho chính đối tượng đó”. Đây mới là hướng điều tra, chưa phải kết luận.

**Giai đoạn B — chuyển giả thuyết thành yêu cầu tìm kiếm.** Planner xác định loại bằng chứng có thể xác nhận/bác bỏ giả thuyết và gửi yêu cầu có mục tiêu cho Explorer. Tùy vấn đề, yêu cầu có thể là:

- tìm tất cả nơi gọi hàm mục tiêu;
- tìm định nghĩa của hàm kiểm tra quyền hoặc hàm làm sạch dữ liệu;
- tìm chính sách/cấu hình quyết định quyền mặc định;
- lần theo nguồn dữ liệu đầu vào tới thao tác nhạy cảm;
- so sánh với các hàm tương tự trong cùng module để xem dự án thường áp dụng guard như thế nào.

Điểm quan trọng: DREA không quy định một chuỗi truy vấn cố định áp dụng cho mọi lỗi. Truy vấn tiếp theo phụ thuộc vào giả thuyết sau khi Planner đọc bằng chứng mới.

**Giai đoạn C — tổng hợp bằng chứng và cập nhật giả thuyết.** Khi Explorer trả kết quả, Planner phải xác định dữ kiện nào ủng hộ, dữ kiện nào mâu thuẫn, và câu hỏi nào còn bỏ ngỏ. Nó cập nhật trạng thái điều tra `Hₜ → Hₜ₊₁`. Nếu bằng chứng cho thấy giả thuyết ban đầu sai, Planner có thể đổi hướng; nếu vẫn thiếu bằng chứng, nó gửi truy vấn mới.

### 3.4. Explorer tìm kiếm như thế nào và trả gì?

Explorer dùng bốn công cụ chỉ đọc trong cấu hình bài báo:

- `ls` để xem cấu trúc thư mục;
- `glob` để tìm tệp theo tên/mẫu;
- `grep` để tìm định nghĩa, lời gọi hoặc chuỗi liên quan;
- `read_file` để đọc mã cụ thể.

Explorer chỉ khảo sát repository snapshot đã cho; các công cụ này không sửa mã. Nó trả thông tin thành ba loại để Planner phân biệt dữ kiện với diễn giải:

1. **Repository Context:** đặt hàm vào đúng module/luồng gọi và chỉ ra các tệp/hàm liên quan.
2. **Code Evidence:** trích câu lệnh hoặc đoạn mã cụ thể, giúp Planner kiểm tra trực tiếp.
3. **Security Findings:** ghi nhận dấu hiệu đáng quan tâm như guard bị thiếu, cách kiểm tra không nhất quán hoặc luồng dữ liệu đáng ngờ.

Security Findings là nhận xét trung gian từ Explorer, không phải phán quyết. Planner cần kiểm tra chúng với code evidence và giả thuyết. Cách phân vai này giúp tránh biến “Explorer nghi ngờ” thành “hệ thống chắc chắn kết luận có lỗ hổng”.

### 3.5. Vòng lặp Planner–Explorer và điều kiện dừng

Có thể mô tả luồng tương tác như sau:

```text
Hàm mục tiêu + repository snapshot
                 │
                 ▼
       Planner đọc và lập H₀
                 │
                 ▼
  Planner tạo câu hỏi điều tra Qₜ
                 │
                 ▼
 Explorer tìm bằng chứng trong repository
                 │
                 ▼
 Context + Code Evidence + Security Findings
                 │
                 ▼
 Planner đánh giá và cập nhật Hₜ → Hₜ₊₁
          ┌──────┴──────┐
     Còn thiếu       Đủ bằng chứng
          │                │
          └─ truy vấn mới  ▼
                 Kết luận + giải thích
```

Thuật toán trong bài đặt một **interaction budget `B`**: tối đa `B` vòng truy vấn. Ở mỗi vòng Planner có thể dừng sớm nếu đã đủ căn cứ. Như vậy có hai tình huống kết thúc: (1) đủ bằng chứng trước khi dùng hết ngân sách; hoặc (2) hết ngân sách và phải đưa ra quyết định dựa trên thông tin hiện có. Trong thí nghiệm, một mẫu thường có xấp xỉ 10 lượt Planner–Explorer; đây là mức quan sát trung bình, không phải quy tắc bắt buộc mọi mẫu đều đúng 10 lượt.

### 3.6. Tiêu chuẩn lập luận cho quyết định cuối

Planner không nên kết luận chỉ từ sự hiện diện của một API hoặc từ tên biến. Nó cần mô tả một chuỗi bằng chứng:

- **Vulnerable:** đầu vào/điều kiện có thể bị kiểm soát → không có hoặc áp dụng sai kiểm tra → giá trị tới thao tác nguy hiểm/ranh giới bảo mật → hậu quả phù hợp với loại lỗi.
- **Benign:** xác định thao tác có rủi ro → chỉ ra guard liên quan → xác nhận guard bao phủ đúng dữ liệu/đối tượng/đường thực thi → giải thích vì sao đường khai thác bị chặn.

Với lỗi do thiếu bảo vệ, chứng minh “không thấy kiểm tra trong một đoạn mã” thường chưa đủ. Cần khảo sát đúng phạm vi: kiểm tra có nằm ở caller, wrapper, middleware, decorator hay chính sách dùng chung khác không. Đây là một lý do DREA cần điều tra nhiều tệp, nhưng cũng là phần đòi hỏi Planner tổng hợp rất tốt.

### 3.7. Ví dụ xuyên suốt: kiểm tra quyền khi publish draft

Bài báo dùng CVE-2021-43781 để minh họa vì sao chỉ đọc hàm mục tiêu có thể gây hiểu nhầm:

1. **Quan sát ban đầu:** hàm `publish` gọi `require_permission(identity, "publish")`. Khi chỉ xem hàm, có vẻ thao tác publish đã được kiểm tra quyền.
2. **Giả thuyết của Planner:** phép kiểm tra có thể chỉ xác nhận quyền chung, chưa kiểm tra người dùng có quyền trên draft cụ thể được chọn bằng `id_` hay không.
3. **Câu hỏi cho Explorer:** các hàm cùng chức năng kiểm tra quyền trên đối tượng draft ra sao; định nghĩa/chính sách `require_permission` yêu cầu những tham số nào; mặc định `can_publish` được cấu hình thế nào.
4. **Bằng chứng Explorer tìm được:** các hàm tương tự như đọc/sửa/xóa draft truyền `record=draft`; chính sách mặc định `can_publish` là `[AnyUser()]`; lời gọi trong hàm lỗi thiếu đối tượng `record`.
5. **Planner cập nhật:** kiểm tra hiện tại chỉ xác nhận quyền chung và không gắn với draft do `id_` chọn; do đó nó chưa chứng minh quyền trên tài nguyên đích.
6. **Đối chiếu bản vá:** phiên bản sửa resolve draft trước rồi gọi `require_permission(..., record=draft)`, buộc phép kiểm tra áp dụng đúng đối tượng.
7. **Kết luận:** hàm trước vá vulnerable vì thiếu ràng buộc quyền theo đối tượng; bản vá bổ sung ràng buộc đó. Căn cứ quyết định đến từ việc kết hợp hàm mục tiêu với chính sách và cách dùng trong các hàm cùng repository.

Ví dụ này thể hiện một nguyên tắc bảo mật tổng quát: chỉ xác nhận “có gọi hàm kiểm tra” chưa đủ; phải xác minh kiểm tra đó áp dụng **đúng chủ thể, đúng tài nguyên và đúng đường thực thi**.

### 3.8. DREA khác retrieval cố định và Single-Agent ra sao?

| Cách tiếp cận | Cách lấy ngữ cảnh | Vai trò của LLM | Rủi ro chính |
| --- | --- | --- | --- |
| Function-Only | Không truy xuất repository | Phân loại từ hàm mục tiêu | Thiếu bằng chứng liên tệp |
| Whole-File | Đưa toàn bộ tệp chứa hàm | Đọc một khối mã cố định | Bỏ sót tệp khác hoặc nạp nhiễu |
| Dependency-Augmented/Context Retrieval cố định | Lấy trước caller/callee/snippet theo quy tắc | Phân loại trên gói ngữ cảnh đã định | Quy tắc có thể không khớp giả thuyết cụ thể |
| Single-Agent | Một mô hình vừa tìm mã vừa kết luận | Điều hướng và suy luận cùng một vai | Lượng mã/token lớn có thể làm loãng suy luận |
| **DREA** | Planner yêu cầu Explorer tìm bằng chứng theo giả thuyết đang cập nhật | Planner suy luận; Explorer điều hướng và báo dữ kiện | Phụ thuộc chất lượng truy vấn, truy xuất và tổng hợp bằng chứng |

DREA không chỉ là “hai LLM cùng làm một việc”. Giá trị thiết kế nằm ở **ranh giới nhiệm vụ**: Explorer cung cấp sự kiện và đoạn mã; Planner giữ trách nhiệm giải thích ý nghĩa bảo mật và ra quyết định. Kết quả ablation của bài báo hỗ trợ hướng thiết kế này, nhưng vì Single-Agent và DREA cũng khác nhau ở cấu hình mô hình nên không thể quy mọi chênh lệch chỉ cho việc tách agent.

## 4. RepoPairBench: benchmark theo cặp có ngữ cảnh repository

### 4.1. Cách xây dựng dữ liệu

RepoPairBench được tạo từ CVE và commit sửa lỗi liên kết với repository. Tác giả dùng NVD để thu thập thông tin CVE và PyDriller để trích xuất thay đổi ở mức hàm. Sau quá trình lọc nghiêm ngặt, benchmark có:

- **100 cặp lỗ hổng–bản vá**, tức 200 mẫu riêng lẻ;
- **48 nhóm CWE**;
- lỗ hổng Python được công bố trong giai đoạn **2021–2025**;
- 100 phiên bản vulnerable lấy từ commit cha trước khi sửa và 100 phiên bản patched lấy từ commit sửa lỗi;
- repository snapshot tương ứng với từng phiên bản, để agent khám phá đúng trạng thái mã nguồn.

Nhóm chỉ giữ các trường hợp hàm được đối chiếu rõ trước/sau khi vá và commit sửa tập trung vào sửa đổi mã, loại các trường hợp thêm/xóa tệp hoặc đưa hàm mới vào để giảm nhiễu khi quy nguyên nhân.

### 4.2. Ý nghĩa và phạm vi của nhãn

Phiên bản patched được gán benign **đối với lỗ hổng cụ thể đã ghi nhận**, không có nghĩa toàn bộ hàm hay repository không còn bất kỳ vấn đề bảo mật nào. Nếu mô hình gắn cờ phiên bản đã vá vì một cơ chế lỗi khác, theo giao thức cặp của bài báo, đó vẫn là false positive. Quy tắc này làm cho benchmark đo khả năng nhận ra đúng lỗ hổng/bản vá được nghiên cứu, chứ không phải khả năng kiểm toán mọi lỗi có thể có.

### 4.3. Vì sao tập trung vào Python?

Tác giả chọn các CVE Python gần đây vì hệ sinh thái GitHub có nhiều dự án đang được duy trì và nhiều commit liên kết CVE; Python cũng xuất hiện trong framework web và pipeline dữ liệu, nơi các lỗi injection, deserialization và path traversal thường cần ngữ cảnh liên tệp. Tuy nhiên, lựa chọn này đồng nghĩa kết quả benchmark chưa tự chứng minh khả năng áp dụng tương đương cho C/C++ hay ngôn ngữ khác.

## 5. Thiết kế thực nghiệm và các chỉ số

### 5.1. Mô hình và baseline

Ba backbone làm Planner:

- DeepSeek-V3.2;
- GLM-4.7;
- GPT-5.2.

Explorer được cố định là GLM-4.7-Flash, lượng tử hóa 4-bit AWQ và chạy cục bộ qua vLLM trên một GPU A800. Việc dùng chung Explorer nhằm giảm biến thiên do thành phần truy xuất khi so sánh các Planner. Bài báo dùng tham số giải mã mặc định.

DREA được so sánh với ba baseline có mức ngữ cảnh/quyền truy cập khác nhau:

1. **Function-Only:** chỉ nhận hàm mục tiêu, không có truy cập repository.
2. **Whole-File:** nhận toàn bộ tệp chứa hàm mục tiêu nhưng không có công cụ khám phá.
3. **Single-Agent:** cùng backbone vừa suy luận vừa dùng công cụ điều hướng repository; không tách Planner và Explorer.

So sánh cùng backbone giữa DREA và Function-Only giúp đánh giá lợi ích của truy cập repository. Whole-File và Single-Agent giúp khảo sát liệu lợi ích đến từ việc có thêm mã, có công cụ, hay từ cách chia vai trò và tổ chức bằng chứng.

### 5.2. Chỉ số phân loại và theo cặp

- **Recall:** tỷ lệ mẫu vulnerable được phát hiện.
- **False Positive Rate (FPR):** tỷ lệ mẫu benign bị báo nhầm.
- **F1:** tổng hợp precision và recall trên 200 mẫu.
- **Pair-Correctness (P-C):** tỷ lệ trong 100 cặp mà cả mẫu vulnerable lẫn patched đều được phân loại đúng.
- **P-V, P-B, P-R:** lần lượt đếm cặp mà cả hai bị dự đoán vulnerable, cả hai bị dự đoán benign, hoặc nhãn bị đảo. Các số này giúp giải thích kiểu sai của hệ thống.
- **Youden’s J = Recall − FPR:** đo khả năng phân biệt sau khi tính cả bắt được lỗi và báo động giả.

### 5.3. Đánh giá chất lượng lập luận

GPT-4.1 được dùng làm LLM judge, không trùng với ba Planner backbone. Judge nhận mô tả CVE, commit message, diff, nhãn CWE và phần phân tích cuối của mô hình; sau đó xem xét:

1. mô hình có nhận diện đúng loại lỗ hổng không;
2. có chỉ ra đúng đoạn mã liên quan không;
3. có xác định đúng nguyên nhân gốc không;
4. cơ chế khai thác có nhất quán với lỗi được ghi nhận không.

Reasoning quality chỉ được tính trên true positive vulnerable samples, nơi có lời giải thích cho lỗ hổng để đối chiếu. Nhóm kiểm tra judge bằng 50 trường hợp do hai nhà nghiên cứu an ninh có kinh nghiệm chú giải độc lập. Mức đồng thuận judge–chuyên gia là 96% và 94%, tương ứng Cohen’s κ 0,92 và 0,88; đồng thuận giữa hai chuyên gia là 92%, κ = 0,84.

**Lucky Hit** là dự đoán đúng nhãn vulnerable nhưng lời giải thích không đúng cơ chế lỗ hổng. **Reasoning Accuracy (RA)** là tỷ lệ true positive có lập luận đúng; **Lucky Hit Rate (LHR)** là tỷ lệ true positive có lập luận sai. Hai đại lượng này bổ sung cho metric phân loại, bởi một nhãn đúng có thể do mô hình đoán theo mẫu chung thay vì hiểu đúng lỗi.

## 6. Kết quả thực nghiệm

### 6.1. DREA so với Function-Only

| Planner | Phương pháp | Recall | FPR | F1 | P-C | Youden’s J |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek-V3.2 | DREA | 80% | 45% | 71,1% | 42% | 35 điểm |
| DeepSeek-V3.2 | Function-Only | 39% | 32% | 45,6% | 19% | 7 điểm |
| GLM-4.7 | DREA | 59% | 38% | 59,9% | 34% | 21 điểm |
| GLM-4.7 | Function-Only | 54% | 43% | 54,8% | 26% | 11 điểm |
| GPT-5.2 | DREA | 53% | 28% | 58,6% | 30% | 25 điểm |
| GPT-5.2 | Function-Only | 42% | 25% | 50,3% | 21% | 17 điểm |

DREA tăng P-C trên cả ba backbone: DeepSeek-V3.2 tăng 23 điểm phần trăm, GLM-4.7 tăng 8 điểm và GPT-5.2 tăng 9 điểm. Với DeepSeek-V3.2, recall tăng 41 điểm trong khi FPR tăng 13 điểm, nên Youden’s J tăng từ 7 lên 35. Với GLM-4.7, FPR còn giảm từ 43% xuống 38% trong khi recall tăng. Với GPT-5.2, recall tăng 11 điểm và FPR chỉ tăng 3 điểm.

Những kết quả này cho thấy tác động của repository context thay đổi theo backbone. DeepSeek-V3.2 là cấu hình nhạy bắt lỗi nhất nhưng cũng có FPR cao nhất trong DREA; GPT-5.2 thận trọng hơn, FPR thấp hơn nhưng recall thấp hơn. Không có một operating point duy nhất tối ưu cho mọi trường hợp triển khai.

### 6.2. Ablation: ngữ cảnh nhiều hơn có tự động tốt hơn không?

Ablation được làm trên DeepSeek-V3.2:

| Phương pháp | Recall | FPR | F1 | P-C | Token API trung bình/mẫu |
| --- | ---: | ---: | ---: | ---: | ---: |
| Function-Only | 39% | 32% | 45,6% | 19% | 3K |
| Whole-File | 57% | 41% | 57,6% | 26% | 20K |
| Single-Agent | 73% | 64% | 61,6% | 24% | 442K |
| DREA | 80% | 45% | 71,1% | 42% | 88K |

Whole-File cải thiện P-C so với Function-Only nhưng thấp hơn DREA; cung cấp cả tệp có thể thêm nhiễu. Single-Agent có quyền khám phá đầy đủ nhưng P-C chỉ 24%, FPR 64%, và tiêu thụ khoảng 442K token API mỗi mẫu. DREA đạt P-C 42% với khoảng 88K token Planner/API mỗi mẫu. So sánh này ủng hộ việc cấu trúc bằng chứng và tách điều tra khỏi suy luận; tuy vậy, tác giả lưu ý Single-Agent và DREA cũng khác nhau ở mô hình Explorer, nên không thể quy toàn bộ chênh lệch chỉ cho kiến trúc.

### 6.3. Chi phí token

Theo thống kê trung bình trên mỗi mẫu:

| Planner | Tổng token | Token Planner/API | Token Explorer cục bộ | Token qua API | Mức giảm chi phí API ước tính |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek-V3.2 | 1.397.669 | 87.847 | 1.309.822 | 6,3% | khoảng 16× |
| GLM-4.7 | 1.560.519 | 32.557 | 1.527.962 | 2,1% | khoảng 48× |
| GPT-5.2 | 345.691 | 8.357 | 337.334 | 2,4% | khoảng 41× |

Explorer xử lý cục bộ 93,7–97,9% tổng token; chỉ 2,1–6,3% được đưa qua API Planner. Mức giảm 16–48 lần là so sánh chi phí API với giả định toàn bộ token đều phải trả theo mức API. Bài báo **không** tính chi phí vận hành GPU A800 cục bộ, nên không nên diễn giải các con số này là mức giảm tương ứng của tổng chi phí sở hữu hệ thống.

### 6.4. Hiệu năng theo CWE và kiểu lỗi

DREA làm tốt hơn ở các lỗi có cấu trúc luồng dữ liệu/đầu vào–đầu ra rõ, chẳng hạn CWE-79 (XSS) và CWE-94 (code injection). Hiệu năng thấp hơn với lỗi do thiếu biện pháp bảo vệ, như CWE-284 (access control) và CWE-20 (input validation). Loại thứ hai đòi hỏi mô hình xác định điều gì lẽ ra phải tồn tại nhưng bị thiếu, thay vì tìm một chuỗi thao tác nguy hiểm hiện rõ trong mã.

Các con số theo CWE cần được đọc thận trọng: mỗi nhóm chỉ có khoảng 3–13 cặp. Phân tích này gợi ý về kiểu lỗi khó/dễ đối với benchmark, chưa đủ để kết luận xếp hạng tổng quát cho từng CWE.

### 6.5. Khám phá nhiều hơn không đồng nghĩa phân tích tốt hơn

Trong cấu hình DeepSeek-V3.2, mẫu vulnerable bị bỏ sót dùng trung bình khoảng 1,70 triệu token, so với 1,24 triệu ở mẫu vulnerable phát hiện đúng — cao hơn khoảng 37%. Số lượt gọi công cụ ở các nhóm kết quả lại khá giống nhau, khoảng 9,2–10 lượt. Tương quan giữa lượng token mỗi mẫu và độ đúng dự đoán là khoảng −0,34.

Tác giả diễn giải rằng điều tra kéo dài thường là dấu hiệu bài toán khó, không phải nguyên nhân tạo ra kết quả tốt hơn. Nếu Planner không tổng hợp được bằng chứng, việc Explorer tiếp tục tìm thêm mã có thể chỉ làm tăng chi phí mà không cải thiện kết luận.

### 6.6. Lucky Hits: nhãn đúng nhưng lý do sai

LHR trong DREA là:

- DeepSeek-V3.2: **55,0%**;
- GLM-4.7: **45,8%**;
- GPT-5.2: **32,1%**.

Như vậy, riêng với DeepSeek-V3.2, trong số các lỗ hổng được phát hiện đúng, hơn một nửa có lời giải thích không đạt tiêu chí khớp cơ chế lỗi. GPT-5.2 có tỷ lệ Lucky Hit thấp nhất trong ba backbone, dù recall cũng thấp hơn. Khi lập luận thất bại, mô hình thường quay về giải thích chung chung như “thiếu kiểm tra đầu vào”, kể cả với lỗi không thuộc nhóm đó.

DREA có thể tạo thêm true positive đúng lý do theo số lượng tuyệt đối vì phát hiện được nhiều mẫu hơn, nhưng tỷ lệ lập luận đúng trên mỗi true positive không nhất thiết cao hơn baseline. Tác giả kết luận chất lượng security reasoning vẫn là điểm nghẽn chung, bất kể mô hình có được truy cập repository hay không.

## 7. Ưu điểm và đóng góp nổi bật

- **Khám phá ngữ cảnh theo câu hỏi bảo mật:** Planner không yêu cầu cùng một gói caller/callee cho mọi hàm; nó xác định bằng chứng cần tìm từ giả thuyết đang xét. Điều này phù hợp với việc lỗi phân quyền, xác thực và luồng dữ liệu cần loại ngữ cảnh khác nhau.
- **Tách điều tra khỏi phán đoán:** Explorer làm nhiệm vụ tìm và trình bày bằng chứng, Planner chịu trách nhiệm kết luận. Vai trò này giảm việc đưa hàng trăm nghìn token mã thô vào mô hình đắt tiền và giữ đầu vào Planner tập trung hơn.
- **Có baseline ablation tương đối rõ:** Function-Only, Whole-File, Single-Agent và DREA giúp phân tích riêng lợi ích của mã mục tiêu, toàn tệp, công cụ điều hướng và kiến trúc hai agent. Kết quả cho thấy chỉ “thêm mã” hoặc “thêm công cụ” chưa đủ.
- **Đánh giá theo cặp gắn với bản vá:** P-C yêu cầu mô hình phân loại đúng cả trạng thái lỗi và trạng thái đã sửa, giảm nguy cơ chỉ đạt điểm cao bằng cách gán quá nhiều mẫu là vulnerable.
- **Đánh giá chất lượng lý do bên cạnh nhãn:** Lucky Hit chỉ ra rằng accuracy/recall có thể đánh giá quá lạc quan nếu mô hình đoán đúng nhãn nhưng viện dẫn sai nguyên nhân. Đây là điểm có ý nghĩa thực tiễn khi người phân tích cần xác minh và xử lý cảnh báo.
- **Thực nghiệm nhiều backbone và phân tích chi phí:** Ba Planner backbone cho thấy các điểm vận hành khác nhau về recall/FPR; thống kê token làm rõ phần truy xuất cục bộ so với phần suy luận qua API.
- **Benchmark có repository snapshot và xác minh thủ công:** Mỗi phiên bản đi kèm trạng thái repository phù hợp; quy trình lọc và kiểm tra thủ công hướng tới độ tin cậy nhãn cao hơn benchmark chỉ lưu đoạn mã.

## 8. Hạn chế và rủi ro diễn giải

### 8.1. Hạn chế do chính tác giả nêu

- **Chỉ có 100 cặp:** Đây là tập dữ liệu nhỏ để đại diện cho toàn bộ kiểu lỗ hổng thực tế; nhóm chọn chất lượng và khả năng kiểm tra từng cặp thay vì số lượng lớn. Các lỗ hổng hiếm hoặc long-tail có thể chưa xuất hiện.
- **Phân tích từng CWE ít mẫu:** Mỗi nhóm thường chỉ có 3–13 cặp, do đó kết quả phân loại theo CWE có độ bất định cao.
- **Phạm vi chỉ gồm Python:** Chưa có thực nghiệm xác nhận mô hình hoạt động tương tự trên C/C++, Java hoặc ngôn ngữ khác.
- **Đánh giá thủ công reasoning chỉ gồm 50 trường hợp:** Mức đồng thuận judge–chuyên gia khá cao, nhưng cỡ mẫu còn hạn chế; nghiên cứu lớn hơn hoặc nhiều judge độc lập có thể củng cố độ tin cậy.
- **Explorer có thể thực hiện lời gọi công cụ chưa hoàn hảo:** Một mô hình Explorer mạnh hơn có thể cải thiện chất lượng context trả về.
- **Nhãn benign có nghĩa hẹp:** “Benign” là không còn lỗ hổng CVE cụ thể của cặp đó, không đảm bảo không tồn tại lỗi bảo mật khác. Nhưng nếu hệ thống báo một lỗi khác trên mẫu đã vá, giao thức vẫn tính false positive; điều này có thể phạt một phát hiện bảo mật hợp lệ ngoài mục tiêu benchmark.

### 8.2. Các điểm cần cân nhắc khi áp dụng

- **Chi phí API không phải tổng chi phí:** mức tiết kiệm 16–48× không tính GPU cục bộ, bảo trì Explorer, tải repository, thời gian chạy hay chi phí vận hành hệ thống.
- **Kết quả phụ thuộc mô hình và môi trường cụ thể:** Planner là các backbone thương mại/đóng được nêu trong bài; Explorer chạy GLM-4.7-Flash trên A800. Cấu hình khác có thể làm thay đổi cả chất lượng lẫn chi phí.
- **Judge cũng là mô hình:** dù được đối chiếu với chuyên gia, LLM-as-a-Judge có thể có thiên lệch đánh giá, bỏ sót lý do hợp lý được diễn đạt khác, hoặc chịu ảnh hưởng của chất lượng prompt/rubric.
- **P-C không mô tả đầy đủ chi phí sai lầm:** một cặp sai có thể do bỏ sót lỗ hổng hoặc báo nhầm bản vá; tác động vận hành của hai trường hợp khác nhau. Cần đọc cùng Recall, FPR, P-V/P-B/P-R và bối cảnh sử dụng.
- **Khả năng tái lập:** kết quả dựa trên các mô hình dịch vụ và một môi trường suy luận cục bộ cụ thể; phiên bản mô hình, prompt, công cụ và repository có thể ảnh hưởng kết quả khi tái chạy.
- **Không nên hiểu “thêm exploration” là luôn tốt:** số liệu cho thấy các trường hợp thất bại thường tiêu thụ nhiều token hơn. Cần cải thiện cách đặt câu hỏi, dừng đúng lúc và tổng hợp bằng chứng, không chỉ tăng ngân sách khám phá.

## 9. Kết luận của bài báo

DREA trình bày một cách tiếp cận repository-level có định hướng giả thuyết: Planner quyết định cần biết gì, Explorer tìm bằng chứng, Planner tiếp tục cập nhật rồi đưa ra kết luận. Trên RepoPairBench, DREA nâng Pair-Correctness so với baseline chỉ dùng hàm ở cả ba backbone; ablation cho thấy cấu trúc khám phá có chọn lọc hiệu quả hơn việc đưa nguyên tệp hoặc để một agent nhận lượng lớn mã.

Đồng thời, kết quả Lucky Hit cho thấy hệ thống vẫn có thể đưa ra câu trả lời đúng vì lý do sai. Vì vậy đóng góp quan trọng của bài không chỉ là tăng phát hiện nhờ ngữ cảnh, mà còn là chỉ ra rằng đánh giá phát hiện lỗ hổng nên đo **cả độ đúng của nhãn và độ đúng của lập luận bảo mật**.

---

# PHẦN 2: BÁO CÁO TỔNG HỢP KIẾN THỨC

**Tên bài báo:** DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection  
**Tác giả:** Mingyang Sun, Guozhu Meng  
**Bài toán:** Phát hiện lỗ hổng phụ thuộc ngữ cảnh liên hàm/liên tệp mà vẫn kiểm soát chi phí context và kiểm tra được mô hình có hiểu đúng nguyên nhân bảo mật hay không.

## Vấn đề cốt lõi (Problem Formulation)

Một hàm đơn lẻ có thể không bộc lộ lỗi nếu điều kiện khai thác, kiểm tra quyền, xác thực hoặc cấu hình được định nghĩa ở nơi khác. Retrieval cố định có thể bỏ sót bằng chứng cần thiết hoặc đưa dữ liệu nhiễu; gửi cả repository tới LLM suy luận mạnh lại tốn kém và dễ quá tải. DREA giải quyết bằng điều tra chủ động: lập giả thuyết, truy xuất bằng chứng phù hợp, cập nhật và quyết định.

## Kiến thức và kỹ thuật trọng tâm

- **Hypothesis-driven exploration:** việc tìm repository được điều khiển bởi giả thuyết bảo mật hiện tại.
- **Planner–Explorer separation:** mô hình suy luận mạnh tập trung vào kết luận; mô hình nhẹ/cục bộ đảm nhiệm điều hướng và thu thập thông tin.
- **Repository-grounded paired benchmark:** giữ liên kết giữa CVE, hàm dễ tổn thương, bản vá và hai trạng thái repository.
- **Pair-Correctness:** yêu cầu phân loại đúng cả hai thành viên của cặp vulnerability/fix.
- **Reasoning correctness và Lucky Hits:** phân biệt phát hiện đúng có căn cứ với trường hợp đúng nhãn nhưng giải thích sai.
- **Ablation và cost accounting:** so sánh với function-only, whole-file, single-agent; tách token API khỏi token xử lý cục bộ.

## Cơ chế hoạt động (Workflow & Methodology)

1. Nhận hàm mục tiêu, đường dẫn tệp và repository snapshot.
2. Planner lập giả thuyết về thao tác nguy hiểm hoặc ranh giới bảo mật có thể bị vi phạm.
3. Planner yêu cầu Explorer tìm bằng chứng cụ thể bằng các thao tác đọc repository.
4. Explorer trả context, trích đoạn mã và phát hiện bảo mật dưới dạng có cấu trúc.
5. Planner đối chiếu, cập nhật giả thuyết và tiếp tục truy vấn nếu cần.
6. Planner dừng khi đủ bằng chứng hoặc hết ngân sách, trả nhãn vulnerable/benign cùng trigger path hoặc guarding evidence.
7. Đánh giá bằng Recall/FPR/F1, Pair-Correctness và kiểm tra reasoning correctness trên true positives.

## Kết quả tiêu biểu

- RepoPairBench: 100 cặp Python, 48 CWE, 200 phiên bản repository-grounded.
- P-C tăng từ 19% lên 42% với DeepSeek-V3.2, từ 26% lên 34% với GLM-4.7, từ 21% lên 30% với GPT-5.2 so với Function-Only.
- Trong ablation DeepSeek-V3.2: Function-Only 19% P-C, Whole-File 26%, Single-Agent 24%, DREA 42%.
- Explorer xử lý 93,7–97,9% token tại chỗ; chi phí API ước tính thấp hơn 16–48 lần so với kịch bản mọi token đều chạy qua API, chưa tính GPU cục bộ.
- Tỷ lệ Lucky Hit trong true positives của DREA là 32,1–55,0%, cho thấy chất lượng lập luận vẫn cần cải thiện.

## Phân tích ưu điểm và hạn chế

**Ưu điểm:** truy xuất ngữ cảnh theo giả thuyết; có bằng chứng cụ thể để hỗ trợ kết luận; kiến trúc phân vai giúp kiểm soát token và hạn chế đưa mã thô vào Planner; ablation tương đối có hệ thống; đánh giá theo cặp; bổ sung đánh giá nguyên nhân/lập luận thay vì chỉ nhãn.

**Hạn chế:** benchmark còn nhỏ và chỉ có Python; mỗi CWE có ít mẫu; đánh giá reasoning thủ công chỉ 50 trường hợp; ước tính tiết kiệm bỏ qua chi phí GPU; mô hình Explorer và công cụ vẫn có thể trả kết quả chưa hoàn hảo; judge tự động vẫn cần xác nhận rộng hơn; nhãn benign chỉ có nghĩa đối với CVE mục tiêu; nhiều true positive vẫn là Lucky Hits.

## Bài học và liên hệ nghiên cứu

- Với lỗi bảo mật cấp repository, nên yêu cầu hệ thống nêu **trigger path** hoặc **bằng chứng bảo vệ**, để người đọc kiểm chứng thay vì chỉ nhận nhãn.
- Nên tách câu hỏi “có tìm thấy đủ thông tin không?” khỏi câu hỏi “có suy luận đúng từ thông tin đó không?”. Nhiều lượt tìm kiếm hơn không đảm bảo phân tích tốt hơn.
- Benchmark nên ghép mã lỗi với bản vá, và báo cáo đồng thời chỉ số theo mẫu, theo cặp, false positive/false negative và độ đúng của lời giải thích.
- Khi áp dụng vào code review, Planner–Explorer có thể được dùng để điều tra pull request: truy vết đầu vào, kiểm tra sanitization/authorization ở nơi khác, lưu bằng chứng và chỉ kết luận khi tạo được chuỗi nguyên nhân hợp lý.
- Hướng phát triển tiếp theo gồm benchmark đa ngôn ngữ và lớn hơn, Explorer chuyên biệt hơn, chính sách dừng thông minh, và đánh giá reasoning bằng chuyên gia/multiple judges với tập lớn hơn.

## Nhận xét tổng hợp

DREA là bước tiến từ “bổ sung ngữ cảnh” sang “điều tra ngữ cảnh theo giả thuyết”. Thiết kế hai agent cải thiện phát hiện theo cặp và làm repository-level analysis khả thi hơn về lượng token API. Tuy vậy, bài báo cũng cho thấy giới hạn sâu hơn của LLM trong an ninh phần mềm: truy cập được mã nguồn không đồng nghĩa với hiểu đúng cơ chế khai thác. Vì thế, một hệ thống thực tiễn cần tối ưu đồng thời việc tìm bằng chứng, tổng hợp lập luận, kiểm soát báo động giả và khả năng giải thích có thể xác minh.

