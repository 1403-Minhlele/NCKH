# STUDY REPORT: LLMs in Software Security

## 1. Thông tin bài báo

- **Tên bài báo:** LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights
- **Tác giả:** Ze Sheng, Zhicheng Chen, Shuning Gu, Heqing Huang, Guofei Gu, Jeff Huang
- **Đơn vị:** Texas A&M University; City University of Hong Kong
- **Tạp chí:** ACM Computing Surveys
- **Tập/số/bài:** Vol. 58, No. 5, Article 134
- **Năm xuất bản:** 2025, ngày xuất bản ghi trong bài là tháng 11/2025
- **DOI:** https://doi.org/10.1145/3769082
- **Trang:** 35 trang
- **Kho cập nhật của tác giả:** https://github.com/OwenSanzas/LLM-For-Vulnerability-Detection
- **Thời gian xử lý bản thảo:** nhận ngày 12/02/2025, sửa ngày 25/08/2025, chấp nhận ngày 15/09/2025

### 1.1. Phạm vi cần phân biệt khi đọc bài

Đây là survey tập trung vào **LLM-based vulnerability detection**. Bài có đề cập vulnerability reproduction, fuzzing và repair như các hướng ứng dụng hoặc hướng nghiên cứu liên quan, nhưng không xây dựng một taxonomy riêng và đầy đủ cho vulnerability repair. Vì vậy, không nên đồng nhất bài này với survey có tiêu đề _Large Language Model for Vulnerability Detection and Repair_ trong file tổng hợp được gửi kèm.

## 2. Tóm tắt bài báo

Bài báo khảo sát việc sử dụng Large Language Models (LLMs) cho phát hiện lỗ hổng phần mềm. Động lực chính xuất phát từ hạn chế của static analysis, dynamic analysis và các mô hình học sâu truyền thống: chúng có thể gặp false positive cao, khó mở rộng theo kích thước phần mềm, hoặc chỉ trả về nhãn nhị phân và thiếu lời giải thích cho nguyên nhân lỗ hổng.

Survey xem xét hơn 80 bài báo, trong đó khoảng 60 bài được chọn là có liên quan cao; phần phân tích chính đề cập 58 nghiên cứu. Các nghiên cứu được hệ thống hóa theo bốn câu hỏi:

1. Những LLM nào đã được sử dụng cho vulnerability detection?
2. Benchmark, dataset và metric nào được dùng để đánh giá?
3. Những kỹ thuật nào được áp dụng khi dùng LLM để phát hiện lỗ hổng?
4. Các thách thức hiện tại và hướng giải quyết tiềm năng là gì?

Kết luận tổng quát của bài báo là LLM có tiềm năng đáng kể trong hiểu mã nguồn, phân loại lỗ hổng, sinh giải thích và hỗ trợ fuzzing hoặc repair. Tuy nhiên, phần lớn nghiên cứu vẫn dừng ở function-level hoặc file-level, tập trung mạnh vào C/C++, sử dụng benchmark nhỏ hoặc dễ bị data leakage. Khả năng xử lý dependency xuyên file, repository-level context, zero-day, tính ổn định và explainability vẫn chưa đủ để thay thế các công cụ phân tích truyền thống.

## 3. Đóng góp và phạm vi của survey

### 3.1. Các đóng góp được tác giả nêu

Bài báo nêu ba đóng góp chính:

- Phân tích có hệ thống việc áp dụng LLM trong vulnerability detection.
- Xây dựng một framework thống nhất để xem xét mô hình, dataset, kỹ thuật và kết quả giữa các nghiên cứu.
- Chỉ ra các thách thức và hướng nghiên cứu tương lai, đặc biệt là cross-language detection, multimodal integration và repository-level analysis.

### 3.2. Phạm vi lựa chọn tài liệu

Quy trình lựa chọn được mô tả như sau:

1. Bắt đầu từ các venue bảo mật và software engineering như IEEE S&P, USENIX Security, ACM CCS, ICSE và IEEE Transactions on Software Engineering.
2. Tìm kiếm theo các từ khóa “vulnerability detection”, “LLM”, “large language model” và “AI”.
3. Lặp lại việc tìm kiếm khoảng ba tuần một lần trong thời gian hai tháng.
4. Sàng lọc khoảng 500–600 bài và chọn khoảng 60 nghiên cứu có liên quan cao.
5. Tập trung vào công trình từ giai đoạn gần đây, với phân bố hình minh họa từ 2017 đến 2025.

Survey giữ lại các nghiên cứu về vulnerability detection, chủ yếu trên C/C++, Java và Solidity. Các công trình chỉ dùng CNN, RNN, LSTM truyền thống hoặc tập trung vào malware analysis, network intrusion detection được loại khỏi phạm vi chính.

### 3.3.1. Kiểm chứng với file tổng hợp được gửi kèm

Các điểm sau trong file tổng hợp **không được bổ sung như kết quả của bài báo hiện tại**, vì không xuất hiện trong nội dung PDF được đối chiếu:

- tỷ lệ encoder-only 47,8% riêng cho detection;
- PU learning, causal learning, MEN, PPO và CodeBLEU;
- kết luận rằng encoder-only chiếm ưu thế cho detection còn decoder-only/encoder-decoder chiếm ưu thế cho repair;
- bảng hoặc taxonomy riêng phân tách adaptation techniques cho detection và repair.

Ngược lại, bài hiện tại có thể kiểm chứng được các nội dung tương ứng ở mức rộng hơn: ba nhóm kiến trúc encoder-only, encoder-decoder, decoder-only; các kỹ thuật AST/CFG/DFG, RAG, slicing, prompt engineering và fine-tuning; cùng các hướng reproduction, repair và fuzzing trong phần thách thức hoặc ứng dụng thực tế. Việc giữ sự phân biệt này tránh gán nhầm kết quả của một survey khác cho bài của Sheng và cộng sự.

### 3.4. Hạn chế về phạm vi

Theo phần Limitations, khoảng 60% nghiên cứu trong lĩnh vực này xuất hiện dưới dạng preprint trên arXiv. Terminology giữa các bài không thống nhất, nên việc tìm kiếm theo từ khóa có thể bỏ sót công trình. Ngoài ra, lĩnh vực biến đổi nhanh khiến các kết luận về model hoặc benchmark có thể nhanh chóng lỗi thời.

## 4. Bối cảnh nghiên cứu

### 4.1. Vì sao vulnerability detection quan trọng

Bài báo dẫn số liệu cho rằng khoảng 70% security vulnerabilities bắt nguồn từ các defect trong quy trình phát triển phần mềm. Trong khoảng năm năm trước thời điểm khảo sát, khoảng 120.000 CVE được phát hiện và báo cáo. Bài cũng nhắc đến sự cố CrowdStrike tháng 7/2024 như một ví dụ về tác động lan rộng của lỗi phần mềm đối với y tế, giao thông và tài chính.

### 4.2. Hạn chế của phương pháp truyền thống

- **Static analysis:** phân tích source code hoặc bytecode mà không chạy chương trình; có thể bao phủ rộng nhưng thường tạo nhiều cảnh báo dương tính giả và cần cấu hình chuyên môn.
- **Dynamic analysis:** quan sát chương trình khi chạy, trong đó có fuzz testing; có khả năng cung cấp bằng chứng thực thi nhưng phụ thuộc vào input, coverage và chi phí chạy.
- **Deep learning cho code:** học mẫu từ dataset, thường dùng sequence model hoặc graph neural network; có thể đạt điểm benchmark tốt nhưng thường trả về nhãn hoặc điểm quan trọng mà không giải thích được chuỗi nguyên nhân.

LLM được đưa vào vì có khả năng kết hợp hiểu code, instruction following, reasoning và sinh văn bản. Tuy nhiên, khả năng sinh lời giải thích không đồng nghĩa với việc lời giải thích luôn đúng; đây là một rủi ro quan trọng được survey nhấn mạnh.

### 4.3. Domain knowledge trong bảo mật

Survey phân biệt các khái niệm thường gặp:

- **CWE:** mô tả nguyên nhân hoặc dạng yếu điểm, ví dụ CWE-416 Use-After-Free và CWE-787 Out-of-bounds Write.
- **CVE:** định danh một lỗ hổng cụ thể trong sản phẩm hoặc phiên bản thực tế.
- **CVSS:** hệ thống chấm điểm mức độ nghiêm trọng từ 0 đến 10 dựa trên các yếu tố như exploitability và impact.
- **NVD:** cơ sở dữ liệu chứa CVE, CVSS, mô tả kỹ thuật và thông tin giảm thiểu rủi ro.

Việc đưa các chuẩn này vào prompt hoặc dataset giúp chuyển bài toán từ “có lỗi hay không” sang phát hiện, phân loại, giải thích và ưu tiên xử lý.

### 4.4. Đạo đức và nguy cơ lạm dụng

Bài báo dành riêng một mục cho tính lưỡng dụng của LLM trong vulnerability detection. Cùng một năng lực có thể giúp defender tìm và sửa lỗi, nhưng cũng có thể bị attacker dùng để:

- tăng tốc sinh exploit;
- hạ thấp rào cản gia nhập cho người tấn công;
- tự động hóa việc tìm lỗ hổng trên quy mô lớn.

Bài cũng nêu rủi ro về quyền riêng tư và sở hữu trí tuệ: model được huấn luyện trên code repository quy mô lớn có thể ghi nhớ hoặc tái sinh fragment nhạy cảm, từ đó gây rò rỉ code độc quyền, vấn đề cấp phép hoặc xử lý dữ liệu không phù hợp. Các đánh giá hiện tại thường tập trung vào accuracy và efficiency, nhưng ít đo tác động tổ chức, xã hội và rủi ro từ disclosure.

Các biện pháp được bài đề xuất gồm kiểm soát quyền truy cập model có năng lực cao, tuân thủ responsible disclosure, red-team để đánh giá khả năng lạm dụng và theo dõi provenance của dữ liệu huấn luyện. Đây là một phần quan trọng khi triển khai hệ thống, nhưng không nên hiểu là bài báo đã cung cấp một protocol đánh giá đạo đức định lượng hoàn chỉnh.

## 5. Cách bài báo hình thức hóa bài toán

### 5.1. Binary vulnerability detection

Với source code $C_i$ và detector $VD_i$, hệ thống trả về nhãn $Y_i \in \{0,1\}$:

- $Y_i = 1$: code vulnerable.
- $Y_i = 0$: code non-vulnerable.

Đây là formulation phổ biến nhất trong các nghiên cứu được khảo sát.

### 5.2. Vulnerability classification

Với classifier $VC_i$, đầu ra là loại lỗ hổng:

$$
Y_i = VC_i(C_i) \in \{type_1, type_2, \ldots, type_n\}
$$

`type` có thể là tên dễ đọc như Buffer Overflow, SQL Injection hoặc định danh CWE như CWE-79, CWE-89.

### 5.3. Severity prediction

Severity prediction có thể là:

- **Categorical classification:** low, medium, high.
- **Score regression/prediction:** dự đoán CVSS score trong khoảng 0–10.

Bài toán này quan trọng vì hệ thống thực tế không chỉ cần biết “có lỗ hổng”, mà còn cần biết nên xử lý lỗ hổng nào trước.

## 6. Taxonomy các LLM được sử dụng

### 6.1. Encoder-only

Encoder-only model dùng encoder của Transformer để tạo biểu diễn code và ngôn ngữ, phù hợp với code understanding và classification nhưng yếu hơn ở sequence generation hoặc code modification.

Các model được nêu gồm:

- BERT
- CodeBERT
- GraphCodeBERT
- CuBERT
- VulBERTa
- CCBERT
- SOBERT
- BERTOverflow

### 6.2. Encoder-decoder

Encoder-decoder kết hợp khả năng hiểu input và sinh output, phù hợp với translation, summarization và transformation của code. Nhược điểm là chi phí tính toán cao và đôi khi thiếu specialization cho một task bảo mật cụ thể.

Các ví dụ gồm:

- PLBART
- T5
- CodeT5
- UniXcoder
- NatGen

### 6.3. Decoder-only

Decoder-only dự đoán token tiếp theo dựa trên context, mạnh ở code generation, code completion, patching và sinh báo cáo. Nhóm này chiếm phần lớn các ứng dụng LLM được survey.

Các model được nhắc đến gồm:

- GPT-2, GPT-3, GPT-3.5, GPT-4
- CodeGPT và Codex
- PolyCoder, Incoder, CodeGen
- GitHub Copilot
- Code Llama
- StarCoder
- Mistral
- LLaMA

### 6.4. Phân bố sử dụng model

Trong 58 nghiên cứu, survey thống kê 33 LLM khác nhau:

- Encoder-only: 24,2% tổng số lượt sử dụng.
- Encoder-decoder: 8,7%.
- Decoder-only: 67,1%.
- GPT-4 xuất hiện 29 lần và GPT-3.5 xuất hiện 25 lần.
- Decoder-only chiếm khoảng 65% các thí nghiệm fine-tuning.
- Encoder-only vẫn chiếm ưu thế trong các nghiên cứu không fine-tuning, được bài báo ghi là 72,4%.

Top model được trình bày trong bài:

| Hạng | LLM           | Kiến trúc       | Kích thước được ghi trong bài |
| ---: | ------------- | --------------- | ----------------------------- |
|    1 | GPT-4         | Decoder-only    | Không công bố                 |
|    2 | GPT-3.5       | Decoder-only    | Không công bố                 |
|    3 | BERT          | Encoder-only    | 109M                          |
|    4 | CodeBERT      | Encoder-only    | 125M                          |
|    5 | CodeLlama     | Decoder-only    | 7B, 13B, 34B, 70B             |
|    6 | LLaMA         | Decoder-only    | 7B, 13B, 70B                  |
|    7 | StarCoder     | Decoder-only    | 15B                           |
|    8 | CodeT5        | Encoder-decoder | 220M                          |
|    9 | Mistral       | Decoder-only    | 7B                            |
|   10 | GraphCodeBERT | Encoder-only    | 125M                          |

### 6.5. Nhận xét

Xu hướng decoder-only phản ánh sự dịch chuyển từ biểu diễn code thuần túy sang hệ thống có thể vừa phân tích vừa sinh explanation, patch hoặc fuzz driver. Tuy nhiên, lợi thế generation không tự động giải quyết dependency analysis. Bảng taxonomy cũng cho thấy việc so sánh model cần kiểm soát prompt, dataset, context, decoding và mục tiêu đầu ra; nếu không, “model tốt hơn” có thể chỉ phản ánh điều kiện thí nghiệm khác nhau.

## 7. Ngôn ngữ và phân bố vulnerability

### 7.1. Ngôn ngữ mục tiêu

Theo 56 nghiên cứu được thống kê trong Figure 6:

| Ngôn ngữ | Tỷ lệ theo bài | Số nghiên cứu ghi trên hình |
| -------- | -------------: | --------------------------: |
| C/C++    |          50,0% |                          38 |
| Java     |          21,1% |                          16 |
| Solidity |          11,8% |                           9 |
| Python   |          10,5% |                           8 |
| Other    |           6,6% |                           5 |

C/C++ chiếm ưu thế vì liên quan đến memory corruption, buffer overflow, use-after-free và out-of-bounds. Java đứng thứ hai do phổ biến trong enterprise software, Android và web application. Solidity được chú ý vì smart contract có thể chứa lỗi logic gây thiệt hại tài chính trực tiếp.

### 7.2. Phân bố CVE theo hệ thống

Bảng CVE trong survey, với dữ liệu thu thập đến ngày 03/11/2024, đưa ra một số ví dụ:

| Hệ thống            | Nhà phát hành | CVE được ghi | Ngôn ngữ chính |
| ------------------- | ------------- | -----------: | -------------- |
| GitLab              | GitLab        |        1.068 | Ruby           |
| Chrome              | Google        |        3.539 | C++            |
| Firefox             | Mozilla       |        2.700 | C++            |
| Android             | Google        |        7.215 | Java           |
| macOS X             | Apple         |        3.206 | C              |
| Linux Kernel        | Linux         |        5.912 | C              |
| Windows Server 2022 | Microsoft     |        1.607 | C              |

Survey dùng bảng này để lập luận rằng operating systems, browsers và nền tảng phát triển tạo ra nhiều bối cảnh có lỗ hổng; memory-related vulnerability đặc biệt phổ biến trong code C/C++.

## 8. Dataset và benchmark

### 8.1. Phân loại theo granularity

#### Function-level

Mỗi item thường chứa implementation của function, cờ vulnerable/non-vulnerable và đôi khi cả phiên bản trước và sau khi sửa. BigVul và Devign là các ví dụ phổ biến.

Ưu điểm:

- dễ chuẩn hóa thành binary classification;
- phù hợp fine-tuning và benchmark nhanh;
- chi phí context và thực thi thấp.

Nhược điểm:

- tách khỏi caller, callee, global state và cấu hình;
- dễ bỏ qua nguyên nhân trải dài nhiều function hoặc nhiều file;
- ít đại diện cho quy trình phân tích thật trong repository.

#### File-level

Juliet C/C++ và Juliet Java là những ví dụ. File-level có thể giữ thêm trace, dòng lỗi và quan hệ giữa nhiều function, nhưng vẫn chưa phản ánh đầy đủ dependency của toàn project.

#### Commit-level

CVEfixes và Pan2023 chứa repository URL, commit hash, diff trước/sau và thông tin security patch. Mục tiêu là xác định thay đổi nào tạo ra hoặc sửa vulnerability.

Commit-level phù hợp với DeltaScan và code evolution, nhưng cần xử lý vấn đề patch localization, API ngoài corpus và nguy cơ train/test leakage theo repository hoặc commit.

#### Repository/application-level

CWE-Bench-Java là ví dụ repository-level; Ghera là application-level. Các dataset này có thể chứa metadata như CWE, CVE, remediation commit, version, hướng dẫn build/run, vulnerable application, malicious application và secure application.

Đây là mức dữ liệu sát thực tế nhất, nhưng khó xây dựng, tốn chi phí xác minh và đòi hỏi môi trường build/execution ổn định.

### 8.2. Các benchmark tiêu biểu

| Dataset           | Kích thước tổng (vulnerable) | Ngôn ngữ           | Phạm vi    | Nguồn       |
| ----------------- | ---------------------------: | ------------------ | ---------- | ----------- |
| BigVul            |             264.919 (11.823) | C/C++              | Function   | Real-world  |
| CVEfixes          |                       12.107 | C/C++, Python, PHP | Commit     | Real-world  |
| Juliet C/C++      |                       64.099 | C/C++              | File       | Synthesized |
| D2A               |           1.295.623 (18.653) | C/C++              | Function   | Real-world  |
| DiverseVul        |             349.437 (18.945) | C/C++              | Function   | Real-world  |
| SARD              |                hơn 5.000.000 | C/C++, Java, PHP   | File       | Mixed       |
| Juliet Java       |                       28.281 | Java               | File       | Synthesized |
| Smartbugs-curated |                          143 | Solidity           | Contract   | Mixed       |
| Smartbugs-wild    |                       47.518 | Solidity           | Contract   | Real-world  |
| Devign            |              27.318 (12.460) | C/C++              | Function   | Real-world  |
| ReVeal            |               18.169 (1.664) | C/C++              | Function   | Mixed       |
| SeVC              |             420.627 (56.395) | C/C++              | Function   | Mixed       |
| PrimeVul          |              235.768 (6.968) | C/C++              | Function   | Real-world  |
| MAGMA             |                          138 | C/C++, Lua, PHP    | Repository | Real-world  |
| VulDeeLocator     |             198.142 (40.450) | LLVM IR            | Function   | Mixed       |
| CWE-Bench-Java    |                          120 | Java               | Repository | Real-world  |
| FELLMVP           |                 15.637 (820) | Solidity           | Contract   | Real-world  |
| LLM4Vuln          |                     194 (97) | Java, Solidity     | Function   | Real-world  |

Trong bảng gốc, số trong ngoặc là số item vulnerable; “N/A” nghĩa là bài nguồn không cung cấp chi tiết. Bảng cũng phân biệt dataset open-source và có nhãn.

### 8.3. Hai hạn chế lớn của dataset

Survey đưa ra Finding II:

1. **Mất cân bằng ngôn ngữ:** C/C++ chiếm phần lớn, còn Java và các ngôn ngữ khác thiếu benchmark toàn diện.
2. **Khoảng trống về scope:** repository-level dataset còn rất ít, trong khi vulnerability thực tế thường liên quan nhiều file, dependency và call stack.

Ngoài ra còn có:

- label incorrectness do tự động thu thập mà thiếu human verification;
- duplicate và data leakage từ GitHub, software version cũ hoặc external libraries;
- class imbalance và long-tail vulnerability types;
- dataset tổng hợp có thể không phản ánh đầy đủ code production;
- ranh giới vulnerable/risk/secure chưa rõ trong các trường hợp phụ thuộc context.

### 8.4. Yêu cầu đối với benchmark chất lượng cao

Một benchmark tốt nên có:

- nhãn được kiểm chứng;
- chia train/validation/test theo thời gian, repository hoặc project để giảm leakage;
- metadata CWE, CVE, version, patch và severity;
- call sequence, control flow, data flow và reproduction trace;
- mô tả vulnerability và dòng liên quan;
- nhiều ngôn ngữ, nhiều loại vulnerability và các trường hợp long-tail;
- khả năng build, chạy và reproduce trong môi trường được kiểm soát.

## 9. Metrics được khảo sát

### 9.1. Classification metrics

- **Accuracy:**

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

- **Precision:**

$$
Precision = \frac{TP}{TP + FP}
$$

- **Recall:**

$$
Recall = \frac{TP}{TP + FN}
$$

- **F1-score:**

$$
F1 = \frac{2 \times Precision \times Recall}{Precision + Recall}
$$

- **Matthews Correlation Coefficient (MCC):**

$$
MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}
$$

MCC hữu ích khi dataset mất cân bằng, vì accuracy hoặc F1 có thể tạo ấn tượng quá lạc quan nếu negative chiếm đa số.

### 9.2. Generation và explainability metrics

Một số nghiên cứu dùng BLEU và ROUGE để đánh giá vulnerability description hoặc explanation sinh ra. Các metric này đo mức overlap giữa output và reference, nhưng không bảo đảm explanation đúng về mặt bảo mật hay có thể reproduce.

### 9.3. Efficiency metrics

Execution time, inference time, token consumption và chi phí gọi model quan trọng trong CI/CD hoặc FullScan. Survey ghi nhận các nghiên cứu đã bắt đầu quan tâm đến cost và latency, nhưng chưa có một protocol thống nhất giữa các model thương mại và open-source.

### 9.4. Đánh giá phản biện metrics

Điểm số classification không phản ánh đầy đủ giá trị của một cảnh báo. Một hệ thống thực tế còn cần trả lời:

- cảnh báo có đúng loại CWE không;
- dòng hoặc path nào thực sự liên quan;
- có reproduce được không;
- patch có qua test và loại bỏ được lỗi không;
- có sinh thêm vulnerability mới không;
- analyst mất bao nhiêu thời gian để xác minh;
- model có nhất quán qua nhiều lần chạy không.

Do đó, benchmark nên kết hợp detection, localization, reproduction, explanation, repair validation và human utility.

## 10. Các kỹ thuật dùng trong LLM-based vulnerability detection

### 10.1. Code preprocessing và semantic representation

#### AST analysis

AST biểu diễn cấu trúc cú pháp phân cấp. Nó được dùng để:

- tách code thành function hoặc đoạn có liên quan;
- giảm syntax noise;
- tạo structured comment tree;
- kết hợp với CFG, DFG và graph attention network;
- hỗ trợ localization trong code evolution.

Các framework hoặc nghiên cứu được nhắc gồm SCALE, DefectHunter, VulnArmor và GRACE.

#### Data flow và control flow

DFG mô tả cách dữ liệu truyền qua các statement; CFG mô tả các nhánh và đường thực thi. Chúng có thể được:

- đưa trực tiếp vào prompt cùng source code;
- lưu trong knowledge base để graph similarity search;
- dùng cùng call graph nhằm biểu diễn dependency giữa các function.

Lợi ích là cung cấp semantic context mà raw token sequence khó thể hiện. Nhược điểm là graph serialization có thể tăng token, tạo noise hoặc phụ thuộc mạnh vào độ chính xác của static analysis.

#### Retrieval-Augmented Generation (RAG)

RAG dùng searcher để lấy thông tin liên quan từ knowledge base rồi ghép vào prompt. Nguồn retrieval có thể là:

- CWE database;
- vulnerability report và CVE description;
- static analysis result;
- code snippet tương tự;
- knowledge base được LLM tóm tắt.

RAG giúp model có thêm kiến thức cập nhật và domain context, nhưng chất lượng phụ thuộc indexing, chunking, embedding, retrieval precision và khả năng phân biệt code similarity với semantic similarity.

#### Program slicing

Program slicing loại bỏ các dòng ít liên quan, giữ các statement nằm trên dependency path của một trigger. Các nghiên cứu dùng slicing cho buffer overflow, trigger function và vulnerability localization; một số nghiên cứu còn fine-tune model trực tiếp trên sliced code.

Slicing có thể giảm context và tăng khả năng tập trung, nhưng slice không đầy đủ có thể loại bỏ caller protection, global state, macro, configuration hoặc dependency quan trọng, từ đó gây false positive hoặc false negative.

#### LLVM IR

LLVM IR giúp giảm phụ thuộc vào ngôn ngữ nguồn và giữ một phần cấu trúc/semantic của chương trình. Hạn chế được bài báo nêu rõ là LLVM IR không phù hợp trực tiếp cho Java và JavaScript; IR cũng có thể làm mất các tín hiệu ở mức ngôn ngữ mà LLM cần hiểu.

### 10.2. Prompt engineering

#### Chain-of-Thought (CoT)

CoT yêu cầu LLM phân tích theo bước, ví dụ:

1. tóm tắt chức năng code;
2. xác định lỗi hoặc điều kiện nguy hiểm;
3. theo dõi data flow và control flow;
4. kết luận vulnerability và severity.

Survey cho rằng CoT thường giúp precision và tổ chức lập luận tốt hơn, nhưng ảnh hưởng đến recall thay đổi theo bối cảnh. Explanation sinh ra vẫn cần được kiểm chứng, vì reasoning dài không đồng nghĩa với reasoning đúng.

#### Few-shot learning

Few-shot đưa vào prompt một số ví dụ có nhãn, CWE hoặc severity. Kỹ thuật này hữu ích cho model nhỏ hoặc task có format đặc thù, nhưng thêm ví dụ có thể làm tăng token, gây bias và vô tình đưa pattern của test set vào prompt.

#### Zero-shot

Model lớn có thể hoạt động tốt với instruction ngắn và không cần nhiều ví dụ. Survey nhận xét model nhỏ thường hưởng lợi từ few-shot/structured prompt, trong khi model lớn có thể phù hợp hơn với zero-shot hoặc CoT.

#### Hierarchical context representation

Code được tổ chức theo module, class, function và statement. LLM xử lý từ abstraction cao xuống chi tiết, giúp giảm áp lực context window khi phân tích codebase lớn.

#### Multi-level prompting

Nhiệm vụ được tách thành nhiều prompt: tổng quan chức năng, nhận diện issue, phân tích vùng cụ thể và sinh report. Cách này có thể làm reasoning rõ hơn nhưng làm tăng số lần gọi model, latency và chi phí.

#### Multiple agents và prompt templates

Các agent chuyên biệt có thể đảm nhận summarization, vulnerability identification, localization, severity hoặc review. Cách chia task giúp tăng tính modular, nhưng nhiều agent không bảo đảm chất lượng nếu mỗi agent dùng context thiếu hoặc các kết luận không được kiểm chứng chéo.

### 10.3. Fine-tuning

#### Full fine-tuning

FFT cập nhật toàn bộ tham số, thường chỉ khả thi với model nhỏ hơn khoảng 15B trong các nghiên cứu được khảo sát. Ưu điểm là khả năng thích ứng cao; nhược điểm là chi phí GPU, nguy cơ overfitting và yêu cầu dataset lớn.

#### Parameter-efficient fine-tuning

PEFT chỉ cập nhật một phần tham số hoặc thêm adapter. Các kỹ thuật được nhắc gồm adapter, LoRA và QLoRA. Chúng giảm memory và compute, phù hợp với CodeLlama, Llama hoặc model lớn hơn.

#### Discriminative fine-tuning

Model được huấn luyện để trả về nhãn binary hoặc multi-class. Cách này thuận lợi khi mục tiêu là classification chính xác và format ổn định.

#### Generative fine-tuning

Model học sinh vulnerability description, vulnerable line hoặc structured report. Nó giàu thông tin hơn nhưng khó đánh giá, vì văn bản có thể trôi chảy mà vẫn sai về nguyên nhân.

### 10.3.1. Các kết quả fine-tuning được Table 5 tổng hợp

Table 5 của bài cho thấy fine-tuning được áp dụng trên nhiều ngôn ngữ và dataset, nhưng các kết quả không nên xếp hạng trực tiếp vì điều kiện thí nghiệm khác nhau. Một số ví dụ được bài ghi nhận:

| Nghiên cứu      | Ngôn ngữ | Phương pháp | Dataset    | Model và F1-score được báo cáo |
| --------------- | -------- | ----------- | ---------- | ------------------------------ |
| Alam et al.     | Solidity | PEFT        | VulSmart   | GPT-4o-mini, 0,99              |
| Ding et al.     | C/C++    | FFT         | PrimeVul   | UnixCoder, 0,21                |
| Du et al.       | C/C++    | FFT + IFT   | Devign     | CodeLlama, 0,71                |
| Ghosh et al.    | C/C++    | DAPT        | NVD        | MPT-7B, 0,93                   |
| Guo et al.      | C/C++    | FFT + PEFT  | Devign     | CodeLlama-7B, 0,97             |
| Haurogné et al. | C/C++    | FFT         | DiverseVul | BERT, 0,69                     |
| Luo et al.      | C/C++    | PEFT        | Liu2023    | Gemma-7B, 0,90                 |
| Ma et al.       | Solidity | PEFT        | Ma2024     | CodeLlama-13B, 0,91            |
| Yin et al.      | C/C++    | FFT         | Big-Vul    | DeepSeek-Coder-6.7B, 0,270     |

Bài cũng ghi nhận các kết quả đáng chú ý sau:

- Một thí nghiệm trên PrimeVul đạt F1 chỉ 0,21 dù đã huấn luyện và validation trên dataset này; một nghiên cứu khác đạt 0,099 trên PrimeVul nhưng 0,66 trên Choi2017. Đây là dấu hiệu cho thấy kết quả phụ thuộc mạnh vào dataset và split.
- PEFT gồm adapter, LoRA và QLoRA giúp giảm số tham số cần cập nhật. Survey nêu ví dụ LoRA đạt F1 0,72 trong một nghiên cứu và 0,97 trong nghiên cứu khác trên các dataset tương ứng; QLoRA đạt accuracy 59% với memory thấp hơn trong một nghiên cứu Solidity.
- Với generative fine-tuning, CodeT5+ được báo cáo đạt ROUGE 0,722, cao hơn DeepSeek-Coder 6.7B đạt 0,425 trong một tác vụ sinh output.

Các con số trên là số liệu do survey trích từ từng bài nguồn, không phải một thực nghiệm chung. Vì thế chúng chỉ hỗ trợ nhận diện xu hướng, không chứng minh model có F1 cao nhất một cách công bằng.

### 10.4. Finding III–V của survey

- **Finding III:** 41,3% nghiên cứu dùng code processing như graph, RAG hoặc slicing. Các kỹ thuật này cải thiện việc sử dụng context nhưng hiệu quả giảm rõ rệt với vulnerability xuyên file; khi model lớn hơn, lợi ích từ bản thân model đôi khi vượt lợi ích của preprocessing.
- **Finding IV:** CoT được báo cáo là phổ biến trong các nghiên cứu model lớn hơn 10B; model nhỏ có thể phù hợp với zero-shot hoặc few-shot tối giản hơn.
- **Finding V:** Fine-tuning, nhất là PEFT trên model lớn, cho kết quả tốt trong một số benchmark; discriminative learning thường cần dataset ít nhất khoảng 10.000 mẫu theo tổng hợp của bài, trong khi compute và chất lượng nhãn vẫn là nút thắt.

## 11. Real-world use cases

### 11.1. FullScan

FullScan phân tích toàn bộ codebase, phù hợp khi chuẩn bị major release hoặc tích hợp external library mới. OSSFuzzGen được survey nêu như một ví dụ open-source:

1. tích hợp project vào OSS-Fuzz;
2. dùng LLM tìm coverage gap và sinh fuzz target;
3. tự sửa build error qua feedback loop;
4. chạy fuzz target liên tục để phát hiện crash.

LLM ở đây không chỉ “đọc code và trả nhãn”, mà hỗ trợ tạo artifact có thể thực thi và dùng dynamic evidence.

### 11.2. DeltaScan

DeltaScan tập trung vào commit hoặc thay đổi gần đây nhằm phát hiện vulnerability mới được đưa vào. Bài báo nhắc đến FuzzBrain và Buttercup như các nỗ lực liên quan đến AIxCC. Workflow thường là phân tích commit, sinh fuzz driver hoặc input, rồi kiểm tra xem thay đổi có tạo crash hoặc security issue không.

### 11.3. Ý nghĩa triển khai

Survey cho thấy hướng thực tế có xu hướng kết hợp LLM với:

- static analysis;
- repository search và RAG;
- fuzzing;
- build/test feedback;
- vulnerability reproduction;
- patch validation.

Điều này thực tế hơn việc dùng LLM như một classifier độc lập, vì bằng chứng thực thi có thể giảm false positive và làm report dễ kiểm chứng.

## 12. Bốn thách thức chính và hướng giải quyết

### 12.1. Challenge 1: Phạm vi bài toán quá hẹp

Khoảng 40 nghiên cứu, tương đương 83% theo bài báo, tập trung vào isolated code snippet. Đây là môi trường dễ kiểm soát nhưng không thể hiện:

- cross-file dependency;
- repository architecture;
- code evolution;
- collaborative development;
- configuration và external API;
- vulnerability phát sinh từ tương tác nhiều component.

**Hướng đề xuất:**

- Full-scale detection trên toàn repository.
- Incremental detection trên commit.
- Vulnerability reproduction bằng fuzzing hoặc driver sinh tự động.
- Vulnerability repair với test, reproduction và regression validation.
- Classification theo CWE và severity prediction.
- Specialized detector cho từng nhóm vulnerability.

### 12.2. Challenge 2: Biểu diễn semantic của vulnerability phức tạp

Vulnerability thường phụ thuộc external dependency, nhiều function call, global variable, state phức tạp và call stack dài. LLM bị giới hạn input, dễ gặp unseen code và có thể kết luận sai khi function bị phân tích tách biệt khỏi caller.

**Hướng đề xuất:**

- Dynamic code knowledge expansion qua feedback loop và adaptive retrieval.
- Kết hợp AST, CFG, DFG, call graph và representation giàu semantic hơn.
- Dùng neural-symbolic hoặc CodeQL để cung cấp fact có kiểm chứng.
- Agent chuyên biệt cho summarization, taint tracking, localization và validation.
- RAG dành riêng cho code, thay vì áp dụng nguyên xi embedding của natural language.

### 12.3. Challenge 3: Hạn chế nội tại của LLM

LLM nhạy với data perturbation, có output không ổn định và có thể sinh explanation sai dù nhãn cuối đúng. Đây là vấn đề đặc biệt nghiêm trọng nếu explanation được dùng để sửa code hoặc ra quyết định disclosure.

**Hướng đề xuất:**

- Fine-tune frontier model hoặc model chuyên biệt theo vulnerability type.
- Repository-adaptive fine-tuning.
- Ensemble prediction để giảm false positive.
- Adaptive learning và feedback loop để cập nhật threat landscape.
- Calibrated confidence, uncertainty estimation và repeated-run consistency.
- Kiểm chứng explanation bằng static/dynamic analysis thay vì chỉ chấm BLEU/ROUGE.

### 12.4. Challenge 4: Thiếu dataset chất lượng cao

Các vấn đề chính là label sai, data leakage, kích thước hoặc scope nhỏ và mất cân bằng vulnerability type.

**Hướng đề xuất:**

- Xây test set nhỏ nhưng chất lượng cao từ các mẫu đã được kiểm chứng.
- Tách dữ liệu theo thời gian và repository để giảm leakage.
- Xây repository-level dataset có call sequence, control flow và reproduction trace.
- Dùng synthetic data có kiểm soát cho rare vulnerability nhưng phải đánh giá transfer sang code thực.
- Kết hợp verified samples với data augmentation và CWE metadata.
- Tạo nhãn nhiều mức: safe, potential risk, confirmed vulnerability.

## 13. Các phát hiện tổng hợp quan trọng

### Finding I: C/C++ thống trị nghiên cứu

C/C++ chiếm 50% nghiên cứu, Java 21,1%, Solidity 11,8%, còn lại là Python, PHP, Go và các ngôn ngữ khác. Điều này phản ánh mức độ quan tâm tới memory safety và smart contract, nhưng cũng cho thấy khả năng generalize cross-language còn hạn chế.

### Finding II: Dataset chưa cân bằng về ngôn ngữ và scope

C/C++ có nhiều dataset hơn Java; repository-level dataset rất hiếm. Đây là nguyên nhân khiến điểm benchmark function-level chưa thể đại diện cho khả năng triển khai thực tế.

### Finding III: Code processing có ích nhưng chưa giải quyết context lớn

AST, graph, RAG và slicing có thể giảm noise hoặc bổ sung semantic, nhưng hiệu quả giảm khi vulnerability kéo dài qua nhiều file. Có sự đánh đổi giữa context đầy đủ và token/chi phí.

### Finding IV: Prompt phụ thuộc kích thước model

Model nhỏ thường cần few-shot hoặc prompt có cấu trúc; model lớn hưởng lợi từ CoT và zero-shot. Tuy nhiên, kết luận này cần được kiểm tra trên cùng dataset, budget và protocol vì các nghiên cứu không luôn đồng nhất.

### Finding V: Fine-tuning giúp thích nghi nhưng đắt và phụ thuộc dữ liệu

PEFT làm giảm chi phí so với FFT, còn discriminative fine-tuning phù hợp detection. Dù vậy, điểm số cao chỉ đáng tin khi dataset sạch, leakage được kiểm soát và test độc lập với train distribution.

### Finding VI: Nên chuyển từ binary classification sang workflow hoàn chỉnh

Nghiên cứu có giá trị thực tế hơn khi bao gồm discovery, localization, reproduction, classification, severity và repair validation.

### Finding VII: Cần kết hợp LLM với semantic tools

RAG, AST, CFG, DFG, neural-symbolic methods và specialized agents là các hướng để cung cấp context và fact có cấu trúc.

### Finding VIII: Robustness và explainability là điều kiện triển khai

Tính chính xác trung bình chưa đủ; hệ thống cần ổn định trước perturbation, giải thích đúng, có confidence đáng tin và hoạt động được khi code thay đổi.

### Finding IX: Dataset phải được thiết kế theo research scope

Dataset phục vụ binary function-level không thể đánh giá tốt repository scanning hoặc repair. Mỗi mục tiêu cần benchmark, annotation và validation protocol riêng.

## 14. Đánh giá phản biện bài báo

### 14.1. Điểm mạnh

- Đưa ra khung RQ rõ ràng, bao phủ model, dataset, technique và challenge.
- Kết nối software security với software engineering và LLM research.
- Phân biệt function/file/commit/repository/application-level, giúp nhìn thấy chênh lệch giữa benchmark và production.
- Tổng hợp cả prompt engineering, preprocessing, RAG, graph, slicing và fine-tuning.
- Đề cập ethical issues: dual-use, exploit generation, data privacy, intellectual property và responsible disclosure.
- Nhấn mạnh reproduction, repair validation và human utility thay vì chỉ nhìn vào accuracy.

### 14.2. Hạn chế cần lưu ý khi sử dụng kết luận

- Quy trình tìm kiếm được mô tả nhưng không trình bày đầy đủ protocol kiểu systematic review như database cụ thể, tiêu chí loại trừ chi tiết, inter-rater agreement hoặc bảng đầy đủ của mọi bài được sàng lọc.
- Một số tỷ lệ được tính trên các tập con khác nhau: 56 nghiên cứu cho ngôn ngữ, 58 nghiên cứu cho model, khoảng 60 nghiên cứu cho lựa chọn tài liệu. Vì vậy không nên cộng hoặc so sánh các tỷ lệ này như cùng một mẫu thống kê.
- Nhiều số liệu là tổng hợp từ báo cáo của các bài nguồn, với dataset, split, prompt và metric không đồng nhất. Chúng phù hợp để chỉ ra xu hướng hơn là xếp hạng tuyệt đối.
- Một số mô tả như “100% nghiên cứu gần đây dùng CoT” hoặc “fine-tuning model lớn đạt gần 0,9 F1” cần được đọc trong đúng subset và điều kiện mà bài báo đã chọn.
- BLEU/ROUGE không đủ để xác nhận explanation bảo mật đúng.
- Các claim về model frontier có thể nhanh chóng lỗi thời do survey xuất bản trong giai đoạn model thay đổi nhanh.
- Việc đưa cả công trình về fuzzing, repair hoặc agent vào cùng bức tranh vulnerability detection có ích cho roadmap nhưng có thể làm ranh giới task không hoàn toàn đồng nhất.

### 14.3. Hàm ý phương pháp luận

Khi dùng survey này làm nền tảng cho luận văn hoặc thực nghiệm, nên:

1. Trích dẫn xu hướng và khoảng trống ở cấp survey.
2. Trích dẫn số liệu hiệu năng cụ thể từ bài gốc, không chỉ từ bảng tổng hợp.
3. Ghi rõ dataset version, split, prompt, model version và inference setting.
4. Báo cáo MCC hoặc PR-AUC khi dữ liệu mất cân bằng.
5. Kiểm soát leakage theo repository, commit, function clone và thời gian.
6. Bổ sung localization, reproduction, explanation correctness và human review.

## 15. So sánh với hướng CoTVD trong repo hiện tại

Bài survey có liên quan trực tiếp tới thư mục `COTVD` vì nó đề cập các ý tưởng cốt lõi của CoTVD: function-level detection, C/C++ là ngôn ngữ chính, CoT prompting, code slicing, data/control flow và đánh giá LLM.

Có thể đối chiếu như sau:

| Khía cạnh       | CoTVD                                              | Survey này                                                                                    |
| --------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Loại công trình | Framework/phương pháp cụ thể                       | Tổng quan nhiều nghiên cứu                                                                    |
| Phạm vi         | Chủ yếu C/C++, function-level                      | C/C++, Java, Solidity và ngôn ngữ khác                                                        |
| Context         | Dependency slice bằng Joern                        | AST, CFG, DFG, RAG, slicing, LLVM IR, call graph                                              |
| Prompt          | CoT và instruction có cấu trúc                     | CoT, few-shot, zero-shot, multi-level, multi-agent                                            |
| Dataset         | Devign và ReVeal, lọc mẫu có library call nhạy cảm | BigVul, Devign, ReVeal, CVEfixes, Juliet, D2A, PrimeVul, repository datasets và nhiều bộ khác |
| Mục tiêu        | Detection và explanation ở mức function            | Detection, classification, severity, localization, reproduction, repair và fuzzing            |
| Điểm mạnh       | Có pipeline static analysis + LLM cụ thể           | Cho bức tranh rộng và roadmap nghiên cứu                                                      |
| Rủi ro          | False positive do nhạy với potential risk          | Tổng hợp không đồng nhất, leakage, context và explainability                                  |

Survey củng cố lý do CoTVD dùng dependency representation trước khi gọi LLM, nhưng đồng thời cho thấy giới hạn của function-level slice: nếu slice bỏ qua context xuyên file, LLM vẫn có thể không đủ thông tin để kết luận chính xác.

## 16. Hướng nghiên cứu đề xuất từ bài survey

Dựa trên các khoảng trống của bài báo, một hướng nghiên cứu khả thi có thể là pipeline nhiều tầng:

```text
Repository / Commit
        |
        v
Static analysis: AST + CFG + DFG + call graph + taint facts
        |
        v
Retrieval: CWE, CVE, code context, historical patch, similar flow
        |
        v
LLM reasoning: summarize -> detect -> classify -> localize -> score
        |
        v
Dynamic validation: test / fuzz / reproduction
        |
        v
Report and repair candidate
        |
        v
Patch validation: tests + reproduction blocked + security regression check
```

Các câu hỏi thực nghiệm nên được thiết kế tách bạch:

- Dependency graph có giúp hơn raw code khi giữ nguyên token budget không?
- RAG lấy CWE/CVE có làm giảm false positive hay chỉ làm output dài hơn?
- CoT cải thiện localization và explanation correctness đến mức nào?
- Model có ổn định khi thay đổi thứ tự code, comment hoặc tên biến không?
- Fine-tuning theo vulnerability type có transfer sang repository mới không?
- Phân tích commit có phát hiện vulnerability chưa từng thấy trong training không?
- Human analyst có hoàn thành task nhanh và chính xác hơn với report của LLM không?

## 17. Kết luận

Bài báo cung cấp một bản đồ tương đối toàn diện về LLM-based vulnerability detection đến năm 2025. Thông điệp trung tâm là LLM đã vượt qua vai trò classifier đơn giản: nó có thể hỗ trợ hiểu code, sinh explanation, truy hồi knowledge, tạo fuzz driver, định vị lỗ hổng và đề xuất repair. Tuy nhiên, kết quả tốt trên function-level benchmark chưa chứng minh rằng LLM đã giải quyết vulnerability detection trong repository thực tế.

Ba nút thắt quan trọng nhất là:

1. **Context:** LLM chưa xử lý đáng tin cậy dependency dài, cross-file và repository-level.
2. **Evidence:** explanation và nhãn cần được kiểm chứng bằng static/dynamic execution, test hoặc reproduction.
3. **Data:** benchmark còn mất cân bằng, có label error và data leakage.

Vì vậy, hướng triển khai hợp lý là mô hình lai: LLM đảm nhận reasoning, summarization và giao tiếp với analyst; static analysis cung cấp fact có cấu trúc; RAG cung cấp domain knowledge; fuzzing/test/reproduction cung cấp bằng chứng thực thi. Các đánh giá tương lai cần đo toàn bộ workflow từ phát hiện đến xác minh và sửa lỗi, thay vì chỉ báo cáo accuracy hoặc F1 trên các đoạn code cô lập.

## 18. Tài liệu và nguồn chính được bài báo nhắc đến

Một số nguồn quan trọng trong survey:

- Devign: graph-based vulnerability identification.
- ReVeal: deep learning based vulnerability detection.
- BigVul: C/C++ code vulnerability dataset with code changes and CVE summaries.
- CVEfixes: collection of vulnerabilities and fixes from open-source software.
- DiverseVul, PrimeVul, D2A và SeVC.
- Juliet C/C++ và Juliet Java trong SARD.
- SmartBugs-curated và SmartBugs-wild cho Solidity.
- CWE-Bench-Java, Ghera và MAGMA cho repository/application-level evaluation.
- CodeBERT, GraphCodeBERT, CodeT5, CodeLlama, GPT, StarCoder và các code LLM khác.
- RAG, CoT prompting, AST/CFG/DFG, program slicing và LLVM IR.
- OSSFuzzGen, Fuzz4All, KernelGPT, WhiteFox và các hệ thống LLM hỗ trợ fuzzing.

Báo cáo này không thay thế bài báo gốc; các con số, taxonomy và kết luận nên được kiểm tra lại với phiên bản PDF/online chính thức khi dùng trong luận văn hoặc công bố khoa học.
