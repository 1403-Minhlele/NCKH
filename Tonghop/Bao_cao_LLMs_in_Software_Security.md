# PHẦN 1: TƯ DUY & PHÂN TÍCH TỪNG BƯỚC

### **Giải mã bối cảnh & Vấn đề nghiên cứu**
- **Bài toán cốt lõi:** Số lượng lỗ hổng phần mềm tăng vọt (hơn 120.000 CVE trong 5 năm qua) kéo theo thiệt hại lớn. Mặc dù Mô hình Ngôn ngữ Lớn (LLMs) đang tỏ ra rất mạnh mẽ trong việc phân tích mã nguồn và phát hiện lỗi, bức tranh tổng thể về các kỹ thuật ứng dụng, phương pháp luận (methodologies) và dữ liệu đánh giá vẫn chưa được hệ thống hóa, dẫn tới khó khăn trong việc xây dựng các công cụ thực tiễn.
- **Hạn chế của phương pháp truyền thống:**
    - _Phân tích tĩnh (Static Analysis) & Phân tích động (Dynamic Analysis / Fuzzing):_ Đòi hỏi cấu hình phức tạp, tỷ lệ dương tính giả (false positive) cực kỳ cao và khó mở rộng quy mô trước sự phức tạp của phần mềm hiện đại.
    - _Học máy truyền thống:_ Thiếu khả năng thấu hiểu ngữ cảnh sâu và suy luận logic (reasoning) phức tạp để tìm ra nguyên nhân gốc rễ của lỗ hổng.

### **Hệ thống hóa kiến thức nền tảng & Cơ chế hoạt động**
- **Khái niệm & Kỹ thuật trọng tâm:** Hệ thống phân loại phương pháp tiếp cận LLM trong bảo mật mã nguồn:
    1. _Task Formulation (Định hình bài toán):_ Phân loại lỗ hổng nhị phân/đa lớp (theo mã CWE) và dự đoán mức độ nghiêm trọng của lỗ hổng (dựa vào điểm CVSS score từ 0-10).
    2. _Model Architectures (Kiến trúc mô hình):_ 
       - Encoder-only (CodeBERT): Tối ưu cho hiểu mã và phân tích tĩnh.
       - Encoder-Decoder (CodeT5): Cân bằng giữa phân tích và sinh mã.
       - Decoder-only (GPT-3.5/GPT-4, CodeLlama): Đang trở thành xu hướng chủ đạo (chiếm >67% lượt sử dụng) nhờ khả năng suy luận mạnh mẽ, sửa lỗi và giải thích nguyên nhân gốc rễ.
    3. _Triển khai thực tế (Deployment Strategies):_ FullScan (Quét toàn bộ dự án, ví dụ OSSFuzzGen) vs DeltaScan (Quét từng thay đổi/commit mới để chặn lỗ hổng từ sớm).
- **Cơ chế hoạt động cốt lõi (Input $\rightarrow$ Xử lý $\rightarrow$ Output):**
  $$\text{Code Snippet + Auxiliary Context (CWE/CVSS)} \xrightarrow{\text{LLM Architecture (Decoder-dominant) + Multi-Agent}} \text{Vulnerability Type (CWE-ID) + Severity Score (CVSS)}$$

| Trục phân loại            | Thành phần kỹ thuật                 | Diễn giải cơ chế & Ứng dụng thực tế                                                                                                                                                                               |
| ------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Task Formulation**      | **Detection & Severity Prediction** | Không chỉ phát hiện lỗ hổng (Có/Không), hệ thống mở rộng sang phân loại chi tiết mã CWE (VD: CWE-79 XSS) và dự đoán điểm nghiêm trọng (CVSS score) để ưu tiên xử lý.                                              |
| **Model Architectures**   | **Frontier LLMs (Decoder-only)**    | Sử dụng các mô hình Decoder khổng lồ (GPT-4o, Claude 3.5, Llama-3) thay cho các mô hình nhỏ kiểu cũ. Tận dụng khả năng lập luận qua cửa sổ ngữ cảnh (context window) siêu dài thay vì chỉ phân loại từ vựng tĩnh. |
| **Real-world Deployment** | **FullScan & DeltaScan**            | Ứng dụng vào quy trình CI/CD: Dùng FullScan (kết hợp Fuzzing) cho các đợt release lớn và DeltaScan (như FuzzBrain) cho việc chặn lỗ hổng sinh ra ngay tại các commit mới.                                         |

### **Đánh giá thực nghiệm & Kết quả**
- **Tập dữ liệu & Chỉ số:** Khảo sát chi tiết các tập dữ liệu nổi bật phân theo ngôn ngữ. C/C++, Java và Solidity chiếm ưu thế tuyệt đối. Dữ liệu hầu hết ở mức hàm (function-level - như Devign, CVEFixes) và mức tệp (file-level).
- **Kết quả & Phát hiện định lượng:**
    - _Sự mất cân bằng loại lỗ hổng:_ Các lỗ hổng về an toàn bộ nhớ (Memory-safety như buffer overflow ở C/C++) có độ chính xác nhận diện cực cao, trong khi các lỗ hổng logic nghiệp vụ phức tạp lại bị ngó lơ hoặc nhận diện rất kém.
    - _Hạn chế về quy mô (Granularity):_ Rất thiếu các tập dữ liệu ở cấp độ toàn kho lưu trữ (repository-level), khiến mô hình gặp "điểm mù" trước các lỗ hổng phân tán xuyên tệp (cross-file dependencies) và ngăn xếp lời gọi hàm sâu (long call stacks).

## **Đúc kết & Liên hệ nghiên cứu**

### Ưu điểm & Đột phá kỹ thuật:
*  **Khung triển khai thực tế (Deployment Framework):** Bài báo là một trong số ít những nghiên cứu chỉ ra cách thức ứng dụng LLM vào môi trường phần mềm thực tế thông qua chiến lược FullScan và DeltaScan.
*  **Liên kết trực tiếp với tri thức an ninh mạng (Domain Knowledge):** Nêu bật việc tích hợp chặt chẽ các chuẩn bảo mật toàn cầu (CVE, CWE, CVSS) vào đầu vào và đầu ra của LLM.
*  **Nhận thức đạo đức (Ethics & Dual-use):** Phân tích rủi ro sử dụng kép (kẻ xấu dùng LLM sinh mã khai thác) và vấn đề rò rỉ mã nguồn nhạy cảm (data privacy).

### Hạn chế & Góc khuất kỹ thuật (Technical Limitations):
*  **Mù ngữ cảnh rộng (Inadequate Context Awareness):** Các LLM hiện tại làm rất tốt trên đoạn mã ngắn nhưng thường thất bại khi phải truy vết (taint tracking) dữ liệu ô nhiễm qua nhiều tệp tin khác nhau.
* **Chất lượng Dataset:** Dữ liệu có xu hướng hẹp, thường xuyên xảy ra tình trạng rò rỉ dữ liệu (data leakage) giữa tập huấn luyện và tập kiểm thử.

### **Bài học rút ra (Key Takeaways):**
- Phát hiện lỗ hổng không chỉ là gán nhãn đúng/sai, mà còn là cung cấp mã CWE và mức độ nghiêm trọng CVSS để tích hợp trơn tru vào quy trình DevSecOps (thông qua DeltaScan).
- **Hướng kế thừa / mở rộng:** Phát triển các mô hình Neuro-Symbolic (ví dụ: dùng CodeQL tạo tập luật, LLM chịu trách nhiệm suy diễn) kết hợp hệ thống Đa tác tử (Multi-agent) để chia nhỏ bài toán quét kho lưu trữ (Repository-level) thay vì quét các tệp đơn lẻ.

---

# PHẦN 2: BÁO CÁO TỔNG HỢP KIẾN THỨC

**Tên chủ đề / Bài báo:** LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights (Ze Sheng et al.)

**Vấn đề cốt lõi (Problem Formulation):**
Mặc dù LLM đang cho thấy tiềm năng to lớn trong bảo mật mã nguồn, sự phát triển của lĩnh vực này đang bị phân mảnh. Bài báo thực hiện khảo sát chuyên sâu về việc áp dụng LLM trong riêng mảng phát hiện lỗ hổng, phân tích cấu trúc mô hình, tập dữ liệu, cách thức triển khai thực tế và những thách thức đang cản trở LLM hiểu được các lỗ hổng cấp độ dự án (repository-level).

**Kiến thức & Kỹ thuật trọng tâm:**
- Kiến trúc Decoder-only (GPT-4, Llama) chiếm lĩnh nhờ khả năng lập luận phức tạp và sinh mô tả/bản vá linh hoạt.
- Kết nối tri thức ngành: Mapping mã nguồn với các định chuẩn CVE, CWE và chấm điểm CVSS.
- Chiến lược DeltaScan: Ứng dụng LLM như một công cụ rà soát từng commit (thay đổi) theo thời gian thực để ngăn chặn các bản cập nhật gây lỗi trước khi đưa vào nhánh chính.

**Cơ chế & Luồng hoạt động của giải pháp (Workflow & Methodology):**
- **Luồng phân tích thông thường**: Mã nguồn thô $\rightarrow$ Làm giàu ngữ cảnh bằng Prompt Engineering / RAG (nhúng kiến thức CWE) $\rightarrow$ Đưa qua hệ thống LLM (thường kết hợp luồng Multi-agent: Tác tử phân tích, Tác tử đối chiếu luật) $\rightarrow$ Trả về Báo cáo lỗ hổng (Gồm: Trạng thái, Loại CWE, Nguyên nhân gốc rễ, và Điểm CVSS).
- **Triển khai DeltaScan**: Lấy diff từ commit $\rightarrow$ Kết hợp LLM và Fuzzing driver tạo ca kiểm thử $\rightarrow$ Xác nhận xem mã mới có làm hỏng chương trình (crash) không $\rightarrow$ Cảnh báo hoặc Sinh bản vá tức thời.

**Phân tích Ưu điểm & Hạn chế:**
- *Ưu điểm:* Tập trung mạnh mẽ vào ứng dụng công nghiệp, đặc tả chi tiết môi trường, dữ liệu và ngôn ngữ bị ảnh hưởng (C/C++, Java, Solidity), giúp lập trình viên định hình rõ các loại công cụ cần xây dựng. Có quan tâm sâu sắc tới đạo đức AI (Sử dụng kép).
- *Hạn chế:* Vạch trần sự yếu kém của giới nghiên cứu hiện tại trong việc tạo ra một tập dữ liệu (dataset) sạch, có mức độ khó cao tương xứng với phần mềm thực tế (liên tệp, cấu trúc sâu).

**Bài học & Hướng ứng dụng (Personal Insights):**
- Để tạo ra các công cụ dò quét lỗ hổng thế hệ mới, sự dịch chuyển bắt buộc là chuyển từ phân tích cấp hàm (function-level) sang cấp kho lưu trữ (repository-level).
- Trong nghiên cứu/dự án tiếp theo, nên kết hợp sức mạnh của một công cụ tĩnh (Static Analyzer) chuyên trích xuất sơ đồ gọi hàm (call graph) rồi cấp dưới dạng ngữ cảnh (Context) cho Frontier LLM (GPT-4o / Claude 3.5), áp dụng theo luồng DeltaScan vào hệ thống CI/CD để đạt hiệu quả tối đa.
