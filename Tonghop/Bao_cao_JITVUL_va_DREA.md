# Tổng hợp hai bài báo trong `New_paper`

Hai bài cùng nghiên cứu phát hiện lỗ hổng ở cấp repository bằng LLM, nhưng đóng góp khác nhau: JITVUL tập trung vào **benchmark và đánh giá agent**, còn DREA tập trung vào **kiến trúc agent khám phá repository có định hướng** và đánh giá chất lượng lập luận.

---

# Bài 1 — Benchmarking LLMs and LLM-based Agents in Practical Vulnerability Detection for Code Repositories

**Tệp:** `2025.acl-long.1490 (1).pdf`  
**Tác giả:** Alperen Yildiz, Sin G. Teo, Yiling Lou, Yebo Feng, Chong Wang, Dinil Mon Divakaran  
**Công bố:** ACL 2025, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, tr. 30848–30865.

## Phần 1: Tư duy và phân tích từng bước

### Bối cảnh và vấn đề nghiên cứu

Phần lớn benchmark phát hiện lỗ hổng đưa riêng một hàm vào mô hình. Cách này bỏ qua quan hệ liên thủ tục: lỗ hổng có thể chỉ xuất hiện khi lần theo nhiều tầng gọi hàm, điều kiện nhánh và ngữ cảnh của repository. Benchmark repository-level hiện có bổ sung caller/callee, nhưng thường tốn kém khi rà mọi hàm, chưa kiểm tra tốt việc phân biệt phiên bản trước và sau khi vá, và chủ yếu dùng ngữ cảnh được truy xuất theo quy tắc cố định.

Bài báo đặt bài toán thực tế hơn: **just-in-time (JIT) vulnerability detection**. Chỉ các hàm bị thay đổi trong commit được phân tích; mỗi hàm được gắn với trạng thái có lỗ hổng và trạng thái đã vá để kiểm tra mô hình có nhận ra đúng thay đổi bảo mật hay không.

### Đóng góp chính: benchmark JITVUL

- Xây dựng JITVUL từ **879 CVE**, bao phủ **91 CWE**.
- Tạo **1.758 mẫu theo cặp**: 879 phiên bản dễ tổn thương và 879 phiên bản lành tính đã vá.
- Mỗi mẫu gắn với repository và hàm mục tiêu; quy mô repository trung bình khoảng 2.956 tệp. Mục tiêu là đánh giá trên tình huống có ngữ cảnh liên thủ tục, thay vì chỉ đưa một đoạn hàm cô lập.
- Dùng thêm **pairwise accuracy (pAcc)**: một cặp chỉ được tính đúng khi mô hình nhận diện đúng cả hàm lỗi lẫn hàm đã vá. Chỉ số này bổ sung cho F1 vốn có thể bị ảnh hưởng mạnh bởi phân bố nhãn.

### Các phương pháp được so sánh

1. **Plain LLM:** chỉ cung cấp mã mục tiêu.
2. **Dependency-augmented LLM:** đưa caller/callee được truy xuất theo cách cố định vào prompt.
3. **ReAct Agent:** cho agent lặp lại chu trình suy luận–gọi công cụ–quan sát để truy xuất caller/callee khi cần.

Thí nghiệm dùng GPT-4o-mini và GPT-4o, với các biến thể prompt: thông thường, Chain-of-Thought (CoT), few-shot (FS), và CoT kết hợp FS. Công cụ truy xuất call graph là CFlow; nhiệt độ mô hình đặt bằng 0.

### Kết quả và phát hiện

ReAct đạt pAcc cao hơn các phương pháp LLM khác ở mọi chiến lược prompt, với mức tăng được báo cáo từ **0,1 đến 16,61 điểm phần trăm**. Trong khi đó, Plain LLM và dependency-augmented LLM thường có F1 cao hơn. Điều này cho thấy F1 cao không đồng nghĩa với việc mô hình phân biệt tốt giữa mã lỗi và mã đã vá.

Một số thiết lập LLM gán nhãn “vulnerable” cho hơn 90% mẫu: recall tăng nhưng nhiều phiên bản lành tính cũng bị báo động, khiến pAcc thấp. ReAct dùng ngữ cảnh động để so sánh phiên bản trước/sau sửa; agent thường gọi công cụ từ một đến ba lần. Truy xuất cố định có thể đưa thêm ngữ cảnh nhiễu và không bảo đảm cải thiện so với chỉ dùng mã mục tiêu.

### Ưu điểm

- Benchmark ghép cặp kiểm tra trực tiếp khả năng nhận ra tác động của bản vá.
- Đánh giá cả F1 và pAcc làm rõ sự khác biệt giữa phát hiện nhiều mẫu dương tính và hiểu đúng đặc điểm lỗ hổng.
- ReAct cho thấy giá trị của việc truy xuất ngữ cảnh có điều kiện trong phân tích JIT.

### Hạn chế

- Việc lần ngược commit đưa lỗ hổng vào mã có thể khó chính xác do lịch sử phát triển phức tạp; nhóm có kiểm tra thủ công một số trường hợp.
- Tập cân bằng nhãn hữu ích cho đánh giá theo cặp nhưng không phản ánh trực tiếp tỷ lệ lỗ hổng ngoài thực tế, nên F1 có thể thay đổi theo phân bố dữ liệu.
- Chưa có thống kê đầy đủ về tỷ lệ lỗ hổng thực sự cần phân tích liên thủ tục.
- Bài báo ghi nhận agent vẫn chưa ổn định: có lúc bỏ sót điểm sửa, có lúc suy đoán hoặc xem các biện pháp bảo vệ là dấu hiệu lỗi.

### Kết luận

JITVUL đóng góp một thiết lập đánh giá sát thực tế hơn cho phát hiện lỗ hổng theo commit. Kết quả ủng hộ việc đo chất lượng theo cặp và cho thấy ReAct khai thác ngữ cảnh liên thủ tục hiệu quả hơn trong việc phân biệt hai phiên bản, dù còn cần cải thiện suy luận và tính nhất quán.

## Phần 2: Báo cáo tổng hợp kiến thức

**Vấn đề cốt lõi:** Mô hình phải nhận ra lỗ hổng trong hàm vừa thay đổi, tận dụng ngữ cảnh repository, đồng thời phân biệt hàm dễ tổn thương với chính hàm đó sau khi được vá.

**Kiến thức/kỹ thuật trọng tâm:** JIT detection; benchmark hàm theo cặp vulnerable/patched; truy xuất caller/callee; ReAct; CoT và few-shot; đánh giá bằng F1 kết hợp pairwise accuracy.

**Luồng phương pháp:** Chọn CVE → xác định commit đưa lỗi vào và commit sửa → trích xuất hàm mục tiêu ở hai trạng thái → cung cấp repository/context cho LLM hoặc agent → dự đoán từng phiên bản → tính F1 và tỷ lệ cặp được phân loại đúng.

**Bài học:** Khi cần kiểm tra mô hình có hiểu tác dụng của bản vá hay không, chỉ số trên từng mẫu như F1 chưa đủ. Cần kiểm tra xem mô hình có nhận diện đúng cả hai phía của mỗi cặp. Context retrieval cũng cần được đánh giá theo chất lượng và tính phù hợp, không chỉ số lượng hàm được đưa vào prompt.

**Hướng ứng dụng:** Dùng JITVUL/pAcc để đánh giá công cụ rà soát pull request hoặc commit; phát triển agent có thể truy vấn call graph và xác minh khác biệt giữa mã trước và sau bản vá.

---

# Bài 2 — DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection

**Tệp:** `2607.13439v1 (1).pdf`  
**Tác giả:** Mingyang Sun, Guozhu Meng  
**Phiên bản trong thư mục:** arXiv:2607.13439v1, ngày 15/07/2026.

## Phần 1: Tư duy và phân tích từng bước

### Bối cảnh và vấn đề nghiên cứu

Phát hiện lỗ hổng ở cấp hàm thường thiếu bằng chứng ở các tệp khác: luồng dữ liệu xuyên hàm, logic kiểm tra quyền, xác thực đầu vào hoặc cấu hình. Các phương pháp thêm ngữ cảnh theo quy tắc cố định khó biết cần tìm gì cho từng giả thuyết bảo mật. Cho một LLM đơn lẻ tự đọc toàn repository lại dễ tốn token và quá tải ngữ cảnh.

Bài báo đề xuất tách riêng hai việc: **suy luận bảo mật** và **khám phá repository**.

### Kiến trúc DREA

- **Planner:** LLM mạnh hình thành giả thuyết về lỗ hổng, đặt truy vấn cần điều tra, đọc kết quả, cập nhật giả thuyết và quyết định khi nào đã đủ bằng chứng.
- **Explorer:** mô hình nhẹ chạy cục bộ, dùng công cụ chỉ đọc để tìm kiếm repository và trả lại bằng chứng có cấu trúc cho Planner.
- Quy trình lặp: giả thuyết → truy vấn → bằng chứng mã nguồn/ngữ cảnh → cập nhật → kết luận vulnerable hoặc benign kèm giải thích.

Điểm thiết kế chính là Explorer tìm theo hướng câu hỏi bảo mật hiện tại, còn Planner tổng hợp bằng chứng đã chọn lọc thay vì phải nhận toàn bộ mã nguồn thô.

### Benchmark và cách đánh giá

Nhóm giới thiệu **RepoPairBench**, gồm **100 cặp lỗ hổng–bản vá Python** (200 phiên bản), thu thập từ CVE giai đoạn 2021–2025 và trải trên 48 CWE. Mỗi cặp có repository snapshot trước và sau commit sửa; hệ thống được phép đọc repository tương ứng.

Ngoài Recall, false positive rate (FPR) và F1, bài báo dùng:

- **Pair-Correctness (P-C):** cả phiên bản lỗi và phiên bản đã vá đều được phân loại chính xác.
- **Youden’s J:** Recall trừ FPR, để cân bằng khả năng bắt lỗi và mức báo động giả.
- **Reasoning Accuracy (RA):** trong các trường hợp phát hiện đúng lỗ hổng, lời giải thích có khớp với cơ chế CVE và bản vá không.
- **Lucky Hit Rate (LHR):** tỷ lệ dự đoán đúng nhưng lý do sai.

LLM-as-a-Judge được đối chiếu với hai chuyên gia trên 50 trường hợp; mức đồng thuận được báo cáo là Cohen’s κ = 0,88–0,92.

### Kết quả chính

So với Function-Only Baseline dùng cùng backbone, DREA tăng P-C trên cả ba mô hình:

| Planner       | Recall DREA | FPR DREA | F1 DREA | P-C DREA | P-C baseline |
| ------------- | ----------: | -------: | ------: | -------: | -----------: |
| DeepSeek-V3.2 |         80% |      45% |   71,1% |      42% |          19% |
| GLM-4.7       |         59% |      38% |   59,9% |      34% |          26% |
| GPT-5.2       |         53% |      28% |   58,6% |      30% |          21% |

Thí nghiệm loại bỏ thành phần trên DeepSeek-V3.2 cho thấy Function-Only đạt P-C 19%; Whole-File 26%; DREA 42%. Single-Agent có đầy đủ công cụ khám phá nhưng đưa mã thô trực tiếp vào một mô hình đạt P-C 24% và FPR 64%. Kết quả gợi ý rằng tăng lượng ngữ cảnh hoặc quyền truy cập công cụ tự thân chưa đủ; cấu trúc Planner–Explorer và bằng chứng chọn lọc có vai trò quan trọng.

Explorer xử lý cục bộ **93,7–97,9% tổng token**. Bài báo ước tính chi phí API phải trả giảm khoảng **16–48 lần** so với giả định mọi token đều chạy qua API. Ước tính này không tính chi phí GPU cục bộ cho Explorer.

### Chất lượng lập luận và giới hạn

Từ **26–55%** dự đoán đúng ở nhóm true positive có lời giải thích không chính xác (Lucky Hits), tùy backbone/cấu hình. Lỗi thường gặp là nêu chung chung “thiếu kiểm tra đầu vào” dù cơ chế lỗi thực tế khác. Vì thế, độ chính xác nhãn không đảm bảo mô hình đã hiểu nguyên nhân bảo mật.

Kết quả theo CWE cho thấy hệ thống làm tốt hơn với lỗi có luồng dữ liệu rõ, như XSS hoặc code injection, so với lỗi dạng thiếu biện pháp bảo vệ như kiểm soát truy cập. Việc tìm thêm ngữ cảnh không tự động cải thiện suy luận; nhiều lượt khám phá có thể phản ánh trường hợp khó hơn.

Giới hạn do tác giả nêu: benchmark chỉ có 100 cặp Python; số mẫu mỗi CWE nhỏ (3–13 cặp); kiểm tra thủ công lời giải thích chỉ gồm 50 trường hợp. Explorer cục bộ được chạy trên một GPU A800 và có thể trả về lời gọi công cụ chưa hoàn hảo. Kết quả chưa chứng minh trực tiếp khả năng khái quát sang ngôn ngữ khác.

### Kết luận

DREA cải thiện khả năng nhận diện đồng thời phiên bản lỗi và bản vá bằng cách cho Planner điều tra repository theo giả thuyết, trong khi Explorer địa phương xử lý phần truy xuất tốn token. Tuy vậy, suy luận đúng cơ chế lỗ hổng vẫn là điểm nghẽn: hệ thống cần được đánh giá cả kết luận lẫn căn cứ của kết luận.

## Phần 2: Báo cáo tổng hợp kiến thức

**Vấn đề cốt lõi:** Làm sao cung cấp đúng bằng chứng cấp repository cho một cuộc điều tra bảo mật cụ thể, mà không đưa toàn bộ repository vào mô hình suy luận tốn kém hoặc làm mô hình quá tải.

**Kiến thức/kỹ thuật trọng tâm:** Multi-agent Planner–Explorer; khám phá repository theo giả thuyết; công cụ đọc mã; benchmark Python theo cặp CVE–patch; Pair-Correctness; đánh giá lập luận bằng LLM-as-a-Judge; Lucky Hits.

**Luồng hoạt động:** Nhận hàm và snapshot repository → Planner lập giả thuyết → yêu cầu Explorer tìm bằng chứng cụ thể → Explorer trả kết quả có cấu trúc → Planner cập nhật giả thuyết và tiếp tục hoặc dừng → trả nhãn cùng trigger path/guarding evidence → đánh giá cả nhãn và tính đúng đắn của lập luận.

**Ưu điểm:** Khai thác được bằng chứng xuyên tệp; tách khâu tìm kiếm khỏi suy luận; giảm token API; đánh giá theo cặp và kiểm tra lý do giúp phát hiện “đúng nhãn do may mắn”.

**Hạn chế:** Benchmark Python còn nhỏ; chi phí GPU Explorer chưa nằm trong ước tính tiết kiệm API; chất lượng cuối cùng còn phụ thuộc vào khả năng tổng hợp bằng chứng và hiểu cơ chế bảo mật; kết quả theo từng CWE chưa chắc chắn do ít mẫu.

**Bài học và hướng ứng dụng:** Hệ thống phát hiện lỗ hổng nên lưu lại bằng chứng và đường kích hoạt cụ thể, không chỉ xuất nhãn. Có thể áp dụng cấu trúc này cho rà soát bảo mật theo pull request: Planner đặt câu hỏi, công cụ truy vết dữ liệu/kiểm tra quyền cung cấp chứng cứ, rồi hệ thống xác minh cả thay đổi gây lỗi lẫn thay đổi khắc phục.

---

## Liên hệ giữa hai bài

| Khía cạnh        | JITVUL (ACL 2025)                         | DREA (arXiv 2026)                                    |
| ---------------- | ----------------------------------------- | ---------------------------------------------------- |
| Trọng tâm        | Benchmark JIT và so sánh LLM/ReAct        | Kiến trúc agent khám phá repository có định hướng    |
| Dữ liệu          | 879 CVE, 91 CWE; cặp hàm C/C++            | 100 cặp CVE–patch Python, 48 CWE                     |
| Ngữ cảnh         | Caller/callee, lấy cố định hoặc qua ReAct | Explorer truy vấn repository theo giả thuyết Planner |
| Đánh giá nổi bật | Pairwise accuracy                         | Pair-Correctness và đúng/sai của lập luận            |
| Kết luận chung   | Cần đo việc phân biệt mã lỗi với mã đã vá | Cần đo cả nhãn lẫn việc mô hình hiểu đúng cơ chế lỗi |

**Nhận xét tổng hợp:** JITVUL đặt nền tảng đánh giá theo cặp và cho thấy agent truy xuất linh hoạt có ích hơn ngữ cảnh cố định trong một số chỉ số. DREA mở rộng hướng này bằng kiến trúc tách biệt suy luận và khám phá, đồng thời chỉ ra rằng thêm context chưa giải quyết được chất lượng lập luận. Hai bài cùng ủng hộ đánh giá theo bản vá và bằng chứng; hướng nghiên cứu kế tiếp là tăng độ tin cậy của lập luận, giảm báo động giả và mở rộng benchmark đa ngôn ngữ/quy mô lớn.
