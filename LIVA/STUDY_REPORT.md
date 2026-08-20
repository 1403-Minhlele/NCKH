# STUDY REPORT: LIVA

Báo cáo này được xây dựng từ bài báo [LIVA_A_Multi-Agent_LLM-Assisted_System_for_IoT_Vulnerability_Analysis.pdf](LIVA_A_Multi-Agent_LLM-Assisted_System_for_IoT_Vulnerability_Analysis.pdf) trong thư mục này. Nội dung tổng hợp các mục tiêu, thiết kế, đánh giá, kết quả và giới hạn mà bài báo trình bày.

## 1. Thông tin bài báo

- **Tên:** *LIVA: A Multi-Agent LLM-Assisted System for IoT Vulnerability Analysis*
- **Tác giả:** Zhe Yang, Hao Peng, Yanling Jiang, Jianwei Liu, Hongbin Luo, Mingsheng Tang, Jiahe Li, Kun Zhang
- **Tạp chí:** *IEEE Transactions on Dependable and Secure Computing*, tập 23, số 3
- **Thời điểm công bố:** 16/02/2026; số tháng 05–06/2026
- **DOI:** https://doi.org/10.1109/TDSC.2026.3665343
- **Mã nguồn và dữ liệu:** https://github.com/RingBDStack/LIVA
- **Từ khóa:** Internet of Things, taint analysis, LLM, lỗ hổng, fine-tuning

## 2. Tóm tắt

LIVA là hệ thống phân tích lỗ hổng web trong firmware IoT bằng phân tích taint tĩnh trên mã nhị phân. Hệ thống kết hợp phân tích ngược, cơ sở dữ liệu đồ thị và hai agent LLM để giải quyết ba điểm yếu của công cụ taint truyền thống: nhận diện source/sink chưa đầy đủ, chi phí phân tích liên thủ tục cao và nhiều cảnh báo sai do quy tắc tĩnh không hiểu đầy đủ ngữ nghĩa mã.

Agent theo dõi taint dùng Qwen3-32B đã fine-tune với 3.000 mẫu firmware thực tế; agent suy luận lỗ hổng dùng LLM thương mại để đánh giá xem một đường truyền dữ liệu có thật sự khai thác được hay không. Trên 64 firmware của 11 hãng, LIVA đạt recall **98,1%**, precision **74,6%**, phát hiện nhiều hơn SaTC 309 lỗ hổng đã biết và nhiều hơn Karonte 349 lỗ hổng. Tổng thời gian phân tích là 4.139 phút, nhanh hơn SaTC khoảng 6,7 lần và Karonte 5,6 lần. Hệ thống còn phát hiện 64 lỗ hổng chưa biết, trong đó 39 đã có mã CVE/CNVD.

## 3. Bối cảnh và vấn đề nghiên cứu

Firmware IoT thường là mã đóng, phụ thuộc phần cứng và khó mô phỏng đầy đủ. Phân tích taint tĩnh có lợi thế vì có thể trực tiếp đọc luồng lệnh nhị phân để theo dõi dữ liệu không tin cậy từ **source** (điểm nhận dữ liệu bên ngoài, chẳng hạn tham số HTTP) đến **sink** (thao tác nhạy cảm, chẳng hạn `system`, `popen`, `strcpy`).

Tuy vậy, các công cụ hiện có như SaTC, Karonte và EmTaint dựa nhiều vào luật và pattern xác định trước. Điều này gây ra các vấn đề sau:

- source rất đa dạng, đặc biệt khi không có frontend hoặc định tuyến không rõ ràng;
- sink nguy hiểm có thể bị bọc bởi nhiều lớp hàm trong shared library;
- việc lần theo từng source–sink riêng lẻ tạo nhiều lượt duyệt lặp lại;
- một đường taint đến sink chưa chắc là lỗ hổng có thể khai thác, vì có thể đã được kiểm tra độ dài hoặc lọc đầu vào.

LIVA dùng hiểu biết ngữ nghĩa của LLM để bổ sung cho phân tích tĩnh, thay vì thay thế hoàn toàn phần phân tích chương trình.

## 4. Mô hình đe dọa

Bài báo xét kẻ tấn công có thể lấy firmware, reverse engineering để hiểu web service phía sau và gửi HTTP request độc hại qua LAN hoặc Internet. Các điểm vào như đăng nhập, trang cấu hình và tải tệp được xem là source tiềm năng. Mục tiêu là phát hiện dữ liệu không tin cậy có thể lan truyền tới các thao tác backend nguy hiểm và tạo ra lỗ hổng web, như command injection hoặc memory corruption.

## 5. Kiến trúc tổng thể của LIVA

LIVA biến firmware nhị phân thành báo cáo lỗ hổng qua năm giai đoạn:

1. **Nhận diện source:** kết hợp string trong binary, vị trí tham chiếu và LLM để tìm hàm nhận input bên ngoài.
2. **Nhận diện sink:** tìm sink trực tiếp trong chương trình chính và sink bị bọc trong shared library.
3. **Phân tích luồng hàm nguy hiểm:** dùng code slicing, gom nhóm source và gộp call chain để giảm các lượt duyệt trùng lặp.
4. **Theo dõi truyền taint:** agent đã fine-tune suy luận ánh xạ tham số và đường truyền dữ liệu qua các hàm.
5. **Suy luận lỗ hổng:** agent thứ hai đánh giá tính khai thác của mỗi đường source–sink, loại bỏ các cảnh báo không phải rủi ro thực sự.

Prototype có hơn 9.000 dòng mã (xấp xỉ 7.000 Python và 2.000 Java), tích hợp IDA Pro 9.0 và Ghidra 10.4, hỗ trợ x86, ARM, MIPS và PowerPC.

## 6. Nhận diện source và sink

### 6.1. Source từ backend binary

LIVA không phụ thuộc hoàn toàn vào mã frontend. Hệ thống trích xuất string hằng từ binary (ví dụ vùng `.rodata`), tìm vị trí chúng được tham chiếu, xác định hàm gọi chứa string rồi để LLM phân loại xem lời gọi đó có mang nghĩa nhận input bên ngoài không. Cách này hữu ích khi frontend thiếu hoặc liên kết frontend–backend yếu.

Trong đánh giá, LIVA tìm 6.723 source, cao hơn 8,1% so với 6.217 của SaTC. Bài báo lưu ý rằng ở một vài firmware LIVA báo ít source hơn SaTC, nhưng kiểm tra thủ công cho thấy một phần chênh lệch là false positive của SaTC.

### 6.2. Sink trực tiếp và sink bọc

Ở chương trình chính, LIVA đối sánh lời gọi với tập sink nguy hiểm định nghĩa sẵn. Với shared library, hệ thống thu thập exported function, lọc ứng viên dựa trên đặc điểm như tham số pointer/buffer, nested call hoặc từ khóa `exec`, `auth`, `parse`, rồi dùng phân tích taint để xem hàm đó có đi tới sink đã biết không. Nếu có, hàm bọc được coi là wrapper sink.

LIVA tìm được 142 sink so với 115 của SaTC, tăng 23,5%. Lợi ích chính đến từ khả năng nhận ra wrapper function trong call chain sâu.

## 7. Tối ưu hóa phân tích taint

### 7.1. Gom nhóm source

Các source có cùng hàm cha trong call graph được gộp vào một cụm. Một lần duyệt từ cụm có thể phủ nhiều đường truyền đến sink, thay vì lặp lại việc duyệt gần giống nhau cho từng source.

Trên 15 firmware router, số source giảm từ 6.723 xuống 1.281 sau gom nhóm, tức giảm **80,95%** số đối tượng cần phân tích. Cách này tăng hiệu quả nhưng bài báo cũng ghi nhận có thể tạo false negative khi hai call site rất giống nhau bị gộp quá mức.

### 7.2. Cấu trúc ánh xạ tham số và gộp call chain

LIVA lưu quan hệ giữa biến của caller và tham số của callee, địa chỉ call site cùng đoạn mã decompile tương ứng. Bốn dạng truyền tham số được đưa vào dữ liệu fine-tune:

- qua biến cục bộ;
- qua tham số hình thức;
- qua hằng số;
- qua giá trị trả về.

Thay vì phân tích tách biệt mọi lời gọi con của cùng một hàm cha, LIVA gộp ngữ cảnh các call site để LLM suy luận trong một lượt. Kết quả là số đường nhạy cảm cần phân tích giảm từ 5.534 xuống 2.132, tương ứng **61,48%**.

## 8. Hệ multi-agent

### 8.1. Agent theo dõi taint

Đây là thành phần chính để đọc mã decompile, suy luận ánh xạ tham số và dựng quan hệ truyền dữ liệu liên thủ tục. Agent dùng Qwen3-32B fine-tune bằng QLoRA (quantization 4-bit kết hợp Low-Rank Adaptation). Đầu ra được chuẩn hóa để tự động xử lý và lưu vào Neo4j.

Neo4j chứa node hàm, node tham số/biến, quan hệ gọi hàm, quan hệ sở hữu và quan hệ truyền dữ liệu. Từ đồ thị này, hệ thống truy vấn được các đường nối source–sink.

### 8.2. Agent suy luận lỗ hổng

Một đường taint chỉ là ứng viên, không phải bằng chứng lỗ hổng. Agent suy luận nhận toàn bộ chuỗi hàm, mã decompile và ánh xạ biến; nó kiểm tra độ dài đầu vào, điều kiện biên, cơ chế lọc/validation và sink nguy hiểm để đánh giá tính khai thác.

Agent này giúp phân biệt trường hợp input không kiểm tra đi tới `system()` với đường dữ liệu đã được bảo vệ hợp lệ. Đó là cơ chế chính để giảm false positive so với chỉ áp dụng quy tắc tĩnh.

## 9. Dữ liệu, baseline và chỉ số đánh giá

Dataset đánh giá gồm **64 firmware** của **11 hãng**, lấy từ SaTC, Karonte, FirmAE, bản firmware chính thức và 15 mẫu mới bổ sung. Thiết bị gồm router, access point, switch, VPN gateway, signal amplifier và NAS; mọi mẫu đều có web service và đa dạng về kiến trúc/định tuyến.

Dataset fine-tune gồm 3.000 mẫu: chuỗi gọi có lỗ hổng đã biết và quan hệ truyền tham số là mẫu dương; hàm không lỗ hổng trong cùng codebase là mẫu âm. Tập kiểm tra LLM gồm 400 mẫu theo bốn dạng truyền tham số nói trên.

Baseline là SaTC và Karonte. Các chỉ số gồm số cảnh báo (Alerts), true positive, false negative, precision, recall và thời gian. Precision là tỉ lệ cảnh báo đúng; recall là tỉ lệ lỗ hổng thực tế được phát hiện.

## 10. Kết quả RQ1: nhận diện source/sink

Tác giả so sánh DeepSeek-V3, GPT-4o, Qwen-Max và Claude-Max trên các đoạn hàm Tenda, D-Link, Linksys. Các mô hình tương đương về source; ở sink, DeepSeek-V3 và GPT-4o có precision cao nhất, mỗi mô hình chỉ có một false positive trong thử nghiệm nhỏ này. LIVA chọn DeepSeek-V3 cho bước source/sink vì hiệu quả tương đương GPT-4o nhưng chi phí suy luận thấp hơn.

Kết quả cho thấy LIVA mở rộng độ bao phủ source và đặc biệt là wrapper sink. Tuy nhiên, sink được bọc nhiều tầng vẫn là nguồn false positive đáng kể, nhất là khi tham số bị format/chuyển kiểu làm mất ngữ nghĩa chuỗi gốc.

## 11. Kết quả RQ2 và RQ3: hiệu quả tối ưu hóa, lựa chọn LLM

Khi tăng dữ liệu huấn luyện từ 500 đến 3.000 mẫu, loss giảm và đường hội tụ ổn định hơn. Tác giả chọn **3.000 mẫu** làm quy mô fine-tune mặc định.

Thử nghiệm bốn model mở—DeepSeek-R1-Distill-Qwen-32B, DeepSeek-Coder-33B-Instruct, QwQ-32B và Qwen3-32B—cho thấy Qwen3-32B và QwQ-32B có accuracy trung bình lần lượt 97,79% và 97,91%. Qwen3-32B có thời gian xử lý ngắn nhất, vì vậy được chọn làm model nền của agent LIVA. Temperature 0,5–0,7 cho cân bằng tốt nhất giữa suy luận và ổn định.

So với LLM thương mại, LIVA dẫn đầu trên ba trong bốn loại ánh xạ tham số: 98,21% (loại 2), 97,33% (loại 3), 92,58% (loại 4); ở loại 1 chỉ thấp hơn GPT-4o một điểm phần trăm. Bài báo báo cáo model fine-tune cải thiện khoảng **3 điểm phần trăm** độ chính xác phân tích quan hệ truyền taint so với LLM thương mại và tăng hiệu quả trung bình **5,5%**.

## 12. Kết quả RQ4: so sánh phát hiện lỗ hổng

Trên tập đánh giá có 370 lỗ hổng đã xác nhận (gồm cả 64 zero-day), LIVA vượt hai baseline ở độ bao phủ, độ chính xác và thời gian:

| Công cụ | True positive | Bỏ sót | Recall | Precision | Số cảnh báo | Thời gian |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **LIVA** | 363 | 6 | **98,1%** | **74,6%** | 487 | 4.139 phút (68,9 giờ) |
| SaTC | — | 316 | 14,6% | 40,3% | 134 | 27.161 phút (452,7 giờ) |
| Karonte | — | 356 | 3,8% | 21,5% | 65 | 22.632 phút (377,2 giờ) |

LIVA phát hiện thêm 309 lỗ hổng đã biết so với SaTC và thêm 349 so với Karonte. Tỷ lệ false positive giảm 59,4% so với SaTC và 67,6% so với Karonte. Thời gian tổng thể nhanh hơn SaTC 6,7 lần và Karonte 5,6 lần.

Lưu ý: bài báo nêu LIVA phát hiện 363/370 lỗ hổng nhưng đồng thời ghi “6 misses”; hai con số này không khớp hoàn toàn về phép đếm. Báo cáo giữ nguyên các số liệu được tác giả công bố và không tự hiệu chỉnh.

## 13. Kết quả RQ5: lỗ hổng zero-day

LIVA tìm được **64** lỗ hổng chưa biết trên 15 model thiết bị IoT. Phần lớn thuộc command injection và memory corruption. Các lỗi được báo cho nhà cung cấp, được xác nhận; **39** lỗi đã có định danh CVE hoặc CNVD. Theo bài báo, các baseline chủ yếu bỏ sót những lỗi này do source/sink không đầy đủ hoặc không mô hình hóa đúng quan hệ biến giữa các hàm.

## 14. Giới hạn và nguyên nhân sai sót

- Chất lượng decompile ảnh hưởng trực tiếp đến LIVA. So với IDA, lỗi khôi phục control flow của Ghidra tác động ít hơn; lỗi suy luận kiểu và tái tạo biến làm accuracy giảm rõ, có thể còn 50–60% ở các trường hợp được khảo sát.
- LIVA có thể cảnh báo sai khi tồn tại cơ chế lọc nhưng agent không đánh giá đúng khả năng khai thác, khi source không có đường routing hợp lệ hoặc khi source được dùng lại trên nhiều route tạo cảnh báo trùng lặp.
- LIVA có thể bỏ sót luồng truyền dữ liệu qua cơ chế lưu/truy xuất dữ liệu giữa các hàm. Code decompile quá dài cũng có thể bị rút gọn làm mất câu lệnh quan trọng.
- Gom call site nhằm giảm thời gian có thể làm giảm độ chính xác ở các call site rất giống nhau.
- Hệ thống phụ thuộc vào reverse engineering và vào chất lượng suy luận của LLM; do đó kết quả thực tế có thể khác theo kiến trúc, compiler optimization và chất lượng firmware.

## 15. Kết luận

LIVA là một hướng tiếp cận lai giữa phân tích taint tĩnh và LLM multi-agent cho firmware IoT nhị phân. Phân tích chương trình đảm nhiệm việc tạo source/sink, call graph và luồng dữ liệu có cấu trúc; LLM được dùng ở các bước cần hiểu ngữ nghĩa, gồm nhận diện điểm đầu/cuối, ánh xạ tham số và xác minh khả năng khai thác.

Kết quả bài báo cho thấy cách kết hợp này tăng mạnh recall, precision và tốc độ so với SaTC và Karonte trên tập firmware đã dùng. Điểm đáng chú ý là LIVA không chỉ tăng số cảnh báo: agent suy luận còn được thiết kế để đánh giá ngữ cảnh đầy đủ của đường taint, nhờ đó giảm cảnh báo sai và tìm được các lỗ hổng zero-day.

## 16. Tài liệu tham khảo trực tiếp

1. Zhe Yang et al. (2026), *LIVA: A Multi-Agent LLM-Assisted System for IoT Vulnerability Analysis*, *IEEE Transactions on Dependable and Secure Computing*, 23(3). https://doi.org/10.1109/TDSC.2026.3665343
2. LIVA replication package: https://github.com/RingBDStack/LIVA
