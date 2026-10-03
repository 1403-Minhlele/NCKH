# BÁO CÁO KHOA HỌC CHUYÊN SÂU: PHÂN TÍCH TOÀN DIỆN 5 BÀI BÁO KHOA HỌC

## ỨNG DỤNG MÔ HÌNH NGÔN NGỮ LỚN (LLM) VÀ AI AGENT TRONG PHÁT HIỆN LỖ HỔNG BẢO MẬT & LẬP TRÌNH AN TOÀN

---

## MỤC LỤC

1. [Giới Thiệu Tổng Quan Bộ Sưu Tập 5 Bài Báo Khoa Học](#1-giới-thiệu-tổng-quan-bộ-sưu-tập-5-bài-báo-khoa-học)
2. [Bài Báo 1: JITVUL - Đánh Giá LLM Và ReAct Agent Trong Phát Hiện Lỗ Hổng Just-in-Time (ACL 2025 Long)](#2-bài-báo-1-jitvul---đánh-giá-llm-và-react-agent-trong-phát-hiện-lỗ-hổng-just-in-time-acl-2025-long)
   - 2.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu
   - 2.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?
   - 2.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)
   - 2.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)
   - 2.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 2 & Bảng 4)
   - 2.6. Điểm Mạnh Của Nghiên Cứu
   - 2.7. Điểm Yếu & Khoảng Trống Nghiên Cứu
3. [Bài Báo 2: LLMxCPG - Phát Hiện Lỗ Hổng Nhận Thức Ngữ Cảnh Qua Đồ Thị Thuộc Tính Mã Nguồn (2025)](#3-bài-báo-2-llmxcpg---phát-hiện-lỗ-hổng-nhận-thức-ngữ-cảnh-qua-đồ-thị-thuộc-tính-mã-nguồn-2025)
   - 3.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu
   - 3.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?
   - 3.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)
   - 3.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)
   - 3.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 2, 3, 4, 5)
   - 3.6. Điểm Mạnh Của Nghiên Cứu
   - 3.7. Điểm Yếu & Khoảng Trống Nghiên Cứu
4. [Bài Báo 3: SecureVibeBench - Đánh Giá Lập Trình Vibe Coding An Toàn Của AI Agent (2025)](#4-bài-báo-3-securevibebench---đánh-giá-lập-trình-vibe-coding-an-toàn-của-ai-agent-2025)
   - 4.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu
   - 4.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?
   - 4.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)
   - 4.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)
   - 4.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 2 & Bảng 3)
   - 4.6. Điểm Mạnh Của Nghiên Cứu
   - 4.7. Điểm Yếu & Khoảng Trống Nghiên Cứu
5. [Bài Báo 4: Đánh Giá Hiệu Quả Và Chi Phí Của LLM Hiện Đại Với Ngữ Cảnh Liên Thủ Tục (ACM EASE 2026)](#5-bài-báo-4-đánh-giá-hiệu-quả-và-chi-phí-của-llm-hiện-đại-với-ngữ-cảnh-liên-thủ-tục-acm-ease-2026)
   - 5.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu
   - 5.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?
   - 5.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)
   - 5.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)
   - 5.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 5, Chi Phí, Rubric)
   - 5.6. Điểm Mạnh Của Nghiên Cứu
   - 5.7. Điểm Yếu & Khoảng Trống Nghiên Cứu
6. [Bài Báo 5: DREA - Tách Rời Suy Luận Và Khám Phá Cấp Repository Cho AI Agent (2026)](#6-bài-báo-5-drea---tách-rời-suy-luận-và-khám-phá-cấp-repository-cho-ai-agent-2026)
   - 6.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu
   - 6.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?
   - 6.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)
   - 6.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)
   - 6.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 1, Bảng 3, Bảng 4)
   - 6.6. Điểm Mạnh Của Nghiên Cứu
   - 6.7. Điểm Yếu & Khoảng Trống Nghiên Cứu
7. [Bảng Ma Trận So Sánh Tổng Hợp Đa Chiều Giữa 5 Công Trình](#7-bảng-ma-trận-so-sánh-tổng-hợp-đa-chiều-giữa-5-công-trình)
8. [Tổng Kết Bài Học Chiến Lược & Xu Hướng Nghiên Cứu Tương Lai](#8-tổng-kết-bài-học-chiến-lược--xu-hướng-nghiên-cứu-tương-lai)

---

## 1. GIỚI THIỆU TỔNG QUAN BỘ SƯU TẬP 5 BÀI BÁO KHOA HỌC

Bộ sưu tập bao gồm 5 công trình nghiên cứu khoa học xuất sắc nhất giai đoạn 2025–2026 trong lĩnh vực An toàn phần mềm hỗ trợ bởi Trí tuệ nhân tạo (AI-assisted Software Security). Trọng tâm xuyên suốt là giải quyết bài toán cốt lõi: **Làm thế nào để các mô hình ngôn ngữ lớn (LLM) và các AI Agent có thể phát hiện, phòng chống và lập trình an toàn trong các kho mã nguồn thực tế (Code Repositories), vượt ra khỏi phạm vi các hàm đơn lẻ (isolated functions) và kiểm soát ngữ cảnh liên thủ tục (interprocedural context) mà vẫn đảm bảo tính khả thi về mặt chi phí và độ tin cậy thực nghiệm.**

5 bài báo gồm:

1. **Bài 1 (`2025.acl-long.1490.pdf`):** _Benchmarking LLMs and LLM-based Agents in Practical Vulnerability Detection for Code Repositories_ (ACL 2025 Long Papers).
2. **Bài 2 (`2507.16585v1.pdf`):** _LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models_ (2025).
3. **Bài 3 (`2509.22097v5.pdf`):** _SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios_ (2025).
4. **Bài 4 (`2604.08417v1.pdf`):** _Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs_ (ACM EASE 2026).
5. **Bài 5 (`2607.13439v1.pdf`):** _DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection_ (2026).

---

## 2. BÀI BÁO 1: JITVUL - ĐÁNH GIÁ LLM VÀ REACT AGENT TRONG PHÁT HIỆN LỖ HỔNG JUST-IN-TIME (ACL 2025 LONG)

- **Tên nguyên bản tiếng Anh:** _Benchmarking LLMs and LLM-based Agents in Practical Vulnerability Detection for Code Repositories_
- **Tác giả:** Alperen Yildiz, Sin G. Teo, Yiling Lou, Yebo Feng, Chong Wang, Dinil Mon Divakaran.
- **Cơ quan:** National University of Singapore (NUS), Institute for Infocomm Research (I2R - A\*STAR), Fudan University, Nanyang Technological University (NTU).
- **Xuất bản tại:** _Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Volume 1: Long Papers)_, pages 30848–30865, Bangkok, Thailand.

### 2.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu

- **Cấu trúc nghiên cứu:** Thiết kế bài toán phát hiện lỗ hổng đúng thời điểm (**Just-in-Time - JIT Detection**) tại mốc commit thay đổi mã nguồn, tích hợp chặt chẽ cơ chế đánh giá theo cặp đối ứng (**Pairwise Evaluation**).
  - Cấu trúc thực nghiệm kiểm tra ma trận 3 phương pháp phát hiện $\times$ 4 chiến lược Prompting $\times$ 4 mô hình ngôn ngữ lớn (2 thương mại + 2 mã nguồn mở).
- **Mô hình AI nghiên cứu:**
  - **Thương mại:** `GPT-4o` (mô hình cờ đầu) và `GPT-4o-mini` (mô hình chi phí thấp), thiết lập nhiệt độ $Temperature = 0$.
  - **Mã nguồn mở:** `Llama-3.1-8B` (Meta) và `DeepSeek-Coder-V2-16B` (DeepSeek AI).
  - **Thư viện triển khai:** `Transformers v4.52.0` và `LangChain v0.3.14`.
- **3 Phương pháp nghiên cứu:**
  1. _Plain LLM:_ Nạp duy nhất mã nguồn của hàm mục tiêu cùng prompt chỉ dẫn.
  2. _Dep-Aug LLM (Dependency-Augmented):_ Mở rộng bằng cách tự động nối thêm Top-5 hàm gọi (callers) và hàm được gọi (callees) có độ tương đồng từ vựng Jaccard cao nhất vào prompt (tái hiện từ VulEval).
  3. _ReAct Agent:_ Tác nhân suy luận lặp theo cơ chế Thought-Action-Observation, trang bị các công cụ tra cứu cấu trúc kho mã nguồn.
- **4 Chiến lược Prompting:**
  1. _Vanilla:_ Prompt định dạng chuẩn cơ bản.
  2. _Chain-of-Thought (CoT):_ Bổ sung câu lệnh _"Solve this problem step by step..."_.
  3. _Few-Shot (FS):_ Cung cấp 10 cặp ví dụ mẫu (vulnerable vs patched benign) trích xuất từ tài liệu CWE Top 25 năm 2024.
  4. _CoT + FS:_ Kết hợp cả chuỗi tư duy từng bước và 10 cặp mẫu đối chứng.

### 2.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?

- **Sản phẩm tạo ra:** Bộ chuẩn đối sánh **JITVUL** gồm **879 CVEs** thực tế với **91 loại CWE** khác nhau trong các dự án phần mềm C/C++ mã nguồn mở.
- **Nền tảng kỹ thuật hoạt động:**
  - **Thuật toán SZZ (Lomio et al., 2022):** Dùng để truy vết ngược lịch sử commit Git nhằm xác định commit đưa vào lỗ hổng (**VIC - Vulnerability-Introducing Commit**, kho mã ký hiệu $R_{intro}$) và commit sửa chữa lỗ hổng (**VFC - Vulnerability-Fixing Commit**, kho mã ký hiệu $R_{fix}$).
  - **GNU CFlow (GNU, 2025):** Công cụ phân tích cú pháp tĩnh dùng để xây dựng đồ thị gọi hàm (Call Graph) theo nhu cầu (on-demand call graph construction).
  - **Universal CTags (2025):** Công cụ lập chỉ mục định nghĩa hàm, trích xuất chính xác thân mã nguồn (function body) từ file tương ứng trong kho mã nguồn.

### 2.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)

```
[Hàm ứng viên f trong Commit mới]
          │
          ▼
    [ReAct Agent]
          │
          ▼
┌───► [Bước 1: THOUGHT] ── Phân tích cú pháp, biến nhạy cảm, biên kiểm tra
│           │
│           ▼
│     [Bước 2: ACTION] ── Cần thêm ngữ cảnh liên hàm không?
│           ├─► CẦN: Gọi Tool API
│           │        ├─► get_callers(func_name)  ──> GNU CFlow
│           │        ├─► get_callees(func_name)  ──> GNU CFlow
│           │        └─► get_function_code(name) ──> Universal CTags
│           │        │
│           │        ▼
│           │   [Bước 3: OBSERVATION] ── Môi trường trả về mã nguồn hàm liên quan
│           │        │
│           └────────┘ (Cập nhật ngữ cảnh, quay lại Bước 1)
│
└─────► ĐÃ ĐỦ CHỨNG CỨ:
            │
            ▼
      [ACTION CUỐI CÙNG: Finish[VULNERABLE hoặc BENIGN]]
            │
            ▼
      [ĐÁNH GIÁ CẶP (pAcc)]:
      Chỉ tính là ĐÚNG nếu: JITDETECT(R_intro, f_vul) = vul  VÀ  JITDETECT(R_fix, f_ben) = ben
```

### 2.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)

- **Vấn đề cốt lõi của LLM thông thường:**
  > _"The LLM-based vulnerability detection methods often over-classify both vulnerable and benign instances as vulnerable, leading to pairwise accuracy that can fall below the level of random guessing, a well-documented issue. For example, GPT-4 achieves only 5.14% accuracy with two-shot prompting and 12.94% with chain-of-thought reasoning, compared to 22.70% for random guessing... larger models tend to perform worse than smaller ones, as they are more susceptible to over-predicting vulnerabilities."_ (Mục 5.1, Trang 30854).
- **Nguyên lý giúp ReAct Agent thành công:**
  > _"The thought-action-observation framework of ReAct Agents, combined with their effective use of interprocedural context, enhances their ability to capture vulnerability characteristics. ReAct Agents consistently outperform Plain LLMs and Dep-Aug LLMs in pAcc across all prompting strategies."_ (Mục 5.1, Trang 30854).
  - Khi Agent gặp một biến con trỏ hoặc bộ đệm không rõ kích thước, Agent chủ động gọi `get_callers` để kiểm tra nơi gọi hàm. Nếu caller đã có lệnh kiểm tra `if (len > MAX) return;`, Agent sẽ xác định hàm đã được bảo vệ an toàn và kết luận `Benign`. Nhờ đó, Agent không bị đánh lừa bởi mã trông nguy hiểm nhưng thực chất an toàn.

### 2.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 2 & Bảng 4 trong bài báo)

#### Bảng 2: Kết quả thực nghiệm của các phương pháp trên JITVUL (Đơn vị: %)

| Phương Pháp                 | GPT-4o-mini: F1 | GPT-4o-mini: pAcc | GPT-4o: F1 | GPT-4o: pAcc |
| :-------------------------- | :-------------: | :---------------: | :--------: | :----------: |
| **Plain LLM (vanilla)**     |      56.00      |       3.36        |   65.96    |     1.02     |
| **Plain LLM (w/ CoT)**      |      65.10      |       3.36        |   62.22    |    15.02     |
| **Plain LLM (w/ FS)**       |      48.74      |       7.56        |   62.77    |     4.44     |
| **Plain LLM (w/ CoT+FS)**   |      64.65      |       11.76       |   64.44    |    17.63     |
| **Dep-Aug LLM (vanilla)**   |      52.68      |       2.05        |   63.30    |     1.03     |
| **Dep-Aug LLM (w/ CoT)**    |    **66.05**    |       4.86        |   62.60    |    18.66     |
| **Dep-Aug LLM (w/ FS)**     |      48.23      |       7.27        |   62.03    |     2.39     |
| **Dep-Aug LLM (w/ CoT+FS)** |      65.01      |       4.68        |   61.12    |    18.79     |
| **ReAct Agent (vanilla)**   |      56.63      |       12.61       |   57.77    |    17.63     |
| **ReAct Agent (w/ CoT)**    |      56.93      |       16.81       |   58.07    |  **19.13**   |
| **ReAct Agent (w/ FS)**     |      56.81      |     **20.17**     |   56.42    |    18.91     |
| **ReAct Agent (w/ CoT+FS)** |      51.06      |       14.29       |   52.61    |    18.89     |

_Nhận xét số liệu Bảng 2:_ Ở cấu hình vanilla trên GPT-4o, Plain LLM chỉ đạt pAcc **1.02%**, trong khi ReAct Agent đạt **17.63%** (tăng vọt tuyệt đối **+16.61%**). ReAct Agent với Few-Shot trên GPT-4o-mini đạt pAcc cao nhất là **20.17%**.

#### Bảng 4: Kết quả với mô hình mã nguồn mở Llama-3.1-8B và DeepSeek-Coder-V2-16B

| Phương Pháp                 | Llama-3.1: F1 | Llama-3.1: pAcc | DeepSeek-Coder: F1 | DeepSeek-Coder: pAcc |
| :-------------------------- | :-----------: | :-------------: | :----------------: | :------------------: |
| **Plain LLM (vanilla)**     |     58.05     |      0.84       |       60.04        |        15.94         |
| **Plain LLM (w/ CoT)**      |     49.79     |      10.92      |       59.74        |        12.41         |
| **Plain LLM (w/ CoT+FS)**   |     29.55     |      14.29      |       50.46        |        10.93         |
| **Dep-Aug LLM (w/ CoT+FS)** |     16.46     |      7.42       |     **82.09**      |      **69.24**       |
| **ReAct Agent (vanilla)**   |     9.09      |      4.20       |       19.40        |         8.39         |
| **ReAct Agent (w/ CoT+FS)** |     3.28      |      1.68       |       31.97        |        21.39         |

_Bảng 3: Nhạy cảm của F1 trước phân bố nhãn:_ Khi thử trên tập PrimeVul không theo cặp (695 vul và 25,216 benign), F1 của GPT-4o-mini giảm từ ~65% xuống còn: vanilla: **9.20%**, w/ CoT: **5.41%**, w/ FS: **12.21%**, w/ CoT+FS: **5.86%**.

### 2.6. Điểm Mạnh Của Nghiên Cứu

- **Vạch trần "Ảo tưởng F1":** Chỉ ra rằng F1 score cao ở các bài báo cũ chỉ là ảo ảnh do mô hình thiên vị nhãn dương tính (Recall > 90% nhưng Precision chỉ ~50%).
- **Tính thực tế Just-in-Time:** Giải quyết bài toán mở rộng (scalability) trong thực tế: chỉ quét các hàm bị sửa đổi trong commit thay vì quét hàng triệu dòng code của cả repo.
- **Chứng minh giá trị của Agent:** ReAct Agent cải thiện vượt trội khả năng phân biệt cặp mã lỗi vs mã đã vá so với LLM thông thường.

### 2.7. Điểm Yếu & Khoảng Trống Nghiên Cứu

- **Điểm yếu:** ReAct Agent trên các mô hình mã nguồn mở nhỏ (8B) thất bại nặng nề do lỗi parse format, thường mặc định trả về nhãn `benign` (Bảng 4: pAcc chỉ đạt 0.84% - 4.20%).
- **Khoảng trống nghiên cứu:** Mới chỉ đánh giá trên C/C++, chưa mở rộng sang Java, Python, Go. Chưa tích hợp các công cụ phân tích luồng dữ liệu (Taint analysis) hay cắt lát mã vào bộ công cụ của Agent.

---

## 3. BÀI BÁO 2: LLMxCPG - PHÁT HIỆN LỖ HỔNG NHẬN THỨC NGỮ CẢNH QUA ĐỒ THỊ THUỘC TÍNH MÃ NGUỒN (2025)

- **Tên nguyên bản tiếng Anh:** _LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models_
- **Tác giả:** Ahmed Lekssays, Hamza Mouhcine, Khang Tran, Ting Yu, Issa Khalil.
- **Cơ quan:** Qatar Computing Research Institute (QCRI), New Jersey Institute of Technology (NJIT), Mohamed bin Zayed University of Artificial Intelligence (MBZUAI).
- **Xuất bản tại:** Công bố quốc tế năm 2025 (arXiv:2507.16585v1).

### 3.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu

- **Cấu trúc nghiên cứu:** Giải quyết hiện tượng sụt giảm độ chính xác và mất độ bền vững (poor robustness) khi áp dụng LLM trực tiếp trên mã nguồn thô. Nghiên cứu đề xuất kiến trúc mô hình kép kết hợp giữa Đồ thị Thuộc tính Mã nguồn (**Code Property Graph - CPG**) và kỹ thuật Cắt tỉa chương trình (**Program Slicing**).
- **Mô hình AI nghiên cứu:** Kiến trúc mô hình kép (**Dual-Model Architecture**):
  1. **LLMxCPG-Q (Query Generator):** Fine-tuned từ `Qwen2.5-Coder-32B-Instruct` chuyên trách sinh các câu truy vấn đồ thị CPGQL chuẩn cú pháp Joern.
  2. **LLMxCPG-D (Vulnerability Detector):** Fine-tuned từ mô hình suy luận `QwQ-32B-Preview` bằng kỹ thuật thích ứng thứ hạng thấp LoRA trên các lát cắt mã nguồn sạch.

### 3.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?

- **Sản phẩm tạo ra:** Khung phát hiện lỗ hổng tự động **LLMxCPG** hỗ trợ 4 ngôn ngữ (C, C++, Java, Python) có khả năng phân tích cả cấp hàm lẫn cấp toàn dự án (project-level).
- **Nền tảng kỹ thuật hoạt động:**
  - **Joern Static Analysis Engine:** Công cụ mã nguồn mở cấp công nghiệp dùng để biên dịch mã thành cấu trúc Đồ thị Thuộc tính Mã nguồn (CPG) tích hợp 3 đồ thị:
    - _AST (Abstract Syntax Tree):_ Cấu trúc phân cấp ngữ pháp.
    - _CFG (Control Flow Graph):_ Luồng điều khiển thực thi tuần tự và rẽ nhánh.
    - _PDG (Program Dependence Graph):_ Luồng phụ thuộc dữ liệu (def-use chains) và phụ thuộc điều khiển.
  - **Ngôn ngữ CPGQL:** Ngôn ngữ truy vấn đồ thị chuyên biệt trên nền Scala của Joern.

### 3.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)

```
[Mã nguồn thô / Repository]
       │
       ▼
[Joern CPG Engine] ── Biên dịch cú pháp ──> [Đồ thị CPG (AST + CFG + PDG)]
       │                                            │
       ▼                                            ▼
[LLMxCPG-Q (32B)] ── Phân tích điểm nghi vấn ──> [Sinh câu truy vấn CPGQL]
                                                    │
                                                    ▼
[Joern Graph Traverser] <───────────────────────────┘
       │
       ├─► Backward Slicing: Lần ngược Data Flow về điểm sinh dữ liệu (Source)
       ├─► Forward Slicing: Đi xuôi Control Flow đến điểm kích hoạt (Sink)
       ▼
[Lát cắt mã nguồn (Code Slice)] ── Rút gọn từ 67.84% đến 90.93% số dòng mã
       │
       ▼
[LLMxCPG-D (QwQ-32B)] ── Suy luận logic bảo mật trên lát cắt sạch
       │
       ▼
[Đầu ra: Nhãn {Vulnerable / Safe} + Chuỗi giải thích Reasoning]
```

### 3.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)

- **Vấn đề cốt lõi trên mã nguồn thô:**
  > _"Current vulnerability detection methods typically analyze code in its raw, unprocessed form... vulnerable code often contains only a small fraction of lines that are actually related to the vulnerability. As a result, detection models face two key challenges: i) including codes irrelevant to vulnerabilities increases token usage, ii) struggling to discern truly relevant vulnerability patterns, often leading to models relying on spurious features."_ (Mục 3.2).
- **Vì sao các LLM thông thường thất bại trong việc tạo câu truy vấn đồ thị:**
  Các mô hình nền tảng như DeepSeek-V3 hay Qwen gốc không nắm được cú pháp API của Joern CPGQL:
  > _"As shown in Table 2, LLMxCPG-Q effectively learns the syntax of CPGQL, whereas the base models... encounter difficulties... DeepSeek often misuses the .code API to filter nodes by their name... cpg.call.code('print') returns empty results because code matches the entire statement... The correct query is cpg.call.name('print')."_ (Mục 4.3.1).
- **Kết quả sinh truy vấn hợp lệ (Bảng 2 trong bài báo):**
  - **DeepSeek-v3:** Chỉ sinh được **132 / 1278** câu truy vấn hợp lệ (10.3%).
  - **Qwen2.5-Coder-32B-Instruct:** Chỉ sinh được **19 / 1278** câu truy vấn hợp lệ (1.5%).
  - **LLMxCPG-Q:** Đạt tỷ lệ tuyệt đối **1278 / 1278** câu truy vấn hợp lệ (**100%**).

### 3.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 3, Bảng 4, Bảng 5)

#### Bảng 3 & 4: Hiệu năng trên PrimeVul, FormAI & Phân rã theo CWE

- **Trên tập dữ liệu FormAI:** Accuracy = **0.8146**, Precision = **0.8097**, Recall = **0.8054**, F1-score = **0.8075**.
- **Trên tập dữ liệu PrimeVul (thẩm định khắt khe):** Accuracy = **0.7250**, Precision = **1.000**, Recall = **0.4500**, F1-score = **0.6206**.
- **Phân rã theo loại CWE (Bảng 4):**
  - **CWE-119 (Memory Buffer Errors):** Acc = **0.941**, Prec = **1.000**, Recall = **0.941**, F1 = **0.970**.
  - **CWE-415 (Double Free):** Acc = **0.757**, Prec = **0.891**, Recall = **0.817**, F1 = **0.852**.
  - **CWE-416 (Use After Free):** Acc = **0.778**, Prec = **1.000**, Recall = **0.736**, F1 = **0.848**.
  - **CWE-190 (Integer Overflow):** Acc = **0.672**, Prec = **0.844**, Recall = **0.745**, F1 = **0.792**.

#### Bảng 5: So sánh trên tập dữ liệu chuẩn SVEN

| Mô Hình               |  Accuracy  | Precision  |   Recall   |  F1-Score  |
| :-------------------- | :--------: | :--------: | :--------: | :--------: |
| VulSim [29]           |   0.3300   |   0.3100   |   0.3100   |   0.3100   |
| VulBERTA-CNN [14]     |   0.5000   |   0.5100   |   0.3800   |   0.4400   |
| VulBERTA-MLP [14]     |   0.5000   |   0.5000   |   0.3700   |   0.4300   |
| ReGVD [25]            |   0.5100   |   0.5300   |   0.4600   |   0.5500   |
| **LLMxCPG (Bài báo)** | **0.6020** | **0.5590** | **0.9534** | **0.7048** |

_Hiệu năng cấp Toàn bộ Dự án (ReposVul Project-level):_ Đạt Accuracy **0.634** khi phân tích toàn kho mã nguồn.

### 3.6. Điểm Mạnh Của Nghiên Cứu

- **Nén mã nguồn ngoạn mục:** Cắt giảm từ **67.84% đến 90.93%** số dòng mã mà không làm mất bất kỳ mắt xích ngữ cảnh an ninh nào.
- **Tăng vọt F1-Score:** Nâng F1 từ 15% đến 40% so với các phương pháp SOTA trước đây trên các benchmark thẩm định gắt gao.
- **Miễn nhiễm trước biến đổi mã (Robustness):** Không bị đánh lừa khi xóa chú thích hoặc đổi tên biến – điều mà các mô hình học sâu trước đây đều thất bại.
- **Khả năng khái quát hóa cao:** Hoạt động xuất sắc trên tập dữ liệu hoàn toàn mới sau điểm cắt tri thức (PKCO-25) trên 4 ngôn ngữ (C, C++, Java, Python).

### 3.7. Điểm Yếu & Khoảng Trống Nghiên Cứu

- **Điểm yếu:** Đồ thị CPG tĩnh không thể bắt được các lỗi tương tranh (Race Conditions) hoặc đa luồng tại thời điểm chạy. Đồng thời cần hạ tầng GPU lớn để chạy 2 mô hình 32B.
- **Khoảng trống nghiên cứu:** Chưa hỗ trợ tự động sinh bản vá sửa lỗi (automated repair). Cần kết hợp phân tích thực thi động (Symbolic Execution) để xử lý các lỗi runtime phức tạp.

---

## 4. BÀI BÁO 3: SECUREVIBEBENCH - ĐÁNH GIÁ LẬP TRÌNH VIBE CODING AN TOÀN CỦA AI AGENT (2025)

- **Tên nguyên bản tiếng Anh:** _SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios_
- **Tác giả:** Junkai Chen, Huihui Huang, Yunbo Lyu, Junwen An, Jieke Shi, Chengran Yang, Ting Zhang, Haoye Tian, Yikun Li, Zhenhao Li, Xin Zhou, Xing Hu, David Lo.
- **Cơ quan:** Singapore Management University (SMU), NUS, Monash, Aalto, York, Zhejiang University.
- **Xuất bản tại:** Công bố quốc tế năm 2025 (arXiv:2509.22097v5, 36 trang).

### 4.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu

- **Cấu trúc nghiên cứu:** Đánh giá an toàn thông tin trong trào lưu "Vibe Coding" – nơi lập trình viên đưa ý tưởng cấp cao bằng ngôn ngữ tự nhiên, còn AI Agent tự động duyệt repo và sửa đổi hàng loạt file. Nghiên cứu khảo sát xem liệu mã do Agent sinh ra có đưa lỗ hổng an toàn bộ nhớ vào dự án hay không.
- **3 Khung Agent Scaffolds được đánh giá:**
  1. `SWE-agent (SWE)` (Yang et al., 2024a).
  2. `OpenHands (OH)` (Wang et al., 2024).
  3. `Aider (AD)` (Aider, 2025).
- **5 Mô hình nền tảng (Backbone LLMs):**
  1. `Claude Sonnet 4.5 (C4.5)` (Anthropic).
  2. `GPT-5 (G5)` (OpenAI).
  3. `Claude 3.7 Sonnet (C3.7)` (Anthropic).
  4. `GPT-4.1 (G4.1)` (OpenAI).
  5. `DeepSeek-V3.1 (DS)` (DeepSeek AI).

### 4.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?

- **Sản phẩm tạo ra:** Benchmark **SecureVibeBench** gồm **105 bài toán lập trình an toàn bộ nhớ C/C++ cấp repository** trích xuất từ 41 dự án mã nguồn mở lớn trong **OSS-Fuzz** và **ARVO** (bao gồm OpenSSL, libcurl, harfbuzz, mruby).
- **Cơ chế thẩm định kép (Dual-Oracle Foundation):**
  - **Dynamic Testing:** Dùng kịch bản khai thác **PoV (Proof of Vulnerability)** chạy kèm trình giám sát bộ nhớ **AddressSanitizer (ASan) / MemorySanitizer (MSan)** để bắt lỗi tràn bộ nhớ tại thời điểm thực thi.
  - **Static Testing:** Dùng công cụ phân tích tĩnh **Semgrep SAST** để quét các rủi ro bảo mật mới phát sinh.
  - **Differential Testing:** Đối chiếu với test suite gốc của dự án để kiểm tra tính đúng đắn chức năng.

### 4.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)

```
[4,993 Lỗ hổng OSS-Fuzz & ARVO]
       │
       ▼
[Thuật toán SZZ + Rà soát thủ công] ── Xác định cặp commit:
       ├─► VIC (Commit đưa lỗi vào)
       └─► PVIC (Commit cha liền trước - sạch lỗi)
       │
       ▼
[Kiểm định chất lượng PoV]: PoV PHẢI chạy FAIL ở PVIC và PHẢI EXPLOIT thành công ở VIC
       │
       ▼
[105 Tác vụ chuẩn mực SecureVibeBench (Dockerized)]
       │
       ▼
[AI Agent nhận Repo ở PVIC + Yêu cầu ngôn ngữ tự nhiên]
       │
       ▼
[Agent tự do: Duyệt file, Sửa multi-file, Biên dịch gcc/clang, Chạy Unit Test]
       │
       ▼
[Bản vá Git Patch do Agent sinh ra]
       │
       ├─────────────────────────────────┬─────────────────────────────────┐
       ▼                                 ▼                                 ▼
[Test Suite Dự án]              [Chạy PoV + ASan]                 [Quét Semgrep SAST]
       │                                 │                                 │
  Vượt qua test?                  Bị crash/segfault?               Có rủi ro an ninh mới?
  ├─ Sai: INCORRECT               ├─ Có: VULNERABLE                ├─ Có: SUSPICIOUS
  └─ Đúng: CORRECT                └─ Không: NON-VUL                └─ Không: SECURE
       │                                 │                                 │
       └─────────────────────────────────┴─────────────────────────────────┘
                                         │
                                         ▼
                 [TIÊU CHUẨN CỐT LÕI: C-SEC (Correct-and-Secure)]
           Bản vá ĐẠT C-SEC  <=>  CORRECT  +  NON-VUL  +  SECURE
```

### 4.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)

- **Vấn đề cốt lõi của Vibe Coding an toàn:**
  > _"Large language model-powered code agents are rapidly transforming software engineering, yet the security risks of their generated code have become a critical concern. Existing benchmarks... fail to capture scenarios in which vulnerabilities are actually introduced by human developers, making fair comparisons between humans and agents infeasible."_ (Abstract).
- **Kết quả đáng báo động về tỷ lệ an toàn của AI Agent:**
  > _"Overall, all agents perform poorly in generating secure code... SWE shows the best average performance (14.3% C-SEC rate), while OH achieves comparable results (13.9%)... C4.5 shows a clear performance lead over others (17.1% vs ≤14.3%). DS and G5 form the second tier (~14%)... while G4.1 and C3.7 show overall weaker performance."_ (Mục 4.1).

### 4.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 2 & Bảng 3)

#### Bảng 2: Quy mô và độ phức tạp của SecureVibeBench

| Thuộc Tính Đo Lường                           | Trung Bình (Average) | Tối Đa (Maximum)  |
| :-------------------------------------------- | :------------------: | :---------------: |
| **Độ dài yêu cầu tính năng (# of Words)**     |       200.1 từ       |      408 từ       |
| **Quy mô Repository (# of Files)**            |  **2,845.3 files**   | **36,388 files**  |
| **Số dòng mã dự án (# of LOC)**               |  **554,718.8 LOC**   | **4,248,069 LOC** |
| **Bản vá mẫu (# of Files sửa đổi)**           |      1.9 files       |      5 files      |
| **Số dòng mã bản vá (# of LOC sửa đổi)**      |       42.5 LOC       |      148 LOC      |
| **Số lượng test case chức năng (# of Cases)** |     434.3 tests      |    5,420 tests    |

#### Bảng 3: Tỷ lệ mã vừa đúng vừa an toàn (C-SEC Rate %)

| Scaffolds / LLMs   | SWE-agent | OpenHands | Aider (AD) |   C4.5    | DeepSeek | GPT-5 | C3.7 | GPT-4.1 | **Trung Bình** |
| :----------------- | :-------: | :-------: | :--------: | :-------: | :------: | :---: | :--: | :-----: | :------------: |
| **C-SEC Rate (%)** | **14.3%** |   13.9%   |    6.7%    | **17.1%** |  14.3%   | 13.3% | 7.3% |  6.0%   |   **11.62%**   |

- **Chi phí và Thời gian:** Chi phí trung bình = **$0.85 / task** (SWE-C4.5 và OH-C4.5 tốn từ **$2.5 đến $3.0** mỗi task). Thời gian thực thi trung bình = **520.90 giây**.
- **Phân bố lỗi an ninh trong mã của Agent:** CWE-120 (Buffer Copy without Checking: **33%**), CWE-457 (Uninitialized Variable: **27%**), CWE-476 (NULL Pointer Dereference: **27%**), CWE-125 (Out-of-bounds Read: **18%**), CWE-416 (Use After Free: **11%**), CWE-122 (Heap Buffer Overflow: **10%**).
- **Chế độ hỏng hóc chức năng (Functional Failure Modes):** Test Failure (TF) = **~40%**, Compilation Error (CE) = **~40%**, No Output (NO) = **~15%**.

### 4.6. Điểm Mạnh Của Nghiên Cứu

- **Tính chân thực tuyệt đối:** Không dùng mã giả định; hoàn toàn dựa trên các sự cố an ninh có thật trong các thư viện nền tảng thế giới thực (OpenSSL, curl, libxml2, harfbuzz).
- **Cảnh báo thực trạng an toàn đáng báo động:** Tỷ lệ mã vừa hoàn thành chức năng vừa an toàn (**C-SEC**) của AI Agent hiện nay trung bình chỉ đạt **11.6%**. Agent viết mã chạy được test nhưng tiềm ẩn vô số lỗi tràn bộ đệm, rò rỉ bộ nhớ nghiêm trọng.
- **Phân tích chi phí - hiệu năng toàn diện:** Claude 4.5 dẫn đầu về độ an toàn (17.1% C-SEC) nhưng đắt đỏ ($2-$3/task); DeepSeek đạt tỷ lệ hiệu năng/giá thành tối ưu nhất (~14.3% C-SEC với chi phí cực thấp).

### 4.7. Điểm Yếu & Khoảng Trống Nghiên Cứu

- **Điểm yếu:** Quy mô mẫu dừng lại ở 105 bài toán do quy trình thẩm định thủ công rất tốn sức. Đồng thời chỉ tập trung vào lỗi bộ nhớ C/C++.
- **Khoảng trống nghiên cứu:** Cần cơ chế tự động fuzzing / kiểm tra bảo mật nội tại (Self-Security Verification) trong chính vòng lặp của Agent trước khi bàn giao mã. Mở rộng tự động hóa sang Python, Java và Rust.

---

## 5. BÀI BÁO 4: ĐÁNH GIÁ HIỆU QUẢ VÀ CHI PHÍ CỦA LLM HIỆN ĐẠI VỚI NGỮ CẢNH LIÊN THỦ TỤC (ACM EASE 2026)

- **Tên nguyên bản tiếng Anh:** _Vulnerability Detection with Interprocedural Context in Multiple Languages: Assessing Effectiveness and Cost of Modern LLMs_
- **Tác giả:** Kevin Lira, Baldoino Fonseca, Davy Baía, Márcio Ribeiro, Wesley K. G. Assunção.
- **Cơ quan:** North Carolina State University (Hoa Kỳ), Federal University of Alagoas (Brazil).
- **Xuất bản tại:** _Proceedings of the International Conference on Evaluation and Assessment in Software Engineering (ACM EASE 2026)_, Glasgow, Scotland, 10–13/6/2026.

### 5.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu

- **Cấu trúc nghiên cứu:** Nghiên cứu thực nghiệm có đối chứng đo lường tác động của việc bổ sung ngữ cảnh liên thủ tục (Callers / Callees) đối với độ chính xác, chi phí tài chính ($ USD) và chất lượng giải thích.
- **4 LLM thương mại hiện đại (Cost-effective Models):**
  1. `Claude Haiku 4.5` (Anthropic).
  2. `Gemini 3 Flash` (Google).
  3. `GPT-5 Mini` (OpenAI).
  4. `GPT-4.1 Mini` (OpenAI).
- **3 Cấu hình ngữ cảnh (Context Variations):**
  - `CO (Code-Only):` Chỉ nạp mã nguồn hàm mục tiêu.
  - `CC (Function + Callers):` Hàm mục tiêu + mã nguồn toàn bộ các hàm gọi nó.
  - `CK (Function + Callees):` Hàm mục tiêu + mã nguồn toàn bộ các hàm mà nó gọi.
- **3 Ngôn ngữ:** C, C++, Python (trích xuất từ ReposVul gồm 509 CVEs, 236 CWEs).

### 5.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?

- **Nền tảng kỹ thuật hoạt động:**
  - **Trích xuất Đồ thị Gọi hàm Call Graph tĩnh:** Để định danh danh sách các hàm gọi trực tiếp (Callers) và hàm được gọi (Callees).
  - **Kiểm định McNemar:** Đo lường ý nghĩa thống kê về sự biến động hiệu năng giữa các cấu hình ngữ cảnh.
  - **Thang Rubric đánh giá giải thích (0 - 2 điểm):** Đánh giá thủ công tính chính xác (Correctness) và tính toàn diện (Comprehensiveness).

### 5.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)

```
[509 Lỗ hổng CVE từ ReposVul (C, C++, Python)]
       │
       ▼
[Trích xuất Đồ thị Gọi hàm Call Graph tĩnh] ──> Xác định Callers & Callees
       │
       ├───────────────────────┬───────────────────────┐
       ▼                       ▼                       ▼
  [Cấu hình CO]           [Cấu hình CC]           [Cấu hình CK]
  Chỉ hàm mục tiêu        Hàm + Toàn bộ Callers   Hàm + Toàn bộ Callees
  (~2,367 tokens)         (~4,785 tokens: +102%)  (~4,586 tokens: +94%)
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               │
                               ▼
               [Prompt chuẩn hóa: Yêu cầu EXPLANATION trước, CLASSIFICATION sau]
                               │
                               ▼
               [Gửi đến 4 LLMs qua API chính thức]
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
[Kết quả Phân loại & Token API]             [Đánh giá Lời giải thích (Rubric 0-2)]
  ├─ Accuracy, F1-Score                       ├─ Correctness (Đúng loại, vị trí, nguyên nhân)
  ├─ Kiểm định McNemar Test                   └─ Comprehensiveness (Cơ chế khai thác)
  └─ Tính toán chi phí thực tế ($ USD)
```

### 5.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)

- **Nghịch lý phản trực giác chấn động (The Context Paradox):**
  > _"The results in Table 5 show a clear and consistent pattern across all models: the CO configuration achieves the best overall performance, both in terms of accuracy and F1-score... For GPT-4.1 Mini, accuracy drops from 75.6% to 51.0% with CC... For GPT-5 Mini in C, with CK context, accuracy decreased from 90.52% to 79.46%."_ (Mục 4.1 & 5.1).
- **Bản chất kỹ thuật giải thích nguyên nhân:**
  > _"One hypothesis for this behavior is that GPT-family models, when supplied with additional context, expand their attention window to elements that are not directly relevant to the vulnerability... introducing noise that degrades model performance. In contrast, models such as Claude Haiku 4.5 and Gemini 3 Flash appear more selective in incorporating additional context."_ (Mục 5.1).

### 5.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 5, Chi Phí, Rubric)

#### Bảng 5: Độ chính xác và F1-Score theo Model và Ngữ cảnh (Tổng hợp đa ngôn ngữ)

| Mô Hình              | Cấu Hình Ngữ Cảnh | Số Lượng Mẫu ($N$) | True Positives ($TP$) |  Accuracy  |  F1-Score  |
| :------------------- | :---------------: | :----------------: | :-------------------: | :--------: | :--------: |
| **Claude Haiku 4.5** |      **CO**       |        451         |          440          |   0.9756   |   0.9877   |
|                      |      **CC**       |        237         |          232          | **0.9789** | **0.9893** |
|                      |      **CK**       |        221         |          216          |   0.9774   |   0.9886   |
| **Gemini 3 Flash**   |      **CO**       |        408         |          402          | **0.9853** | **0.9926** |
|                      |      **CC**       |        170         |          162          |   0.9529   |   0.9759   |
|                      |      **CK**       |        149         |          143          |   0.9597   |   0.9795   |
| **GPT-5 Mini**       |      **CO**       |        442         |          401          | **0.9072** | **0.9514** |
|                      |      **CC**       |        230         |          192          |   0.8348   |   0.9100   |
|                      |      **CK**       |        217         |          168          |   0.7742   |   0.8727   |
| **GPT-4.1 Mini**     |      **CO**       |        451         |          341          | **0.7561** | **0.8611** |
|                      |      **CC**       |        237         |          128          |   0.5401   |   0.7014   |
|                      |      **CK**       |        221         |          153          |   0.6923   |   0.8182   |

#### Bảng Chi Phí & Chất Lượng Giải Thích:

- **Chi phí tài chính API toàn bộ thử nghiệm:**
  - `GPT-4.1 Mini`: **$0.87**
  - `GPT-5 Mini`: **$3.04**
  - `Gemini 3 Flash`: **$3.76** (Đạt F1 > 0.952 trên mọi cấu hình, tỷ lệ cost-effectiveness tối ưu nhất).
  - `Claude Haiku 4.5`: **$7.23** (Đắt gấp 8.3 lần GPT-4.1 Mini).
- **Đánh giá Rubric chất lượng giải thích (Thang 0 - 2 điểm):**
  - `Claude Haiku 4.5`: Dẫn đầu tuyệt đối với **Correctness = 1.942 / 2.0**, **Comprehensiveness = 1.902 / 2.0**, giải thích chính xác nguyên nhân gốc rễ trong **93.6%** các trường hợp.

### 5.6. Điểm Mạnh Của Nghiên Cứu

- Bác bỏ quan niệm sai lầm về việc "nhồi nhét ngữ cảnh" liên hàm nguyên khối; chứng minh sự bất đối xứng kinh tế (tốn gấp đôi token nhưng độ chính xác giảm hơn 21%).
- Chỉ ra Gemini 3 Flash là mô hình có tỷ lệ hiệu năng/giá thành tối ưu nhất, và Claude Haiku 4.5 giải thích sâu nhất.

### 5.7. Điểm Yếu & Khoảng Trống Nghiên Cứu

- **Điểm yếu:** Ngữ cảnh callers/callees chèn thô sơ, chưa dùng kỹ thuật cắt tỉa (slicing) thông minh. Nguy cơ ô nhiễm dữ liệu tiền huấn luyện (data contamination) từ ReposVul.
- **Khoảng trống nghiên cứu:** Cần cơ chế nén ngữ cảnh có chọn lọc. Cần đánh giá trên các hệ thống mã nguồn đóng (Proprietary Codebases) chưa từng xuất hiện trên mạng.

---

## 6. BÀI BÁO 5: DREA - TÁCH RỜI SUY LUẬN VÀ KHÁM PHÁ CẤP REPOSITORY CHO AI AGENT (2026)

- **Tên nguyên bản tiếng Anh:** _DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection_
- **Tác giả:** Mingyang Sun, Guozhu Meng.
- **Cơ quan:** Institute of Information Engineering, Chinese Academy of Sciences (IIE - CAS), University of Chinese Academy of Sciences (UCAS), Beijing, China.
- **Xuất bản tại:** Công bố quốc tế năm 2026 (arXiv:2607.13439v1).

### 6.1. Cấu Trúc Nghiên Cứu & Mô Hình AI Nghiên Cứu

- **Cấu trúc nghiên cứu:** Phát hiện lỗ hổng cấp toàn bộ kho mã nguồn (**Repository-Level**) bằng kiến trúc tách rời giữa tác nhân suy luận và tác nhân thám hiểm theo định hướng giả thuyết (**Hypothesis-Driven Decoupled Architecture**).
- **Cấu hình Tác nhân (Dual-Agent Setup):**
  1. **Planner Agent:** Chạy trên các mô hình thương mại cao cấp: `DeepSeek-V3.2`, `GLM-4.7`, `GPT-5.2`.
  2. **Explorer Agent:** Chạy trên mô hình nguồn mở cục bộ nhẹ: `GLM-4.7-Flash` (triển khai on-premise miễn phí chi phí token).
- **Bộ chuẩn đối sánh RepoPairBench:** 100 cặp bài toán vulnerability-fix Python sạch (2021–2025), kèm nhãn CVE, CWE, commit diff và commit message gốc.

### 6.2. Sản Phẩm Hoạt Động Như Thế Nào & Hoạt Động Dựa Trên Nền Tảng Gì?

- **Nền tảng kỹ thuật hoạt động:**
  - **Cơ chế phân tách trách nhiệm (Decoupled Division of Labor):** Đẩy hơn **93% lượng token đọc duyệt tốn kém** sang cho mô hình cục bộ nhẹ (chạy miễn phí tại chỗ), chỉ giữ lại các đoạn bằng chứng chắt lọc gửi cho mô hình cao cấp.
  - **4 Công cụ điều hướng chỉ đọc:** `ls` (liệt kê file), `glob` (tìm file theo pattern), `grep` (tìm chuỗi/regex trong mã nguồn), `read_file` (đọc nội dung file cụ thể).
  - **LLM Judge tự động:** Để thẩm định tính đúng đắn của chuỗi lập luận (Reasoning Correctness).

### 6.3. Quy Trình Hoạt Động Chi Tiết (Step-by-Step Workflow)

```
[Mã hàm mục tiêu x + Bản chụp Repository Snapshot]
       │
       ▼
[PLANNER AGENT (LLM Cao Cấp - DeepSeek-V3.2 / GPT-5.2)]
       │
       ├─► Phân tích thao tác nhạy cảm
       └─► Hình thành giả thuyết an ninh ban đầu H_0
       │
       ▼
┌─► [Ủy thác truy vấn tìm kiếm sang Explorer]
│   (Ví dụ: "Tìm file định nghĩa sanitize_url và kiểm tra logic regex")
│      │
│      ▼
│   [EXPLORER AGENT (Mô hình cục bộ nhẹ: GLM-4.7-Flash)]
│      │
│      ├─► Chạy 4 công cụ dòng lệnh chỉ đọc:
│      │     • ls       ── Liệt kê file
│      │     • glob     ── Tìm file theo pattern
│      │     • grep     ── Tìm chuỗi/regex trong mã nguồn
│      │     • read_file── Đọc nội dung file cụ thể
│      │
│      ▼
│   [Báo cáo cấu trúc 3 phần gửi ngược về Planner]:
│     1. Repository Context: Vị trí file trong dự án
│     2. Code Evidence: Trích đoạn mã thực tế liên quan (vài dòng)
│     3. Security Findings: Phát hiện sơ bộ về kiểm tra an toàn
│      │
│      ▼
│   [PLANNER AGENT tiếp nhận báo cáo]
│      │
│      ├─► Giả thuyết đã khép kín chứng cứ chưa?
│      │     ├─► CHƯA: Cập nhật giả thuyết H_{i+1}, quay lại vòng lặp (~10 rounds)
│      │     └─► ĐÃ ĐỦ: Dừng vòng lặp (Terminate)
│      ▼
└─► [PHÁN QUYẾT CUỐI CÙNG: Nhãn {Vulnerable / Benign} + Báo cáo Rationale]
       │
       ▼
[THẨM ĐỊNH LẬP LUẬN BẰNG LLM JUDGE]
       │
       ├─ So khớp Rationale của Planner với Commit Message & CVE gốc
       ▼
[Phân loại kết quả True Positives]:
  ├─ TRUE UNDERSTANDING: Đoán đúng nhãn VÀ hiểu đúng cơ chế lỗ hổng
  └─ LUCKY HIT: Đoán đúng nhãn nhưng lập luận sai / ngụy biện
```

### 6.4. Vì Sao Nó Hoạt Động & Trích Dẫn Nguyên Văn (Quotes)

- **Vấn đề cốt lõi của Monolithic Agent (Tác nhân đơn khối):**
  > _"Because repository-level analysis requires extensive code navigation... the resulting token volume would be prohibitively expensive if routed entirely through a high-cost API model. DREA therefore decouples the workflow into two collaborating agents, shifting the token-heavy exploration cost from the expensive reasoning model to a lightweight locally deployed model."_ (Mục 3.1).
- **Kết quả cắt giảm token ngoạn mục:**
  > _"Across all three models, the Planner accounts for only 2.1–6.3% of total token consumption, while the Explorer handles the remaining 93.7–97.9% locally... reducing API costs by 76–88%."_ (Mục 5.2 & Abstract).
- **Phát hiện về "Lucky Hits" (Ăn may trong phân loại):**
  Nghiên cứu chỉ ra rằng ở các phương pháp cấp hàm cũ, có tới 30-50% số mẫu đoán đúng nhãn thực chất là "Lucky Hits" (hiểu sai hoàn toàn cơ chế lỗi). DREA giúp mô hình đạt tỷ lệ **True Understanding** cao vượt bậc nhờ thu thập đúng bằng chứng ngữ cảnh.

### 6.5. Bảng Số Liệu Thực Nghiệm Tuyệt Đối Chính Xác (Bảng 1, Bảng 3, Bảng 4)

#### Bảng 1: Hiệu năng phát hiện của DREA so với Function-Only Baseline trên RepoPairBench

| Mô Hình Backbone  | Phương Pháp        | Recall (%) | FPR (%) | $F_1$ (%) | Pair-Correctness: P-C (%) | Youden's $J$ (pp) |
| :---------------- | :----------------- | :--------: | :-----: | :-------: | :-----------------------: | :---------------: |
| **DeepSeek-V3.2** | **DREA (Bài báo)** | **80.0%**  |  45.0%  | **71.1%** |         **42.0%**         |     **35.0**      |
|                   | Function-Only      |   39.0%    |  32.0%  |   45.6%   |           19.0%           |        7.0        |
| **GLM-4.7**       | **DREA (Bài báo)** | **59.0%**  |  38.0%  | **59.9%** |         **34.0%**         |     **21.0**      |
|                   | Function-Only      |   54.0%    |  43.0%  |   54.8%   |           26.0%           |       11.0        |
| **GPT-5.2**       | **DREA (Bài báo)** | **53.0%**  |  28.0%  | **58.6%** |         **30.0%**         |     **25.0**      |
|                   | Function-Only      |   42.0%    |  25.0%  |   50.3%   |           21.0%           |       17.0        |

_Ghi chú:_ P-C (Pair-Correctness) tăng từ **19–26% lên 30–42%** trên cả 3 mô hình backbone.

#### Bảng 3: Nghiên cứu triệt tiêu thành phần (Ablation Study trên DeepSeek-V3.2)

| Phương Pháp Cấu Hình          | Recall (%) | FPR (%) | $F_1$ (%) |  P-C (%)  | API Tokens qua mạng trả phí  |
| :---------------------------- | :--------: | :-----: | :-------: | :-------: | :--------------------------: |
| **DREA (Decoupled)**          | **80.0%**  |  45.0%  | **71.1%** | **42.0%** |        **88K tokens**        |
| **Single-Agent (Monolithic)** |   73.0%    |  64.0%  |   61.6%   |   24.0%   | **442K tokens** (gấp 5 lần!) |
| **Whole-File Baseline**       |   57.0%    |  41.0%  |   57.6%   |   26.0%   |          20K tokens          |
| **Function-Only Baseline**    |   39.0%    |  32.0%  |   45.6%   |   19.0%   |          2K tokens           |

_Nhận xét số liệu Bảng 3:_ Single-Agent (dùng 1 mô hình đắt tiền tự duyệt file) tiêu tốn **442,000 token API**, nhưng P-C chỉ đạt **24.0%** (kém xa DREA 42.0%) do hiện tượng thối rữa ngữ cảnh (Context Rot).

_Độ tin cậy của LLM Judge:_ Đối chiếu với chuyên gia con người qua hệ số Cohen’s $\kappa = \mathbf{0.88 - 0.92}$ (mức tương đồng gần như hoàn hảo).

### 6.6. Điểm Mạnh Của Nghiên Cứu

- **Tiết kiệm chi phí ngoạn mục:** Cắt giảm **76% đến 88% chi phí API** nhờ offload hơn 93% token cho mô hình cục bộ.
- **Tăng vọt Pair-Correctness:** Cải thiện tỷ lệ P-C từ 19-26% lên **30-42%**.
- **Phân biệt rạch ròi bản chất lập luận:** Tách biệt True Understanding khỏi Lucky Hits bằng LLM Judge đã được hiệu chuẩn.

### 6.7. Điểm Yếu & Khoảng Trống Nghiên Cứu

- **Điểm yếu:** Chỉ mới thực nghiệm trên hệ sinh thái Python. Explorer cục bộ dung lượng nhỏ đôi khi phát sinh cú pháp regex sai.
- **Khoảng trống nghiên cứu:** Mở rộng DREA sang C/C++ và Java nơi có hệ thống build phức tạp. Tự động sinh mã khai thác (PoV Script) từ giả thuyết an ninh của Planner.

---

## 7. BẢNG MA TRẬN SO SÁNH TỔNG HỢP ĐA CHIỀU GIỮA 5 CÔNG TRÌNH

| Tiêu Chí So Sánh                  | 1. JITVUL (ACL 2025)                                          | 2. LLMxCPG (2025)                                                  | 3. SecureVibeBench (2025)                                            | 4. Interprocedural LLMs (EASE 2026)                                            | 5. DREA (2026)                                                                            |
| :-------------------------------- | :------------------------------------------------------------ | :----------------------------------------------------------------- | :------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **Vấn đề kỹ thuật cốt lõi**       | Over-prediction bias ở LLM; cần ngữ cảnh liên hàm on-demand   | Nhiễu cú pháp và đặc trưng giả trên mã thô                         | Mã Vibe Coding chạy qua unit test nhưng dính lỗi bộ nhớ              | Nghịch lý nhồi callers/callees gây loãng attention                             | Phân tích repo tốn kém hàng triệu token; Context Rot                                      |
| **Mô hình AI nghiên cứu**         | GPT-4o, GPT-4o-mini, Llama-3.1, DeepSeek-Coder                | `LLMxCPG-Q` (32B) + `LLMxCPG-D` (QwQ-32B)                          | SWE, OpenHands, Aider + Claude 4.5, DeepSeek, GPT-5                  | Claude Haiku 4.5, Gemini 3 Flash, GPT-5/4.1 Mini                               | Planner (DeepSeek-V3.2, GPT-5.2) + Explorer (GLM-4-Flash)                                 |
| **Sản phẩm / Nền tảng hoạt động** | Benchmark JITVUL (879 CVEs); GNU CFlow + CTags + ReAct        | Framework LLMxCPG; Joern CPG Engine (AST+CFG+PDG)                  | Benchmark SecureVibeBench (105 tasks, 41 repos); Docker + PoV + ASan | Ma trận 4x3x3 trên 509 CVE ReposVul; McNemar test + Rubric                     | Khung DREA + RepoPairBench (100 pairs); LLM Judge ($\kappa=0.92$)                         |
| **Workflow cơ bản**               | Commit $ o$ ReAct loop (Thought-Action-Observation) $ o$ pAcc | Code thô $ o$ CPG $ o$ CPGQL Query $ o$ Slice (-80%) $ o$ Vul/Safe | PVIC $ o$ Agent sinh patch $ o$ Test Suite + PoV ASan $ o$ C-SEC     | Call Graph $ o$ Cấu hình CO/CC/CK $ o$ LLM $ o$ Cost + Rubric                  | Hàm mục tiêu $ o$ Planner định hướng $\leftrightarrow$ Explorer duyệt CLI $ o$ Phán quyết |
| **Số liệu đột phá then chốt**     | ReAct tăng pAcc từ 1.02% lên **17.63%** (+16.61% trên GPT-4o) | Giảm **67-91%** code; F1 đạt **0.7048** trên SVEN (SOTA cũ 0.55)   | C-SEC trung bình chỉ **11.62%**; Claude 4.5 đạt 17.1%                | Code-Only (CO) chính xác hơn CC tới **21-25%**; Gemini 3 Flash rẻ nhất ($3.76) | Offload **>93% token** cho local model; P-C tăng lên **42.0%** (baseline 19.0%)           |
| **Hạn chế lớn nhất**              | ReAct tốn nhiều bước lặp; mô hình 8B bị lỗi format            | CPG tĩnh không bắt được Race Conditions; tốn 2 GPU 32B             | Mới có 105 bài toán; tập trung chủ yếu vào bộ nhớ C/C++              | Chèn caller/callee nguyên khối thô; nguy cơ nhiễm dữ liệu                      | Chỉ áp dụng trên Python; Explorer nhỏ đôi khi gọi sai tool                                |

---

## 8. TỔNG KẾT BÀI HỌC CHIẾN LƯỢC & XU HƯỚNG NGHIÊN CỨU TƯƠNG LAI

Từ việc đối chiếu và phân tích 5 công trình nghiên cứu khoa học xuất sắc trên, chúng ta có thể đúc kết **5 bài học then chốt** định hình tương lai của An ninh phần mềm trong kỷ nguyên AI:

1. **Từ bỏ tư duy cấp hàm đơn lẻ (Death of Function-Level Isolation):**
   Cả 5 nghiên cứu đều khẳng định việc chỉ nhìn vào một hàm độc lập là không đủ để bảo vệ các hệ thống phần mềm hiện đại. Hơn 24% đến 40% lỗ hổng thực tế có nguồn gốc liên thủ tục, trải rộng qua nhiều hàm, nhiều lớp trừu tượng và nhiều tệp tin.

2. **Loại bỏ "Ảo tưởng F1" bằng Đánh giá theo Cặp (Pairwise Evaluation):**
   Các bài báo 1, 3 và 5 đã vạch trần một sự thật phũ phàng: LLM rất dễ đoán mò nhãn `Vulnerable` để đạt Recall cao ngất ngưởng. Đánh giá bảo mật bắt buộc phải sử dụng **Đánh giá theo cặp (Pairwise Evaluation / RepoPairBench)** và **Đánh giá tính đúng đắn của lập luận (Reasoning Correctness)** để phân biệt giữa năng lực phân tích thực thụ và những "cú đoán trúng ngẫu nhiên" (Lucky Hits).

3. **Nghịch lý Ngữ cảnh: Thừa mứa thông tin là thuốc độc (The Context Paradox):**
   Bài báo 4 và Bài báo 2 đã chứng minh rằng việc nhồi nhét ngữ cảnh một cách mù quáng (nhồi toàn bộ callers/callees nguyên khối) chỉ làm tăng chi phí và làm "ô nhiễm" khả năng tập trung của mô hình, khiến độ chính xác giảm tới 25%. Ngữ cảnh chỉ phát huy sức mạnh tối đa khi được **Cắt tỉa có định hướng (CPG Slicing như Bài 2)** hoặc **Truy vấn chủ động theo giả thuyết (Hypothesis-Driven Exploration như Bài 1 & Bài 5)**.

4. **Sự trỗi dậy của Kiến trúc Tác nhân Phân tầng (Decoupled Multi-Agent Architecture):**
   Mô hình nguyên khối (Monolithic Agent) đang dần trở nên lỗi thời do chi phí API khổng lồ và hiện tượng phân tâm ngữ cảnh. Thiết kế của **DREA (Bài 5)** và **LLMxCPG (Bài 2)** đại diện cho xu hướng tất yếu: kết hợp giữa các công cụ phân tích tĩnh truyền thống / mô hình cục bộ giá rẻ (làm nhiệm vụ thô tốn token) với các LLM suy luận đỉnh cao (làm nhiệm vụ ra quyết định và đánh giá rủi ro).

5. **Khủng hoảng An toàn trong Kỷ nguyên "Vibe Coding":**
   Phát hiện từ **SecureVibeBench (Bài 3)** gióng lên hồi chuông cảnh báo cho toàn ngành công nghiệp phần mềm: Các AI Agent hiện nay hoàn toàn có thể tạo ra các đoạn mã chạy trơn tru về mặt chức năng nhưng lại ẩn chứa các lỗ hổng tràn bộ nhớ, rò rỉ tài nguyên cực kỳ nghiêm trọng. Các quy trình CI/CD trong tương lai bắt buộc phải tích hợp các cơ chế kiểm thử an ninh tự động chuyên sâu (Dual-Oracle với Dynamic PoV và Fuzzing) trước khi chấp nhận mã nguồn do AI tạo ra.
