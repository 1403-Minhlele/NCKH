# PHẦN 1: 
# PHẦN 1: 

### **Giải mã bối cảnh & Vấn đề nghiên cứu**

- **Bài toán cốt lõi:** Lĩnh vực phát hiện lỗ hổng phần mềm bằng Mô hình Ngôn ngữ Lớn (LLMs) bùng nổ mạnh mẽ (hơn 40.000–48.000 CVE mỗi năm giai đoạn 2024–2025), nhưng bức tranh nghiên cứu đang bị **phân mảnh nghiêm trọng**. Các công trình có sự phân tán lớn về cách xây dựng bài toán, biểu diễn đầu vào, kiến trúc hệ thống, kỹ thuật thích nghi và cách dùng dataset, dẫn đến việc thiếu chuẩn mực so sánh công bằng (benchmarking) và đánh giá độ tin cậy thực tế.
- **Hạn chế của phương pháp truyền thống:**
    - _Công cụ phân tích tĩnh (SAST / Rule-based):_ Phụ thuộc vào các quy tắc cứng do chuyên gia định nghĩa thủ công, tỷ lệ dương tính giả (false positive) rất cao, khó mở rộng theo quy mô phát triển phần mềm hiện đại.
    - _Học sâu truyền thống (DL/GNN cổ điển):_ Chỉ giới hạn ở bài toán phân loại nhị phân đơn giản (`vulnerable`/`non-vulnerable`), thiếu khả năng giải thích nguyên nhân gốc rễ, thiếu tri thức ngữ nghĩa toàn cục và dễ suy giảm hiệu năng khi mã nguồn thay đổi cú pháp.

### **Hệ thống hóa kiến thức nền tảng & Cơ chế hoạt động**

- **Khái niệm & Kỹ thuật trọng tâm:** Hệ thống phân loại (Taxonomy) 4 chiều toàn diện:
    1. _Task Formulation (F):_ Phân loại (Binary, Specific-vulnerability, Multi-class, Multi-label CWE) vs. Sinh (Mô tả lỗ hổng, suy luận nguyên nhân gốc - Root-cause reasoning, Báo cáo có cấu trúc JSON/SARIF).
    2. _Input Representation (I):_ Mã thô (Raw text) vs. Mã có cấu trúc (AST, CFG, DFG, PDG, CPG, Program Slicing, Code Gadgets) kết hợp Thông tin bổ trợ (Auxiliary Info: CWE descriptions, runtime traces, SAST outputs).
    3. _System Architecture (S):_ Lấy LLM làm trung tâm (Encoder-only, Encoder-Decoder, Decoder-only; từ Tiny <1B đến Large >70B) vs. Hệ thống lai (LLM kết hợp RNN/CNN/GNN).
    4. _Techniques (T):_ Thích nghi (Prompting: Zero-shot, Few-shot, CoT, RAG; Fine-tuning: Full-parameter, PEFT như LoRA/QLoRA/PiSSA/GaLore; Learning Paradigms: Contrastive, Causal, Multi-task, Continual Learning, RL/RLAIF) và Điều phối (Multi-Step, Verification/Self-reflection, Multi-Agent/ReAct, Ensemble, Controller/MoE).
- **Cơ chế hoạt động cốt lõi (Input $\rightarrow$ Xử lý $\rightarrow$ Output):** $$\text{Source Code + Auxiliary Context} \xrightarrow{\text{Slicing/CPG/Prompt Eng.}} \text{Prompt/Embeddings} \xrightarrow{\text{LLM / Hybrid + Reasoning/Agent}} \text{Vulnerability Status + CWE-ID + Root-cause}$$

| Trục phân loại            | Thành phần kỹ thuật                  | Diễn giải cơ chế & Ứng dụng thực tế                                                                                                                                                                                                                                  |
| ------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Task Formulation**      | **Classification & Generation**      | Chuyển từ phân loại nhị phân thô sơ (`Có`/`Không`) sang phân loại đa nhãn CWE, tạo báo cáo lỗ hổng có cấu trúc (JSON/SARIF) và **suy luận nguyên nhân gốc rễ (Root-cause reasoning)** theo luồng xuôi/ngược.                                                         |
| **Input Representation**  | **Structure-aware & Auxiliary Info** | Vượt qua giới hạn mã thô (raw text) bằng cách tích hợp biểu diễn cú pháp - ngữ nghĩa: **CPG** (kết hợp AST + CFG + PDG), **Program Slicing**, **Code Gadgets**; bổ trợ thêm metadata CWE, runtime traces và kết quả từ công cụ phân tích tĩnh (SAST).                |
| **Model Architectures**   | **LLM-Centric & Hybrid**             | Mô hình Decoder-only (GPT-4, Llama-3, Qwen-Coder, DeepSeek) chiếm ưu thế áp đảo cho suy luận; Kiến trúc lai kết hợp LLM Embedding với **GNN / CNN / BiLSTM** để trích xuất đặc trưng cấu trúc đồ thị mã.                                                             |
| **Adaptation Techniques** | **PEFT & Learning Paradigms**        | Tối ưu hóa tham số qua **LoRA, QLoRA, PiSSA, GaLore**; kết hợp các mô hình học nâng cao: **Contrastive Learning** (phân biệt mã an toàn và mã lỗi tương đồng), **Causal Learning** (khử tương quan giả), **Multi-task Learning** (vừa phát hiện vừa sửa lỗi).        |
| **Orchestration Systems** | **Agentic & Verification**           | Thiết kế quy trình suy luận phức hợp: **Multi-Step** (hiểu chức năng trước $\rightarrow$ tìm lỗi sau), **Verification / Reflection** (mô hình tự kiểm tra phản biện), **Multi-Agent** (mô phỏng nhóm chuyên gia: Researcher, Auditor, Reviewer), **MoE Controller**. |
| **Datasets & Evaluation** | **CWE-1000 Analysis**                | Đánh giá 15 benchmark chính (Big-Vul, Devign, DiverseVul, CVEfixes, PrimeVul, CleanVul...); chỉ rõ vấn đề phân phối **long-tail**, **thiên lệch ngôn ngữ C/C++** (thiếu Python/Java) và nguy cơ **data leakage**.                                                    |

### **Đánh giá thực nghiệm & Kết quả**

- **Tập dữ liệu & Chỉ số:** Khảo sát 263 công trình (2020 – 11/2025) trên IEEE, ACM, arXiv. Phân tích các bộ dữ liệu tiêu biểu: _Synthetic_ (Juliet, SARD), _Real-world_ (Devign, Big-Vul, MegaVul, CVEfixes, DiverseVul), _Constructed/LLM-evaluated_ (SecurityEval, SVEN, PrimeVul, CleanVul, FormAI). Đánh giá dựa trên ma trận CWE-1000 Research View (10 Pillars).
- **Kết quả & Phát hiện định lượng:**
    - _Mất cân bằng dữ liệu & Phân phối Long-tail:_ Top 25 CWE chiếm đến 80% nhãn trong các bộ dữ liệu thực tế, tập trung chủ yếu vào nhóm quản lý bộ nhớ C/C++ (_Improper Control of a Resource_); hơn 555 CWE hợp lệ trong CWE-1000 hoàn toàn vắng bóng trong các benchmark.
    - _Rò rỉ dữ liệu (Data Leakage):_ Đa số benchmark phổ biến (Devign, Big-Vul) đã nằm trong tập tiền huấn luyện của các mô hình nền tảng, khiến kết quả đánh giá phản ánh khả năng "ghi nhớ" hơn là "suy luận tổng quát".
    - _Nhiễu nhãn (Label Noise):_ Các phương pháp gắn nhãn tự động dựa trên VFC (Vulnerability Fixing Commits) thường đưa vào nhiều thay đổi không liên quan (refactoring, comment).

## **Đúc kết & Liên hệ nghiên cứu**

### Ưu điểm & Đột phá kỹ thuật:

*  **Tính linh hoạt và tri thức ngữ nghĩa toàn cục:** LLM có khả năng hiểu các mẫu lập trình phức tạp, thích nghi đa ngôn ngữ mà không cần viết lại tập luật thủ công như SAST.
*  **Khả năng giải thích và hỗ trợ tương tác:** Không chỉ gắn cờ cảnh báo, LLM có thể cung cấp ngữ cảnh, giải thích dòng mã gây lỗi và gợi ý bản vá (patch suggestion).
* * **Sự phát triển của hệ thống tác tử (Agentic Workflows):** Phối hợp nhiều agent với các vai trò chuyên biệt giúp giảm đáng kể tỷ lệ ảo giác (hallucination) và nâng cao độ chính xác trong các dự án lớn.

### Hạn chế & Góc khuất kỹ thuật (Technical Limitations):

*  **Giới hạn Granularity (Cấp độ phân tích):** Hầu hết các nghiên cứu chỉ chạy trên từng hàm riêng lẻ (function-level), bất lực trước các lỗ hổng phân tán liên tệp (inter-procedural / project-level vulnerabilities).
* ***Chất lượng Dataset & Hiện tượng rò rỉ dữ liệu (Data Leakage):** Nhiều tập dữ liệu thực tế chứa nhiễu nhãn lớn do khai thác VFC tự động; các mô hình LLM hiện đại có thể đã "thuộc lòng" các benchmark cũ, dẫn đến điểm số cao ảo trên bài báo nhưng kém hiệu quả trong thực tế.
* * **Phân phối Long-tail & Thiếu biểu diễn CWE:** Đa số các mô hình chỉ giỏi phát hiện các lỗi an toàn bộ nhớ C/C++ quen thuộc (Buffer Overflow, Null Pointer), trong khi các lỗi logic nghiệp vụ, xác thực quyền truy cập hay kiểm soát luồng phức tạp bị bỏ sót nghiêm trọng

### **Bài học rút ra (Key Takeaways):** 
- Không nên tiếp tục giải quyết bài toán phát hiện lỗ hổng dưới dạng phân loại nhị phân ở mức hàm đơn lẻ (function-level binary classification) trên mã thô. Cần chuyển dịch sang **hệ thống nhận biết cấu trúc (Structure-aware)**, **đa tác tử cộng tác (Multi-Agent/Agentic)** kết hợp **suy luận nguyên nhân gốc rễ (Root-cause reasoning)** và đánh giá trên **ngữ cảnh liên tệp (inter-procedural / project-level)**.
- **Hướng kế thừa / mở rộng:** Xây dựng quy trình phát hiện lỗ hổng kết hợp biểu diễn đồ thị (CPG/Code Gadgets) + RAG với cơ sở tri thức CWE chuyên sâu + Cơ chế tự kiểm tra/phản biện (Self-Verification / Multi-agent Debating) để loại bỏ dương tính giả.

