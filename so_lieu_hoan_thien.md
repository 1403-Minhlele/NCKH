# Số liệu hoàn thiện

## 1. Tổng quan các nghiên cứu về LLM trong phát hiện lỗ hổng phần mềm

| STT | Tên bài báo                                                                                          | Viết tắt            | Năm  | Venue                             | Loại nghiên cứu                            | Tập dữ liệu                        | Phương pháp                               | Chỉ số chính                     | Kết quả chính                                          |
| --- | ---------------------------------------------------------------------------------------------------- | ------------------- | ---- | --------------------------------- | ------------------------------------------ | ---------------------------------- | ----------------------------------------- | -------------------------------- | ------------------------------------------------------ |
| 1   | CoTVD: A function-level vulnerability detection framework using chain-of-thought reasoning with LLMs | CoTVD               | 2024 | Repo nghiên cứu / paper           | Detection via LLM reasoning                | Devign + Reveal                    | Joern slicing + GPT-4o + Chain-of-Thought | Precision, Recall, F1            | Precision 39.09%, Recall 94.77%, F1 0.553              |
| 2   | LIVA: A Multi-Agent LLM-Assisted System for IoT Vulnerability Analysis                               | LIVA                | 2026 | IEEE TDSC                         | IoT vulnerability analysis                 | 64 firmware, 11 hãng               | Multi-agent LLM + taint analysis          | Recall, Precision, thời gian     | Recall 98.1%, Precision 74.6%                          |
| 3   | RLV: LLM-based vulnerability detection by retrieving and refining contextual information             | RLV                 | 2026 | The Journal of Systems & Software | Function-level detection with repo context | FFmpeg+QEMU, DiverseVul            | Retrieval + refinement + DeepSeek-R1      | F1, Precision, Recall            | FFmpeg+QEMU F1 0.6428; DiverseVul F1 0.3258            |
| 4   | LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights               | Survey-LLM-Security | 2025 | ACM Computing Surveys             | Survey                                     | 58 nghiên cứu                      | Systematic review                         | Taxonomy, model usage, benchmark | Decoder-only chiếm >65% thí nghiệm                     |
| 5   | Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead    | Survey-Lit-Review   | 2025 | Review paper                      | Systematic review                          | Nghiên cứu LLM detection và repair | SLR + taxonomy                            | Số lượng paper, roadmap          | Tập trung vào adaptation, dataset, deployment, hạn chế |
| 6   | COTVD source dataset summary                                                                         | COTVD-Repo          | 2024 | Repo experiment                   | Data pipeline                              | Devign + Reveal                    | Filter sensitive function + Joern slice   | Số lượng sample                  | 3435 positive / 6018 negative                          |

## 2. Kết quả trọng tâm

- Mục tiêu chính: Phân tích và phát hiện lỗ hổng phần mềm bằng LLM.
- Phạm vi dữ liệu: C/C++, source code và repository-level context.
- LLM nền phổ biến: GPT-4, GPT-4o, DeepSeek-R1, Qwen3-32B.
- Chỉ tiêu đánh giá: Precision, Recall, F1, độ tổng quát hóa.
- Điểm nổi bật: Context repository + dependency slice + prompt reasoning giúp cải thiện hiệu năng.

## 3. Dữ liệu chi tiết theo từng nghiên cứu

### CoTVD

- Năm: 2024
- Mô hình: GPT-4o-128K
- Dữ liệu: Devign + Reveal
- Kết quả: Precision 39.09%, Recall 94.77%, F1 0.553
- Ghi chú: Pipeline tập trung vào dependency slice + reasoning bằng Chain-of-Thought.

### LIVA

- Năm: 2026
- Mô hình: Qwen3-32B + agent suy luận
- Dữ liệu: 64 firmware của 11 hãng
- Kết quả: Recall 98.1%, Precision 74.6%
- Ghi chú: Phát hiện 64 zero-day, trong đó 39 lỗi có CVE/CNVD.

### RLV

- Năm: 2026
- Mô hình: DeepSeek-R1
- Dữ liệu: FFmpeg+QEMU, DiverseVul
- Kết quả: FFmpeg+QEMU F1 0.6428; DiverseVul F1 0.3258
- Ghi chú: Tăng hiệu quả tổng quát hóa trên dự án chưa từng thấy.

### Survey LLM in Software Security

- Năm: 2025
- Đối tượng: 58 nghiên cứu
- Kết luận: Decoder-only chiếm >65% thí nghiệm; GPT-4 và GPT-3.5 xuất hiện nhiều nhất.
- Ghi chú: Cung cấp taxonomy, benchmark, thách thức và hướng nghiên cứu tương lai.

## 4. Bản tóm tắt ngắn để copy vào Excel

| STT | Tên nghiên cứu                 | Viết tắt            | Năm  | Kết quả chính                                          |
| --- | ------------------------------ | ------------------- | ---- | ------------------------------------------------------ |
| 1   | CoTVD                          | CoTVD               | 2024 | Precision 39.09%, Recall 94.77%, F1 0.553              |
| 2   | LIVA                           | LIVA                | 2026 | Recall 98.1%, Precision 74.6%                          |
| 3   | RLV                            | RLV                 | 2026 | FFmpeg+QEMU F1 0.6428; DiverseVul F1 0.3258            |
| 4   | Survey LLM Security            | Survey-LLM-Security | 2025 | Decoder-only chiếm >65% thí nghiệm                     |
| 5   | Literature Review & Road Ahead | Survey-Lit-Review   | 2025 | Tập trung vào adaptation, dataset, deployment, roadmap |

## 5. Dạng dữ liệu chuẩn để paste vào Excel

STT, Tên bài báo, Viết tắt, Năm, Venue, Loại nghiên cứu, Tập dữ liệu, Phương pháp, Chỉ số chính, Kết quả chính
1, CoTVD: A function-level vulnerability detection framework using chain-of-thought reasoning with LLMs, CoTVD, 2024, Repo nghiên cứu, Detection via LLM reasoning, Devign + Reveal, Joern slicing + GPT-4o + Chain-of-Thought, Precision, Recall, F1, Precision 39.09%, Recall 94.77%, F1 0.553
2, LIVA: A Multi-Agent LLM-Assisted System for IoT Vulnerability Analysis, LIVA, 2026, IEEE TDSC, IoT vulnerability analysis, 64 firmware, 11 hãng, Multi-agent LLM + taint analysis, Recall, Precision, thời gian, Recall 98.1%, Precision 74.6%
3, RLV: LLM-based vulnerability detection by retrieving and refining contextual information, RLV, 2026, The Journal of Systems & Software, Function-level detection with repo context, FFmpeg+QEMU, DiverseVul, Retrieval + refinement + DeepSeek-R1, F1, Precision, Recall, FFmpeg+QEMU F1 0.6428; DiverseVul F1 0.3258
4, LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights, Survey-LLM-Security, 2025, ACM Computing Surveys, Survey, 58 nghiên cứu, Systematic review, Taxonomy, model usage, benchmark, Decoder-only chiếm >65% thí nghiệm
5, Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead, Survey-Lit-Review, 2025, Review paper, Systematic review, Nghiên cứu LLM detection và repair, SLR + taxonomy, Số lượng paper, roadmap, Tập trung vào adaptation, dataset, deployment, hạn chế

## 6. Gợi ý cách điền vào Excel

- Cột A: STT
- Cột B: Tên bài báo
- Cột C: Viết tắt
- Cột D: Năm
- Cột E: Venue
- Cột F: Loại nghiên cứu
- Cột G: Tập dữ liệu
- Cột H: Phương pháp
- Cột I: Chỉ số chính
- Cột J: Kết quả chính

Bạn có thể copy trực tiếp các dòng ở phần 5 vào Excel và cắt theo đúng số cột.
