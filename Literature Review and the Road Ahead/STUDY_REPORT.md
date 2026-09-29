# STUDY REPORT: Large Language Model for Vulnerability Detection and Repair

Báo cáo này phân tích bài báo **“Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead”** của Xin Zhou và cộng sự. Nội dung được tổng hợp từ PDF được cung cấp, tập trung vào phương pháp systematic literature review (SLR), kết quả trả lời bốn RQ, các kỹ thuật adaptation, đặc điểm dataset, deployment, hạn chế và roadmap nghiên cứu.

## 1. Thông tin bài báo

- **Tên bài báo:** Large Language Model for Vulnerability Detection and Repair: Literature Review and the Road Ahead
- **Tác giả:** Xin Zhou, Sicong Cao, Xiaobing Sun, David Lo
- **Đơn vị:** Singapore Management University và Yangzhou University
- **Tạp chí:** ACM Transactions on Software Engineering and Methodology (TOSEM)
- **Tập/số/bài:** Vol. 34, No. 5, Article 145
- **Năm xuất bản:** 2025
- **Ngày xuất bản:** tháng 5/2025
- **DOI:** https://doi.org/10.1145/3708522
- **Độ dài:** 31 trang
- **Khoảng thời gian tìm kiếm:** tháng 01/2018 đến tháng 03/2024
- **Tập nghiên cứu cuối cùng:** 58 primary studies
- **Giấy phép:** Creative Commons Attribution International 4.0
- **Ngày nhận/sửa/chấp nhận:** 03/04/2024, 30/09/2024, 19/11/2024

## 2. Tóm tắt bài báo

Bài báo thực hiện một SLR về việc sử dụng Large Language Models (LLMs) cho hai nhiệm vụ trong software security: **vulnerability detection** và **vulnerability repair**. Mục tiêu là tổng hợp các model đã được sử dụng, phân loại cách thích ứng LLM cho từng task, phân tích dataset và chiến lược deployment, đồng thời đề xuất roadmap nghiên cứu.

Bài khảo sát cuối cùng 58 nghiên cứu. Phần tóm tắt cho biết tập này gồm 43 bài đã xuất bản tại 25 venue và 15 preprint chất lượng cao. Trong phần methodology, quy trình lọc được mô tả chi tiết hơn: 35 bài từ manual search, 1.500 kết quả từ automated search, 42 bài sau quality assessment và thêm 16 bài từ snowballing. Vì các con số này thuộc các giai đoạn khác nhau của quy trình, không nên cộng chúng cơ học.

Các kết luận trung tâm của survey là:

- CodeBERT và encoder-only model chiếm ưu thế trong vulnerability detection.
- CodeT5, decoder-only model và commercial LLM nổi bật hơn trong vulnerability repair.
- Fine-tuning là kỹ thuật thích ứng phổ biến nhất trong cả hai task.
- Detection thường được đánh giá ở function-level với heuristic labels.
- Repair thường sử dụng function-level data nhưng thiếu test case để xác nhận patch.
- Repo-level, class-level, developer interaction và workflow integration còn rất ít được nghiên cứu.
- Accuracy và robustness hiện tại chưa đủ để bảo đảm khả năng triển khai thực tế.

## 3. Bối cảnh và động lực nghiên cứu

### 3.1. Vấn đề vulnerability detection và repair

Software vulnerability là một lỗi hoặc điểm yếu trong phần mềm có thể bị attacker khai thác. Các nghiên cứu trước đã xây dựng detector tự động và công cụ repair, nhưng vẫn tồn tại các vấn đề về false positive, độ bao phủ vulnerability và khả năng xử lý nhiều dạng code khác nhau.

LLM được quan tâm vì được pre-train trên corpus lớn, có thể học đặc trưng từ vulnerability đã biết, hỗ trợ tìm vulnerability chưa thấy trong dữ liệu và sinh code sửa lỗi. Ngoài việc dự đoán nhãn, LLM còn có thể nhận instruction, sử dụng context và sinh output dạng code hoặc ngôn ngữ tự nhiên.

### 3.2. Hạn chế của các hướng trước

- **Rule-based detector:** phụ thuộc vào luật được thiết kế thủ công và có thể tạo nhiều cảnh báo sai.
- **Program-analysis-based repair:** có thể khó thích ứng với nhiều loại vulnerability khác nhau.
- **Deep learning truyền thống:** thường được huấn luyện cho một dataset hoặc một granularity cụ thể, có thể gặp vấn đề với context dài, data noise và vulnerability liên thủ tục.
- **Đánh giá offline:** nhiều công trình chỉ dùng static/historical data, chưa chứng minh được lợi ích trong workflow của developer.

### 3.3. Khoảng trống của literature review

Các survey trước thường chỉ tập trung vào một trong các phạm vi sau: machine learning cho vulnerability detection, LLM cho toàn bộ software engineering, hoặc automated program repair nói chung. Bài này tập trung riêng vào LLM cho cả detection và repair, đồng thời phân tích cách model được adaptation ở từng task.

## 4. Hình thức hóa bài toán

### 4.1. Vulnerability detection

Vulnerability detection thường được hình thức hóa như bài toán phân loại nhị phân. Với function mã nguồn đầu vào $C_i$, model dự đoán nhãn $Y_i$:

$$
Y_i \in \{0,1\}
$$

Trong đó $Y_i = 1$ biểu thị function vulnerable và $Y_i = 0$ biểu thị function non-vulnerable.

### 4.2. Vulnerability repair

Vulnerability repair được hình thức hóa như bài toán sequence-to-sequence:

$$
C_v \rightarrow C_r
$$

Trong đó $C_v$ là vulnerable code snippet và $C_r$ là repaired code do LLM sinh ra. Một patch tốt cần sửa được nguyên nhân vulnerability, giữ lại hành vi đúng của chương trình và lý tưởng nhất là vượt qua các test case. Vì có thể tồn tại nhiều patch đúng, so sánh chuỗi output với một reference patch duy nhất là chưa đủ.

## 5. Phương pháp systematic literature review

### 5.1. Research questions

Bài báo sử dụng bốn RQ:

- **RQ1:** What LLMs have been utilized to solve vulnerability detection and repair tasks?
- **RQ2:** How are LLMs adapted for vulnerability detection?
- **RQ3:** How are LLMs adapted for vulnerability repair?
- **RQ4:** What are the characteristics of the datasets and deployment strategies in LLM-based vulnerability detection and repair studies?

Ba RQ đầu tập trung vào model construction; RQ4 mở rộng sang data preparation và deployment.

### 5.2. Search strategy

Tác giả tìm kiếm trong các venue thuộc software engineering, AI và security.

**13 hội nghị:** ICSE, ESEC/FSE, ASE, ISSTA, CCS, IEEE S&P, USENIX Security, NDSS, AAAI, IJCAI, ICML, NIPS và ICLR.

**4 tạp chí:** TOSEM, TSE, TDSC và TIFS.

Bên cạnh manual search, tác giả automated search trên 7 database:

- IEEE Xplore;
- ACM Digital Library;
- SpringerLink;
- Wiley;
- ScienceDirect;
- Web of Science;
- arXiv.

Search string được xây dựng từ các bài liên quan tìm thấy trong manual search. Phụ lục trực tuyến chứa bộ từ khóa đầy đủ.

### 5.3. Study selection

Quy trình lựa chọn được mô tả qua các bước:

1. Tìm kiếm trong 17 venue và 7 database.
2. Lọc các bài ngắn hơn 5 trang và loại duplicate, còn 1.332 bài.
3. Kiểm tra venue, title và abstract, còn 212 bài.
4. Đọc full text để loại bài không dùng LLM, không làm source-code vulnerability detection/repair hoặc chỉ nhắc tới LLM như future work, còn 82 bài.
5. Quality assessment, còn 42 bài.
6. Forward/backward snowballing từ các bài đã chọn, thu thêm 83 bài để kiểm tra và bổ sung 16 bài.
7. Tập cuối gồm 58 primary studies.

Tiêu chí inclusion gồm: bài tiếng Anh, có full text, là full research paper được peer review, và thực sự dùng LLM cho source-code vulnerability detection hoặc repair.

Tiêu chí exclusion gồm: bài dưới 5 trang, sách, keynote, technical report, thesis, tool demo, editorial, survey, duplicate, bài chỉ dùng GNN/RNN hoặc phương pháp không phải LLM, bài về binary/protocol/network thay vì source code, và bài chỉ đề cập LLM trong thảo luận.

### 5.4. Quality assessment

Mỗi bài được chấm từ 0 đến 3 theo năm tiêu chí:

- **QAC1:** xuất bản tại venue uy tín;
- **QAC2:** có đóng góp cho cộng đồng học thuật hoặc công nghiệp;
- **QAC3:** mô tả rõ workflow và implementation;
- **QAC4:** mô tả rõ dataset, baseline và metric;
- **QAC5:** kết quả thực nghiệm có hỗ trợ lập luận chính hay không.

Ngưỡng chọn là tổng điểm ít nhất 12/15, tương đương 80%. Sau bước này có 42 bài, gồm 37 bài đã xuất bản và 5 preprint chất lượng cao.

## 6. Phân loại kiến trúc LLM

### 6.1. Encoder-only

Encoder-only chỉ sử dụng encoder của Transformer để tạo biểu diễn cho input. Nhóm này phù hợp với code understanding, representation learning và classification.

Các model được nêu gồm CodeBERT, GraphCodeBERT, CuBERT, VulBERTa, CCBERT, SOBERT và BERTOverflow.

### 6.2. Encoder-decoder

Encoder-decoder dùng encoder để xử lý input và decoder để sinh target text/code. Kiến trúc này phù hợp với code transformation và repair.

Các model gồm PLBART, T5, CodeT5, UniXcoder và NatGen.

### 6.3. Decoder-only

Decoder-only sử dụng decoder để sinh text hoặc code bằng cách dự đoán token tiếp theo. Nhóm này phù hợp với code generation, prompt-based detection và patch generation.

Các model gồm GPT-2, GPT-3, GPT-3.5, GPT-4, CodeGPT, Codex, PolyCoder, InCoder, CodeGen, Copilot, Code Llama và StarCoder.

## 7. RQ1 - Những LLM nào được sử dụng?

Trong 58 nghiên cứu, tác giả xác định **37 LLM khác nhau**. Một nghiên cứu có thể sử dụng nhiều model, nên tỷ lệ dưới đây tính theo số lượt model được sử dụng, không phải tỷ lệ số bài độc lập.

### 7.1. LLM cho vulnerability detection

Có 92 lượt sử dụng LLM trong detection:

| Model/nhóm    | Số lượt | Tỷ lệ |
| ------------- | ------: | ----: |
| CodeBERT      |      24 | 26,1% |
| GPT-3.5       |       9 |  9,8% |
| GPT-4         |       8 |  8,7% |
| CodeT5        |       8 |  8,7% |
| UniXcoder     |       7 |  7,6% |
| GraphCodeBERT |       4 |  4,3% |
| CodeLlama     |       4 |  4,3% |
| VulBERTa      |       3 |  3,3% |
| Others        |      25 | 27,2% |

Theo kiến trúc:

- encoder-only: **44/92 = 47,8%**;
- decoder-only: **22/92 = 23,9%**;
- encoder-decoder: **9/92 = 9,8%**;
- commercial LLM không công khai kiến trúc: **17/92 = 18,5%**.

CodeBERT đứng đầu vì detection chủ yếu là representation/classification, không yêu cầu model sinh patch dài.

### 7.2. LLM cho vulnerability repair

Có 45 lượt sử dụng LLM trong repair:

| Model/nhóm              | Số lượt | Tỷ lệ |
| ----------------------- | ------: | ----: |
| CodeT5                  |       7 | 15,6% |
| GPT-3.5                 |       5 | 11,1% |
| GPT-4                   |       4 |  8,9% |
| Domain-specific Seq2Seq |       4 |  8,9% |
| CodeGen                 |       3 |  6,7% |
| Others                  |      18 | 40,0% |

Theo kiến trúc:

- decoder-only: **14/45 = 31,1%**;
- encoder-decoder: **12/45 = 26,7%**;
- encoder-only: **3/45 = 6,7%**;
- commercial LLM không công khai kiến trúc: **16/45 = 35,6%**.

Repair cần sinh code nên các model có decoder được sử dụng nhiều hơn detection.

### 7.3. Top model theo Table 1

| Hạng | Detection                    | Repair                        |
| ---: | ---------------------------- | ----------------------------- |
|    1 | CodeBERT, encoder-only, 125M | CodeT5, encoder-decoder, 220M |
|    2 | GPT-3.5                      | GPT-3.5                       |
|    3 | GPT-4                        | GPT-4                         |
|    4 | CodeT5, 220M                 | Seq2seq, 60M                  |
|    5 | UnixCoder, 126M              | CodeGen, 350M đến 16,1B       |
|    6 | GraphCodeBERT, 125M          | Codex, 12B                    |
|    7 | CodeLlama, 7B đến 70B        | InCoder, 1,3B và 6,7B         |
|    8 | VulBERTa, 125M               | PLBART, 406M                  |
|    9 | RoBERTa, 125M                | UnixCoder, 126M               |
|   10 | BERT, 109M                   | CodeGPT, 124M                 |

**Kết luận RQ1:** encoder-only LLM thống trị detection; commercial LLM và decoder-only LLM nổi bật trong repair. Detection thường dùng model nhẹ không quá 126M tham số, còn repair có xu hướng dùng model lớn hơn và có khả năng sinh code.

## 8. RQ2 - Kỹ thuật adaptation cho vulnerability detection

Bài báo chia adaptation thành ba nhóm:

- fine-tuning: khoảng **73%**;
- prompt engineering: khoảng **17%**;
- retrieval augmentation: khoảng **10%**.

### 8.1. Fine-tuning

Fine-tuning dùng code sample có nhãn vulnerable/non-vulnerable để cập nhật tham số LLM. Các hướng nâng cao được chia thành năm nhóm.

#### 8.1.1. Data-centric innovations

- **Imbalanced learning:** sampling hoặc tăng trọng số loss cho lớp vulnerable hiếm.
- **Positive and Unlabeled learning:** PILOT học từ positive và unlabeled data, sinh pseudo-label và dùng mixed-supervision loss để giảm label noise.
- **Counterfactual training:** thay đổi user-defined identifier nhưng giữ cấu trúc cú pháp và ngữ nghĩa, giúp model không phụ thuộc vào tên biến hoặc tên hàm.

#### 8.1.2. Kết hợp với program analysis

Program analysis bổ sung quan hệ cấu trúc mà mô hình tuần tự có thể bỏ sót:

- Joern xây AST và Program Dependence Graph; LLM được pre-train để dự đoán control dependency ở mức statement và data dependency ở mức token.
- Program slicing giữ lại control/data dependency liên quan.
- Static source information được kết hợp với dynamic execution traces.
- Syntax-based CFG được tách thành nhiều execution path.
- Tên biến và tên hàm được chuẩn hóa thành `VAR_1`, `VAR_2`, `FUNC_1` để tăng robustness.
- Dependency-based attention mask giảm attention tới quan hệ không liên quan.

#### 8.1.3. Kết hợp với deep learning module khác

- **LLM + GNN:** GNN học graph feature từ DFG rồi kết hợp với feature hoặc hidden state của CodeBERT/LLM.
- **LLM + Bi-LSTM:** chia code thành nhiều đoạn, dùng BERT mã hóa từng đoạn, Bi-LSTM tổng hợp biểu diễn và classifier đưa ra dự đoán.

#### 8.1.4. Domain-specific pre-training

Các objective được khảo sát gồm:

- **Masked Language Modeling:** VulBERTa pre-train RoBERTa trên project C/C++ open-source.
- **Contrastive Learning:** kéo gần function tương tự, đẩy xa function khác nhau; có thể dùng dropout mask để tạo positive pair.
- **Predicting Program Dependencies:** học control dependency và data dependency.
- **Annotating Vulnerable Statements:** đánh dấu Potentially Vulnerable Statements bằng marker token hoặc đưa token liên quan lên đầu input.

#### 8.1.5. Causal learning

CausalVul xử lý vấn đề model học spurious feature như tên biến có tương quan giả với nhãn. Phương pháp tạo perturbation để nhận diện feature không bền vững, sau đó dùng causal learning và do-calculus nhằm hướng model tới quan hệ có tính nhân quả hơn.

### 8.2. Prompt engineering

Prompt engineering giữ nguyên tham số model và thiết kế input có cấu trúc. Thành phần thường gặp:

- **Task description:** mô tả mục tiêu và format output.
- **Role description:** yêu cầu model đóng vai security researcher, vulnerability scanner hoặc experienced developer.
- **Vulnerability-related information:** thêm CWE, loại vulnerability hoặc vulnerable code examples.
- **Program-analysis information:** thêm data flow, API call hoặc yêu cầu mô phỏng source-sink-sanitizer analysis.
- **Chain-of-thought:** thêm chỉ dẫn như “Let’s think step by step”.

### 8.3. Few-shot prompting

Few-shot đưa các cặp code và ground-truth label vào prompt. Một số nghiên cứu dùng 1 đến 6 ví dụ trong context window 4.096 token; nghiên cứu khác dùng hai ví dụ. Ưu điểm là model hiểu task và output format nhanh hơn, nhưng số ví dụ bị giới hạn bởi context window.

### 8.4. Retrieval-Augmented Generation

RAG mở rộng prompt bằng cách truy hồi sample hoặc knowledge phù hợp:

1. nhận code test;
2. tìm sample có nhãn hoặc vulnerability knowledge tương tự;
3. đưa kết quả retrieval vào context;
4. yêu cầu LLM đánh giá code.

Các phương pháp được nêu gồm BM25, TF-IDF, CodeBERT embedding với cosine similarity, knowledge base từ CVE và dependency được truy hồi từ call graph. Vul-RAG xây knowledge base từ thông tin nhiều chiều của CVE rồi truy hồi theo functional semantics để hỗ trợ detection và đề xuất hướng sửa.

**Kết luận RQ2:** fine-tuning là hướng phổ biến nhất, tiếp theo là prompt engineering và RAG.

## 9. RQ3 - Kỹ thuật adaptation cho vulnerability repair

Repair sử dụng:

- fine-tuning: khoảng **63%**;
- prompt engineering: khoảng **37%**.

### 9.1. Fine-tuning cho repair

#### 9.1.1. Data-centric innovations

Ngoài vulnerable code, model có thể nhận:

- AST của code;
- vulnerability description;
- vulnerable code examples từ CWE website;
- vulnerability-inducing commits;
- vulnerability-fixing commits.

Để xử lý function dài hơn giới hạn 512 subtoken của CodeT5, Fusion-in-Decoder chia function thành nhiều segment rồi đưa từng segment vào model. Một hướng khác dùng static analysis để tạo reduced code, loại bỏ phần ít quan trọng nhưng giữ lại thông tin cần thiết cho static analysis report và repair.

#### 9.1.2. Model-centric innovations

- Vulnerability query được thêm vào Transformer để tìm vulnerable code block.
- Vulnerability mask giúp query tập trung vào vùng code có nguy cơ.
- Multi-task learning cho phép model vừa sinh fix vừa tạo developer-friendly explanation.

#### 9.1.3. Domain-specific pre-training

Một số công trình pre-train model trên bug-fix corpus thông thường, sau đó fine-tune trên vulnerability-fix dataset. Đây là transfer learning, dựa trên sự tương đồng giữa bug fixing và vulnerability fixing.

#### 9.1.4. Reinforcement learning

SecureCode kết hợp:

- **CodeBLEU** làm syntactic reward;
- **BERTScore** làm semantic reward;
- **PPO** để fine-tune CodeGen2-7B.

Cách này tối ưu patch bằng reward về cấu trúc và ngữ nghĩa, thay vì chỉ học supervised loss từ reference patch.

### 9.2. Prompt engineering cho repair

#### 9.2.1. Zero-shot prompting

Prompt thường chứa:

- **Vulnerability description:** mô tả loại lỗi và yêu cầu sửa.
- **Vulnerability location:** đánh dấu dòng lỗi bằng comment hoặc `BUG:`.
- **Vulnerability semantics:** mô tả hành vi khiến chương trình dễ bị khai thác.
- **Program-analysis information:** xác định Minimum Edit Node (MEN), là common ancestor của các node bị sửa, sau đó dùng rule theo MEN để trích pattern đưa vào prompt.

#### 9.2.2. Few-shot prompting

Một số nghiên cứu cung cấp ba repair examples cho GPT-3.5/GPT-4. Một hướng khác thu hẹp input vào vùng liên quan, yêu cầu LLM tìm root cause và chọn exemplar phù hợp động từ database trước khi sinh patch.

**Kết luận RQ3:** fine-tuning chiếm khoảng 63%, prompt engineering khoảng 37% trong các nghiên cứu repair.

## 10. RQ4 - Dataset và deployment

### 10.1. Input granularity

Các mức input gồm line-level, function-level, class-level và repository-level.

Đối với detection:

- đa số nghiên cứu dùng function-level;
- chỉ 7 nghiên cứu xử lý line-level;
- không có nghiên cứu class-level;
- chỉ một nghiên cứu ban đầu khảo sát repo-level detection.

Đối với repair:

- tất cả nghiên cứu trong Table 3 dùng function-level;
- không có nghiên cứu class-level repair;
- không có nghiên cứu repo-level repair.

Giới hạn 512 token/subtoken của CodeBERT và CodeT5 phù hợp với function-level nhưng gây khó khăn khi mở rộng sang class hoặc repository. GPT-4 với context được bài mô tả tới 128k token tạo cơ hội cho repo-level analysis.

### 10.2. Label của detection dataset

Nhiều dataset dùng heuristic-based labeling:

1. lấy vulnerability-fixing commit từ nguồn như NVD;
2. gán pre-commit function trong file bị sửa là vulnerable;
3. gán function không thay đổi trong cùng file là non-vulnerable.

Cách này có thể gán nhãn sai vì function bị sửa chưa chắc là vị trí trực tiếp của vulnerability, còn function không thay đổi chưa chắc sạch. Vì vậy, detection dataset thường có noisy label và incorrect label.

### 10.3. Test case trong repair dataset

Repair dataset thường là:

- synthetic vulnerable code và fix;
- real-world vulnerable code và fix nhưng không có test case.

Synthetic data dễ tạo nhưng có thể không đại diện cho production. Real-world data không có test case thì khó xác định patch có giữ behavior và thực sự sửa lỗi hay không. Chỉ một số ít nghiên cứu có real-world data kèm test case; bài báo nêu hai nghiên cứu lần lượt đánh giá 42 và 12 sample.

### 10.4. Developer interaction và workflow

Survey xem xét model có giao tiếp với developer và có được tích hợp vào workflow hay không. Kết quả:

- rất ít detection study hỗ trợ interaction;
- một ngoại lệ sinh explanation trong quá trình detection;
- phần lớn repair study không hỗ trợ interaction;
- một nghiên cứu cung cấp explanation cho fix;
- không nghiên cứu nào trong review được tích hợp vào developer workflow; các hệ thống chủ yếu đánh giá offline trên static/historical data.

Thiếu interaction làm giảm trust vì developer không biết lý do của cảnh báo hoặc patch. Thiếu integration khiến hệ thống khó được dùng trong IDE, version control, code review hoặc CI/CD.

**Kết luận RQ4:** nghiên cứu hiện tại thiên về function/line-level, detection dùng heuristic label, repair thiếu test case và deployment chưa chú trọng developer collaboration.

## 11. Xu hướng xuất bản và một số kết quả định lượng

- Nghiên cứu sớm nhất mà tác giả xác định được xuất bản năm 2021.
- Năm 2024 chiếm **46,6%** tổng số nghiên cứu được chọn.
- ICSE là venue nổi bật nhất, chiếm **20,7%**.
- TSE chiếm 5,2%.
- FSE, EMSE, ISSTA và MSR mỗi venue chiếm 3,4%.
- TOSEM chiếm 1,7%.

Trong phần hạn chế, bài báo dùng hai kết quả state-of-the-art được trích dẫn để minh họa rằng hiệu năng chưa đủ tốt:

- vulnerability detection: **67,6% accuracy**;
- vulnerability repair: **20% accuracy**.

Đây là kết quả của các nghiên cứu cụ thể, không phải accuracy trung bình của 58 bài.

## 12. Hạn chế của lĩnh vực

### 12.1. Granularity nhỏ

Function-level và line-level bỏ qua vulnerability trải dài nhiều function, class hoặc file. Function-level repair cũng khó tạo patch cần chỉnh sửa nhiều nơi trong repository.

### 12.2. Dataset chất lượng thấp

Detection chịu ảnh hưởng của heuristic label, label noise và data contamination. Repair thường thiếu test case, khiến việc đánh giá patch correctness không đầy đủ.

### 12.3. Vulnerability phức tạp

Inter-procedural vulnerability khó hơn intra-procedural vulnerability. Model cũng gặp khó với CWE ít xuất hiện và vulnerability trải dài nhiều code unit.

### 12.4. Phụ thuộc lightweight LLM

Phần lớn nghiên cứu dùng LLM dưới 1B tham số, đặc biệt CodeBERT. Model trên 1B tham số và custom vulnerability LLM còn ít được nghiên cứu.

### 12.5. Thiếu deployment consideration

Các hệ thống chủ yếu được đánh giá offline, chưa tích hợp IDE, version control hoặc workflow của developer. Interaction, feedback và explanation cũng còn hạn chế.

### 12.6. Accuracy và robustness chưa đủ

LLM có thể thay đổi dự đoán khi code bị perturbation, đổi tên biến hoặc thay đổi cách trình bày dù semantics gần như không đổi. Điều này ảnh hưởng tới độ tin cậy trong production.

## 13. Roadmap nghiên cứu

### 13.1. Stage 1 - Nghiên cứu từng module còn thiếu

#### Cơ hội 1: High-quality detection test set

Thay vì làm sạch toàn bộ dataset lớn, cộng đồng có thể xây test set nhỏ nhưng được expert kiểm tra. Các sample đã xác minh từ nhiều nghiên cứu có thể được hợp nhất và cập nhật thành living benchmark.

#### Cơ hội 2: Repo-level detection và repair

Cần phát triển model xử lý dependency xuyên file, nhiều function và kiến trúc repository. Context window lớn của LLM hiện đại tạo điều kiện cho hướng này.

Nghiên cứu repo-level được bài nhắc tới so sánh Code Llama với SAST như CodeQL: SAST có detection rate thấp hơn nhưng false positive thấp hơn; LLM phát hiện nhiều vulnerability hơn nhưng false positive cao hơn.

#### Cơ hội 3: Customized vulnerability LLM

CodeBERT, CodeT5 và GPT-3.5 chưa khai thác đầy đủ vulnerability corpus. Tác giả đề xuất phát triển các model chuyên biệt, mở nguồn và minh bạch hơn. vulnGPT và Microsoft Security Copilot được nêu như các nỗ lực ban đầu, nhưng chi tiết của các hệ thống proprietary chưa được công khai đầy đủ.

#### Cơ hội 4: Advanced LLM usage

Các hướng còn ít được nghiên cứu trong vulnerability detection/repair gồm:

- LLM agent để chia task phức tạp;
- external tools như search engine, database và program-analysis tool;
- iterative RAG;
- recursive RAG;
- adaptive RAG.

#### Cơ hội 5: Deployment-ready features

Cần bổ sung real-time developer feedback, explanation, giao tiếp tự nhiên, IDE integration và version-control integration.

### 13.2. Stage 2 - Kết hợp các module

Sau khi từng module được nghiên cứu riêng, có thể kết hợp:

- customized vulnerability LLM với fine-tuning hoặc prompting;
- expert-verified dataset với test case và repair model;
- repo-level model với RAG và developer interaction;
- vulnerability-specific LLM với agent và IDE integration.

### 13.3. Stage 3 - Hệ thống thế hệ mới

Mục tiêu dài hạn là hệ thống có thể detection và repair ở line-level, method-level, class-level và repo-level, sử dụng expert-annotated benchmark, tương tác với developer, có accuracy và robustness cao, đồng thời cung cấp insight đáng tin cậy.

## 14. Đánh giá phương pháp luận

### 14.1. Điểm mạnh

- Xây dựng bốn RQ rõ ràng, bao phủ model, adaptation, data và deployment.
- Kết hợp manual search, automated search, full-text screening, quality assessment và snowballing.
- Phân biệt rõ detection với repair, thay vì gom hai task thành một bài toán chung.
- Phân loại kỹ thuật theo giai đoạn data preparation, model design, model training và training optimization.
- Chỉ ra khoảng cách giữa điểm số offline và khả năng triển khai thực tế.
- Đưa ra roadmap theo ba giai đoạn có thứ tự phát triển.

### 14.2. Điểm cần thận trọng

- Các tỷ lệ model được tính theo lượt sử dụng; một bài có thể dùng nhiều model.
- Các kết quả hiệu năng đến từ nhiều dataset, split, prompt và metric khác nhau, nên không thể dùng để xếp hạng tuyệt đối.
- “LLM” trong bài bao gồm cả model code tương đối nhỏ như BERT, CodeBERT và CodeT5; không có đồng thuận về ngưỡng số tham số.
- Số lượng bài ở các bước lọc khác nhau không nên bị diễn giải như các tập độc lập để cộng trực tiếp.
- Kết quả repair cần test case vì nhiều patch khác nhau có thể cùng đúng; metric dựa trên reference patch đơn lẻ có thể đánh giá thiếu.

### 14.3. Threats to validity

Rủi ro chính là bỏ sót bài liên quan do terminology của LLM, vulnerability detection và vulnerability repair không thống nhất. Tác giả giảm rủi ro bằng cách:

- tìm thủ công ở 13 conference và 4 journal;
- automated search trên 7 database;
- dùng search string được xây từ các bài liên quan;
- forward/backward snowballing;
- manual full-text screening và quality assessment.

Tuy nhiên, selection bias, publication bias và sự phụ thuộc vào chất lượng báo cáo của primary study vẫn có thể tồn tại.

## 15. Bài học áp dụng cho nghiên cứu mới

1. Tách riêng protocol cho detection và repair.
2. Ghi rõ model, kiến trúc, số tham số, context limit và inference setting.
3. Chia dữ liệu theo repository, commit hoặc thời gian để giảm leakage.
4. Dùng expert-verified test set thay vì chỉ dựa vào heuristic labels.
5. Với repair, cung cấp test case và kiểm tra behavior preservation.
6. Đánh giá nhiều granularity, không chỉ function-level.
7. Kiểm tra robustness với đổi tên biến, formatting, perturbation và out-of-distribution code.
8. Đánh giá explanation correctness, interaction và workflow integration.
9. Không so sánh trực tiếp F1/accuracy từ các nghiên cứu có dataset và protocol khác nhau.
10. Kết hợp LLM với program analysis, retrieval và dynamic validation khi hướng tới triển khai thực tế.

## 16. Kết luận

Bài báo của Xin Zhou và cộng sự cung cấp một SLR có hệ thống về LLM cho vulnerability detection và vulnerability repair. Survey cho thấy detection chủ yếu sử dụng encoder-only model nhẹ như CodeBERT, trong khi repair cần model có khả năng sinh code như CodeT5, CodeGen, InCoder và các commercial LLM.

Fine-tuning là kỹ thuật phổ biến nhất, nhưng các hướng data-centric innovation, program analysis integration, GNN/Bi-LSTM, domain-specific pre-training, causal learning, prompt engineering, RAG, model-centric repair và reinforcement learning đều đã được nghiên cứu ở các mức độ khác nhau.

Khoảng cách lớn nhất không chỉ nằm ở model mà còn ở dữ liệu và triển khai. Dataset detection thường có heuristic label; dataset repair thường thiếu test case; input chủ yếu ở function-level; repo-level và class-level còn trống; các hệ thống chưa được tích hợp vào workflow hoặc tương tác thường xuyên với developer.

Vì vậy, hướng phát triển quan trọng là xây benchmark expert-annotated có test case, mở rộng từ function lên repository, kết hợp LLM với program analysis và external tools, kiểm tra robustness, đồng thời thiết kế hệ thống có thể cộng tác với developer. Thành công của LLM trong lĩnh vực này cần được đo bằng khả năng phát hiện đúng, sửa đúng, giải thích đáng tin cậy và hoạt động hiệu quả trong quy trình phát triển thực tế, không chỉ bằng một điểm accuracy trên benchmark nhỏ.

## 17. Các nghiên cứu và kỹ thuật tiêu biểu được bài báo nhắc đến

- **CodeBERT, GraphCodeBERT, VulBERTa, CodeT5, CodeGen, InCoder, GPT-3.5 và GPT-4:** các model đại diện cho các kiến trúc và quy mô khác nhau.
- **PILOT:** positive and unlabeled learning cho detection.
- **VulBERTa:** masked language model pre-training cho C/C++.
- **CausalVul:** causal learning để giảm spurious correlation.
- **CSGVD và DFEPT:** kết hợp LLM với graph/data-flow representation.
- **PTLVD:** program slicing và Transformer cho line-level detection.
- **Vul-RAG:** knowledge-level retrieval augmentation.
- **SecureCode:** reinforcement learning với CodeBLEU, BERTScore và PPO cho repair.
- **Fusion-in-the-Decoder:** chia function dài thành nhiều segment.
- **NAVRepair:** dùng Minimum Edit Node và program-analysis information trong prompt repair.
- **VulEval:** hướng repo-level evaluation.
- **DeepCode AI Fix, VulRepair, SeqTrans, VulRep và AIBugHunter:** các hướng vulnerability repair hoặc hỗ trợ repair.

Báo cáo này phản ánh nội dung của bài báo trong PDF được cung cấp. Những con số hiệu năng cụ thể cần được đọc cùng primary study tương ứng vì survey không thực hiện lại tất cả thí nghiệm trong cùng một điều kiện.
