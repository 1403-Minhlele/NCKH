# STUDY REPORT: CoTVD

Bản báo cáo này được xây dựng dựa trên nội dung của [paper_extract.txt](paper_extract.txt). Nội dung dưới đây phản ánh đúng các ý chính, phương pháp, thí nghiệm và kết luận được trình bày trong bài báo, không thêm suy đoán ngoài dữ liệu của bài báo.

## 1. Thông tin bài báo

- Tên bài báo: COTVD: A function-level vulnerability detection framework using chain-of-thought reasoning with large language models
- Tác giả: Yinan Chen, Xiangping Chen, Yuan Huang, Changlin Yang, Lei Yun
- Tạp chí: Information and Software Technology
- Năm/ấn phẩm: 2026
- Mã DOI: https://doi.org/10.1016/j.infsof.2026.108043
- Dữ liệu mở: https://github.com/AFE23-u/CoTVD

## 2. Tóm tắt bài báo

Bài báo đặt ra vấn đề rằng các phương pháp phát hiện lỗ hổng phần lớn chỉ tập trung vào việc dự đoán mẫu có lỗi hay không, nhưng không cung cấp giải thích chi tiết. Điều này khiến người phát triển phải tự tái dựng nguyên nhân của lỗ hổng, tạo gánh nặng lớn trong thực tế.

Để giải quyết vấn đề, bài báo đề xuất CoTVD, một phương pháp phát hiện lỗ hổng ở mức hàm dựa trên mô hình ngôn ngữ lớn (LLM). CoTVD sử dụng Chain-of-Thought (CoT) để hướng LLM phân tích dữ liệu và điều kiện điều khiển liên quan đến các hàm thư viện nhạy cảm. Mục tiêu là không chỉ phát hiện lỗ hổng mà còn giải thích rõ nguyên nhân.

Các mô hình LLM được đánh giá bao gồm GPT-4o-128K, GPT-3.5-Turbo, Gemini-1.5-Pro, Claude-3.5-Sonnet, Llama-3.1-405B, Qwen2-72B-Instruct-T và DeepSeek-67B-T. Kết quả thực nghiệm cho thấy CoTVD dựa trên GPT-4o-128K có kết quả tốt nhất, đạt recall 94.77%.

Bài báo cũng chỉ ra rằng CoTVD có xu hướng tạo ra nhiều false positive vì nó nhạy với các rủi ro tiềm ẩn, không chỉ các lỗ hổng truyền thống mà còn cả các rủi ro như rò rỉ thông tin. Nghiên cứu tiếp tục tinh chỉnh nhãn dữ liệu và tiến hành đánh giá thực tế với 10 chuyên gia. Kết quả cho thấy, khi có hỗ trợ từ CoTVD, mỗi người đánh giá báo cáo phát hiện thêm trung bình 1.7 mẫu bị lỗ hổng và 1.1 dòng mã có rủi ro.

## 3. Bối cảnh và động lực nghiên cứu

### 3.1. Vấn đề với các phương pháp truyền thống

Bài báo nhấn mạnh rằng:

- Các phương pháp học sâu truyền thống thường chỉ đưa ra nhãn nhị phân hoặc điểm quan trọng ở mức dòng.
- Giải thích được tạo ra thường là hậu nghiệm (post-hoc) và mô tả, thiếu lập luận rõ ràng về cách lỗ hổng xuất hiện từ tương tác giữa data flow và control flow.
- Điều này làm tăng gánh nặng cho người phát triển khi phải tự suy luận lại nguyên nhân.

### 3.2. Vị trí của LLM trong phát hiện lỗ hổng

Bài báo cho rằng LLM có khả năng suy luận và tạo ra giải thích ngôn ngữ tự nhiên khi được hướng dẫn đúng cách. Do đó, CoTVD được đề xuất như một framework dựa trên LLM, tránh chỉ dự đoán nhãn mà còn làm rõ “vì sao” có lỗ hổng.

## 4. Tổng quan về framework CoTVD

Theo bài báo, CoTVD tập trung vào mã C/C++ có hàm thư viện nhạy cảm về bảo mật và sử dụng Joern để trích xuất dependency slice. Dependency slice nắm các thông tin quan trọng về data dependency và control dependency xung quanh các hàm thư viện nhạy cảm.

Các thành phần chính của prompt trong CoTVD bao gồm:

1. Global prompt
2. Source code context
3. Dependency slice
4. Reasoning instructions
5. Label prompt

Mục tiêu của thiết kế này là hướng LLM phân tích từng bước theo cách giống người kiểm toán mã, thay vì chỉ nhận là nhị phân.

## 5. Tài liệu và bộ dữ liệu nghiên cứu

### 5.1. Nguồn dữ liệu

Bài báo lấy dữ liệu từ:

- Devign
- ReVeal

Cả hai đều được xây dựng từ các dự án C/C++ thực tế.

- Devign được thu thập từ bốn dự án C lớn: Linux kernel, QEMU, Wireshark và FFmpeg.
- ReVeal bao phủ hai dự án thực tế lớn: Linux Debian kernel và Chromium.

### 5.2. Dữ liệu nhạy cảm với hàm thư viện

Bài báo quan sát rằng nhiều lỗ hổng thực tế xảy ra khi gọi các hàm thư viện hoặc API C/C++ nhạy cảm với bảo mật. Những hàm này thường liên quan tới các kiểu lỗ hổng phổ biến như:

- buffer overflows
- memory corruption
- improper input handling

Các ví dụ điển hình nêu trong bài báo bao gồm getenv, strncpy, malloc, và nhiều hàm khác.

### 5.3. Sử dụng dependency slice như điểm neo cho phân tích

Bài báo cho rằng các mẫu chứa lời gọi tới các hàm thư viện C/C++ nhạy cảm được chọn để làm đầu vào phân tích. Lý do:

- cung cấp tiêu chí cắt lát rõ ràng
- cho phép trích xuất data-flow và control-flow dependency bằng phân tích tĩnh
- giúp CoTVD thực hiện suy luận theo từng bước trên các đường thực thi dễ bị lỗ hổng

## 6. Thiết kế CoTVD

### 6.1. Dataset collection and processing

Theo bài báo, quá trình nghiên cứu tập trung vào các mẫu có chứa lời gọi đến hàm thư viện C/C++. Dữ liệu sau khi lọc đã tạo ra 3,435 mẫu dương và 6,018 mẫu âm. Sau đó, do giới hạn chi phí suy luận của LLM, các mẫu được trộn và ngẫu nhiên chọn 1/10 làm tập kiểm thử, dẫn tới 344 mẫu dương và 602 mẫu âm.

### 6.2. Dependency extraction bằng Joern

Bài báo cho thấy CoTVD sử dụng Joern, một framework phân tích tĩnh theo truy vấn, dựa trên Code Property Graphs (CPGs).

Joern giúp:

- kết hợp abstract syntax trees, control-flow graphs và data-flow graphs
- thực hiện program dependence analysis
- trích xuất dependency slices nhỏ gọn, tập trung vào các đường thực thi quan trọng và loại bỏ mã không liên quan

Theo mô tả của thuật toán trong bài báo, quy trình là:

1. Khởi tạo tập rỗng S để lưu các câu lệnh dependency đã trích xuất.
2. Tạo danh sách L chứa các hàm thư viện/API nhạy cảm như printf, getenv.
3. Xác định các lời gọi hàm trong sample F phù hợp với danh sách L.
4. Với mỗi lời gọi nhạy cảm, trích xuất các biến tham số.
5. Dùng Joern để trích xuất backward data dependency ảnh hưởng tới biến tham số.
6. Dùng Joern để trích xuất control dependency quyết định việc lời gọi có được thực thi hay không.
7. Tổng hợp và sắp xếp lại theo thứ tự thực thi của chương trình.

Mục tiêu của bước này là xây dựng dependency slice thể hiện context quan trọng liên quan tới lời gọi nhạy cảm, nhằm giảm nhiễu và tăng tính giải thích của LLM.

### 6.3. Prompt design của CoTVD

Bài báo mô tả prompt gồm 5 thành phần và cho thấy mục tiêu không chỉ là cung cấp thêm bối cảnh, mà là bắt LLM thực hiện phân tích tuần tự và mạch lạc như một người kiểm toán mã.

Prompt gồm:

- Global prompt: giao cho LLM vai trò “code auditor”
- Dependency slice: cho LLM biết các đoạn mã quan trọng đã được trích xuất từ data và control dependency
- Instructions: yêu cầu LLM tập trung vào các lời gọi hàm thức nhạy cảm, theo dõi data flow và control flow
- Label prompt: yêu cầu LLM phải phân tích kỹ trước khi đưa ra nhãn

Mẫu prompt trong bài báo như sau:

1. # Global Prompt
2. You are a code auditor tasked with reviewing the following C/C++ code. Your goal is to analyze the code and identify any vulnerabilities or security flaws.
3. # Code slice extracted: {dependencies}
4. # Instructions
5. 1. Analyze the provided code carefully. Focus on the function calls {func_list} in the slice and consider how they interact with the surrounding code.
6. 2. Pay attention to how data is passed to and from the function calls and how the control flow is managed around them.
7. # Label Prompt
8. You must first thoroughly analyze the code. Only after completing the analysis should you provide your detection result:
9. - If no vulnerabilities are found, output: ‘Label:0’
10. - If vulnerabilities are found, output: ‘Label:1’

Bài báo cho rằng cách thiết kế prompt này giúp LLM thực hiện reasoning có cấu trúc, tương ứng với Chain-of-Thought và tăng tính giải thích.

## 7. Thiết kế thí nghiệm và đánh giá

### 7.1. Môi trường thí nghiệm

Bài báo cho biết tất cả thí nghiệm chạy trên cùng môi trường phần cứng và phần mềm để đảm bảo so sánh công bằng.

- CPU: Intel(R) Xeon(R) Gold 6348 CPU
- GPU: NVIDIA A800 (80 GB)
- Hệ điều hành: Ubuntu 20.04 LTS
- Python: 3.7
- Static analysis: Joern
- Temperature sampling: 0.7

Các mô hình LLM được đánh giá gồm cả thương mại và mã nguồn mở:

- GPT-4o-128K
- GPT-3.5-Turbo
- Gemini-1.5-Pro
- Claude-3.5-Sonnet
- Llama-3.1-405B
- Qwen2-72B-Instruct-T
- DeepSeek-67B-T

### 7.2. Chỉ số đánh giá

Bài báo sử dụng các chỉ số sau:

- Number of Detected Positive Samples: số mẫu được xác định đúng là dương
- Precision: tỉ lệ các mẫu dương được phát hiện là đúng trong tổng số mẫu được mô hình gán nhãn dương
- Recall: tỉ lệ các mẫu dương thực tế mà mô hình phát hiện được
- F1-score: trung bình điều hòa giữa precision và recall

Công thức theo bài báo:

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 = 2 × Precision × Recall / (Precision + Recall)

## 8. Kết quả thử nghiệm theo RQ

### 8.1. RQ1: So sánh hiệu quả giữa CoTVD và mô hình học sâu truyền thống

Bài báo báo cáo các thống kê sau:

| Model                | Precision | Recall | F1-score | #Detected positive samples |
| -------------------- | --------: | -----: | -------: | -------------------------: |
| GPT-4o-128K          |     39.09 |  94.77 |    0.553 |                        326 |
| GPT-3.5-Turbo        |     35.49 |  63.66 |    0.456 |                        219 |
| Gemini-1.5-Pro       |     38.11 |  88.08 |    0.532 |                        303 |
| Claude-3.5-Sonnet    |     34.04 |  69.77 |    0.458 |                        240 |
| Llama-3.1-405B       |     29.09 |  60.46 |    0.393 |                        208 |
| Qwen2-72B-Instruct-T |     35.03 |  65.99 |    0.458 |                        227 |
| DeepSeek-67B-T       |     46.91 |  11.04 |    0.179 |                         38 |
| ReVeal               |     33.19 |  70.05 |    0.450 |                        241 |
| Devign               |     31.10 |  64.82 |    0.420 |                        223 |
| LineVul              |     53.30 |  56.97 |    0.551 |                        196 |

Theo bài báo:

- GPT-4o-128K-based CoTVD cho kết quả tốt nhất với F1-score 0.553, precision 39.09%, recall 94.77%.
- Gemini-1.5-Pro xếp thứ hai với recall 88.08% và F1-score 0.532.
- DeepSeek-67B-T xếp cuối với recall 11.04% và F1-score 0.179.
- So với các mô hình học sâu truyền thống như ReVeal và Devign, CoTVD cải thiện đáng kể recall. Cụ thể, CoTVD dựa trên GPT-4o-128K phát hiện 85 và 103 mẫu dương nhiều hơn ReVeal và Devign tương ứng.
- LineVul có precision cao nhất (53.30%), nhưng recall thấp hơn nhiều so với GPT-4o-based CoTVD.

Kết luận phần này: CoTVD có hiệu quả trong phát hiện lỗ hổng ở mức hàm và tốt hơn mô hình học sâu trong recall, đồng thời cung cấp tính giải thích cao hơn.

### 8.2. RQ2: Đóng góp của từng thành phần trong CoTVD

Bài báo thực hiện ablation study trên mô hình GPT-4o-128K để phân tách hai thành phần chính:

- Dependency Slice
- Chain-of-Thought instructions

Các biến thể thực nghiệm gồm:

- GPT-4o-128K (full CoTVD)
- GPT-4o-w/o-Slice
- GPT-4o-w/o-CoT

Kết quả được mô tả trong bảng sau:

| Model            | Precision | Recall | F1-score |
| ---------------- | --------: | -----: | -------: |
| GPT-4o-128K      |     39.09 |  94.77 |    0.553 |
| GPT-4o-w/o-Slice |     37.18 |  92.44 |    0.530 |
| GPT-4o-w/o-CoT   |     36.56 |  94.48 |    0.527 |

Theo bài báo:

- Full CoTVD đạt hiệu suất tốt nhất.
- Khi bỏ dependency slice, hiệu năng giảm rõ rệt trên mọi chỉ số, cho thấy dependency slice đóng vai trò quan trọng trong việc giúp mô hình xác định các đường thực thi có nguy cơ.
- Khi bỏ CoTVD instructions nhưng giữ dependency slice, recall vẫn tương đối cao nhưng precision và F1-score giảm. Điều này cho thấy reasoning theo bước giúp giảm false positive.

Kết luận: cả dependency slice và CoTVD instructions đều quan trọng; dependency slice cung cấp ngữ cảnh, CoT instructions hướng mô hình suy luận có hệ thống.

### 8.3. RQ3: Giá trị thực tế của CoTVD

Bài báo thiết kế một khảo sát thực tế với 10 chuyên gia có ít nhất 5 năm kinh nghiệm C/C++. Họ được chia thành hai nhóm:

- Source code group: chỉ xem mã nguồn
- CoTVD group: xem cả mã nguồn và phân tích CoTVD

Mỗi người làm 10 mẫu ở mỗi nhóm. Họ phải:

- xác định có hay không lỗ hổng
- nếu có, chỉ ra số dòng lỗi
- ghi lại thời gian hoàn thành

Kết quả được thể hiện trong bảng sau:

| Group       | Vulnerabilities Correct line | Average time (s) |
| ----------- | ---------------------------: | ---------------: | ----- |
| Source Code |                          6.4 |              8.8 | 577   |
| CoTVD       |                          8.1 |              9.9 | 441.5 |

Theo văn bản:

- Trong nhóm CoTVD, người đánh giá phát hiện trung bình 8.1 mẫu có lỗ hổng, cao hơn 1.7 so với nhóm chỉ xem source code.
- Về vị trí dòng lỗi, nhóm CoTVD xác định trung bình 9.9 dòng đúng, so với 8.8 dòng trong nhóm source code.
- Thời gian trung bình giảm từ 577s xuống 441.5s.

Kết luận của bài báo: CoTVD cải thiện khả năng phát hiện, giúp định vị lỗi tốt hơn và giảm thời gian khảo sát, từ đó tăng giá trị thực tế của công cụ trong môi trường phát triển thực tế.

## 9. Kết luận thực nghiệm và phát hiện chính

### 9.1. CoTVD làm tăng chất lượng phân tích thực tế

Bài báo cho rằng các phân tích bằng ngôn ngữ tự nhiên do CoTVD cung cấp giúp người phát triển cải thiện độ bao phủ và độ chính xác trong phát hiện lỗ hổng. Các chuyên gia nhận ra nhiều mẫu nguy cơ hơn khi được hỗ trợ bởi CoTVD.

### 9.2. CoTVD nhạy với rủi ro tiềm ẩn hơn so với lỗ hổng truyền thống

Bài báo chỉ ra rằng CoTVD đánh dấu nhiều mẫu âm như dương vì mô hình nhạy với các nguy cơ bảo mật tiềm ẩn, không chỉ những rủi ro dẫn trực tiếp tới lỗ hổng mà còn cả:

- rò rỉ thông tin
- xử lý lỗi không phù hợp
- thiếu kiểm tra trạng thái đối tượng hoặc tài nguyên
- phụ thuộc vào thông tin bên ngoài không xác định
- các rủi ro thời gian chạy hoặc đa luồng

Tuy những nguy cơ này không nhất thiết là lỗ hổng trực tiếp theo nhãn dataset, nhưng chúng cho thấy CoTVD có xu hướng cảnh báo nhiều rủi ro hơn so với nhãn gốc.

## 10. Thảo luận về hiệu quả và tính thực tiễn của dependency slicing

Bài báo đưa ra phân tích về sự đánh đổi giữa độ chính xác và hiệu quả thực tế khi kết hợp phân tích tĩnh với LLM.

### 10.1. Giảm input tokens

Bài báo cho thấy khi thay toàn bộ hàm bằng dependency slice được bổ sung hướng dẫn, số token đầu vào giảm từ 900.04 xuống 328.94 trên 946 mẫu, tương ứng giảm 571.10 token, khoảng 63.45%.

Theo bài báo, đây là lợi ích quan trọng vì:

- giảm nhiễu trong ngữ cảnh đầu vào
- giảm nguy cơ hallucination do mã không liên quan
- giảm chi phí token và tăng khả năng triển khai thực tế

### 10.2. Độ trễ suy luận với mô hình nguồn mở

Bài báo đo thời gian suy luận của các mô hình nguồn mở khi chạy dưới CoTVD. Kết quả:

| Model                | Parameters | Avg. inference time (s/sample) |
| -------------------- | ---------: | -----------------------------: |
| Qwen2-72B-Instruct-T |        72B |                            5.8 |
| DeepSeek-67B-T       |        67B |                            5.2 |

Kết hợp thiết bị 4 × NVIDIA A80 (80 GB).

Theo bài báo, mặc dù các mô hình nguồn mở có hiệu năng thấp hơn mô hình thương mại, thời gian suy luận cho thấy CoTVD có thể triển khai trong CI/CD theo chế độ batch hoặc bất đồng bộ ở mức chấp nhận được.

## 11. Ví dụ giải thích có tính khả năng diễn giải

Bài báo trình bày một ví dụ bằng đoạn mã sử dụng memcpy và minh họa cách CoTVD đưa ra lập luận theo bước:

- Step 1: Identify security-sensitive function calls.
- Step 2: Analyze data dependencies.
- Step 3: Analyze control dependencies.
- Step 4: Vulnerability conclusion.

Ví dụ này cho thấy CoTVD không chỉ cho nhãn mà còn giải thích:

- có hàm memcpy nhạy cảm
- add_len được truyền trực tiếp như số byte sao chép
- có khả năng mismatch giữa kích thước vùng nhớ và độ dài sao chép
- khả năng dẫn tới heap-based buffer overflow

Đây là cái mà bài báo gọi là “interpretable vulnerability reasoning”.

## 12. Vì sao nhiều mẫu âm bị CoTVD gán nhầm là dương?

Bài báo phân loại các false positive vào bốn nhóm chính:

### #1. Rủi ro liên quan đến print statements

Nếu print statement xuất dữ liệu nhạy cảm, CoTVD đánh giá đây là nguy cơ rò rỉ thông tin và gán nhãn dương.

### #2. Xử lý lỗi không phù hợp

Nếu lỗi được in ra bằng printf rồi exit, CoTVD cho rằng đây là cách xử lý không phù hợp trong nhiều bối cảnh, và có thể đánh dấu là positive.

Ví dụ bài báo đưa ra một đoạn như:

- printf("out of memory");
- exit(U_MEMORY_ALLOCATION_ERROR);

CoTVD nhận xét đây là cách xử lý lỗi không tối ưu và xem đó là rủi ro cho code design.

### #3. Rủi ro phụ thuộc vào thông tin bên ngoài chưa biết

Khi behavior của hàm phụ thuộc vào thông tin bên ngoài không có trong dependency slice (ví dụ: biến cấu hình, environment, logic của hàm chưa giải quyết), CoTVD có xu hướng cảnh báo quá mức và đánh dấu positive.

Bài báo nêu ví dụ về các trường hợp như:

- hàm gọi llstr, dynstr_append, memcmp với các biến hoặc hằng chưa xác định
- việc kiểm tra chỉ số array, biến không xác định hoặc thông tin đầu vào chưa rõ

CoTVD có thể kết luận “nên kiểm tra điều kiện nếu không an toàn” và gán Label: 1.

### #4. Rủi ro phụ thuộc runtime unknowns

Trong các trường hợp cực hiếm, CoTVD cho rằng trong môi trường đa luồng, việc truy cập cùng biến có thể dẫn tới race condition và đánh dấu positive.

## 13. Cải thiện độ chính xác sau khi “sửa” false positive

Bài báo cho biết họ đã “corrected” 459 mẫu false positive do CoTVD tạo ra. Những mẫu này ban đầu bị gán nhãn positive nhưng sau khi điều chỉnh trở thành negative. Kết quả cho thấy:

- precision tăng từ 39.09% lên 86.94%
- F1-score tăng từ 0.530 lên 0.907

Bài báo giải thích đây là do CoTVD rất nhạy cảm với các rủi ro tiềm ẩn trong mã và có xu hướng over-detect. Tuy nhiên, theo lập luận của tác giả, đây cũng cho thấy CoTVD có giá trị trong việc phát hiện các thiết kế rủi ro tiềm ẩn mà dataset gốc chưa dán nhãn đầy đủ.

## 14. Threats to validity

### 14.1. Internal validity threats

Bài báo liệt kê các mối đe dọa nội bộ:

- Dataset Bias: tập dữ liệu chỉ tập trung vào mẫu C/C++ có lời gọi hàm thư viện. Chưa được đánh giá trên Java, Python hoặc ngôn ngữ khác.
- Prompt Design Bias: prompt của CoTVD bao gồm nhiều phần; bất kỳ thiết kế không phù hợp nào cũng có thể gây khác biệt hiệu năng.
- Reliability of the Joern: nếu Joern extract sai, toàn bộ slice và phân tích sẽ bị ảnh hưởng. Để giảm nguy cơ, nhóm đã kiểm tra mẫu và so sánh với các công cụ phân tích mã khác.

### 14.2. External validity threats

- Hiệu suất của CoTVD khác nhau giữa các LLM. GPT-4o-128K có hiệu quả tốt hơn, nhưng điều này có thể do khả năng thích ứng tốt hơn với CoTVD.
- Để giảm nguy cơ, bài báo triển khai CoTVD trên nhiều mô hình khác nhau.

### 14.3. Construct validity threats

- Các metrics như precision, recall và F1-score có thể không hoàn toàn phản ánh hiệu quả trong môi trường phát triển thực tế.
- Vì vậy, tác giả bổ sung đánh giá thực tế bằng chuyên gia người dùng (RQ3).

## 15. Kết luận của bài báo

### 15.1. Kết luận chính

Bài báo kết luận rằng CoTVD là một phương pháp phát hiện và phân tích lỗ hổng dựa trên LLM, là nỗ lực đầu tiên sử dụng khả năng suy luận của LLM để phân tích data dependency và control dependency cho mục đích phát hiện lỗ hổng.

CoTVD không chỉ phát hiện ở mức hàm, mà còn cung cấp giải thích về nguyên nhân tiềm ẩn của lỗ hổng. Kết quả thực nghiệm cho thấy GPT-4o-128K-based CoTVD vượt trội hơn các phương pháp học sâu truyền thống theo precision, recall và F1-score.

### 15.2. Vấn đề rủi ro tiềm ẩn và nhãn dataset

Bài báo phát hiện rằng CoTVD có độ nhạy cao đối với các rủi ro tiềm ẩn và thiết kế code không an toàn, bao gồm cả thông tin rò rỉ. Điều này cho thấy nhãn dataset hiện có có thể bỏ sót các rủi ro chưa được gán nhãn chính xác, đặc biệt khi nhãn dựa trên commit và không cần thiết phải sửa code mới cho thấy không có rủi ro.

### 15.3. Future work

Bài báo đề xuất các hướng nghiên cứu tiếp theo:

1. Nâng cấp độ phân loại nhãn dataset, ví dụ: no risk, potential risk, confirmed vulnerability.
2. Nghiên cứu cách xây dựng prompt tốt hơn, có thể có điều chỉnh động theo từng đoạn mã và mức rủi ro khác nhau.

## 16. Thông tin định danh và tài liệu đi kèm

### CRediT authorship contribution statement

- Yinan Chen: Methodology
- Xiangping Chen: Methodology
- Yuan Huang: Software
- Changlin Yang: Data curation
- Lei Yun: Methodology

### Declaration of competing interest

Theo bài báo, các tác giả không có bất kỳ mối quan hệ hoặc lợi ích tài chính cạnh tranh nào có thể ảnh hưởng tới công trình này.

### Data availability

Dữ liệu được cung cấp mở tại: https://github.com/AFE23-u/CoTVD

## 17. Các tài liệu tham khảo nổi bật được đề cập trong bài báo

Bài báo liệt kê các tài liệu từ [1] đến [58], bao gồm các nghiên cứu về:

- deep learning for vulnerability detection
- program dependence graph
- VulDeePecker
- SySeVR
- Devign
- ReVeal
- VDoTR
- CircleGGNN
- Transformer và BERT cho mã nguồn
- ChatGPT
- Chain-of-Thought prompting
- Joern
- Gemini, Claude, Llama, Qwen2, DeepSeek
- Flawfinder, Checkmarx

## 18. Kết thúc

Tổng hợp lại, bài báo tập trung vào một quan điểm chính: CoTVD không chỉ hướng tới việc gán nhãn lỗ hổng, mà còn hướng tới việc giải thích cách lỗ hổng xuất hiện qua data dependency và control dependency trong mã C/C++. Đó là điểm khác biệt lớn so với các mô hình học sâu truyền thống, đồng thời là lý do bài báo đề xuất CoTVD như một phương pháp có giá trị nghiên cứu và thực tiễn.
