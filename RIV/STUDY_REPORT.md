# STUDY REPORT: RLV

Báo cáo này được xây dựng từ bài báo [RLV- LLM-based vulnerability detection by retrieving and refining contextual information.pdf](RLV-%20LLM-based%20vulnerability%20detection%20by%20retrieving%20and%20refining%20contextual%20information.pdf) trong thư mục này. Nội dung chỉ tổng hợp các mục tiêu, phương pháp, kết quả và giới hạn được tác giả trình bày.

## 1. Thông tin bài báo

- **Tên:** *RLV: LLM-based vulnerability detection by retrieving and refining contextual information*
- **Tác giả:** Fangcheng Qiu, Zhongxin Liu, Bingde Hu, Zhengong Cai, Lingfeng Bao, Xinyu Wang
- **Tạp chí:** *The Journal of Systems & Software*, tập 235, bài 112756
- **Năm:** 2026; trực tuyến ngày 02/01/2026
- **DOI:** https://doi.org/10.1016/j.jss.2025.112756
- **Từ khóa:** phát hiện lỗ hổng, mô hình ngôn ngữ lớn (LLM), prompt engineering

## 2. Tóm tắt

RLV (*Retrieving & Refining Contextual Information for LLM-based Vulnerability Detection*) là phương pháp phát hiện lỗ hổng ở mức hàm cho mã C/C++. Điểm xuất phát của bài báo là: một hàm tách rời thường không đủ thông tin để hiểu đúng ngữ nghĩa và đánh giá an toàn. Ý nghĩa của biến, kiểu dữ liệu do dự án định nghĩa, hàm được gọi và cách hàm đó được gọi từ nơi khác có thể quyết định liệu một thao tác có gây lỗi hay không.

Thay vì chỉ đưa hàm đích vào LLM, RLV truy xuất ngữ cảnh liên quan trong repository, tinh lọc ngữ cảnh để không vượt giới hạn đầu vào, rồi kết hợp nó với hàm đích trong prompt có hướng dẫn suy luận từng bước. Mô hình nền của RLV là DeepSeek-R1; phương pháp không yêu cầu huấn luyện riêng trên dữ liệu của dự án cần kiểm tra.

Trên FFmpeg+QEMU và DiverseVul, RLV đạt F1 lần lượt là **0,6428** và **0,3258**. Khi đánh giá trên các dự án chưa từng xuất hiện trong huấn luyện, RLV đạt F1 **0,3153** trên DiverseVul, cao hơn **26,83%** so với baseline prompt-based tốt nhất theo cách tác giả báo cáo.

## 3. Vấn đề và động lực nghiên cứu

Các phương pháp học sâu hoặc fine-tuning thường học mẫu từ dữ liệu đã gán nhãn. Vì vậy, hiệu năng có thể giảm khi áp dụng cho dự án mới có phong cách lập trình, API nội bộ hoặc mẫu lỗ hổng khác dữ liệu huấn luyện. Việc fine-tune lại mô hình lớn cũng tốn tài nguyên.

Các phương pháp prompt-based tránh được chi phí huấn luyện, nhưng nếu chỉ nhận mã của một hàm, LLM khó biết:

- một hàm do người dùng định nghĩa thực hiện việc gì;
- cấu trúc hoặc kiểu dữ liệu nội bộ mang ý nghĩa gì;
- hàm đích được gọi trong bối cảnh nào;
- điều kiện an toàn có nằm ở caller/callee hay ở định nghĩa kiểu dữ liệu không.

RLV mô phỏng cách lập trình viên đọc mã: tìm định nghĩa của các thành phần chưa biết, hiểu mục đích của hàm trong bối cảnh dự án, sau đó mới đưa ra nhận định về lỗ hổng.

## 4. Ý tưởng chính của RLV

RLV xây dựng “repository knowledge” cho từng hàm đích. Tri thức này gồm ba loại thông tin:

1. **Callee:** các hàm do dự án định nghĩa được hàm đích gọi.
2. **Data type:** các kiểu dữ liệu do dự án định nghĩa xuất hiện trong hàm đích.
3. **Caller:** hàm gọi đến hàm đích; RLV chọn caller được dùng thường xuyên nhất để làm rõ mục đích sử dụng của hàm đích.

Với callee, RLV tạo chữ ký hàm bằng phân tích tĩnh và dùng LLM để sinh tóm tắt mục đích, đầu vào và đầu ra. Với data type, RLV giữ lại định nghĩa đầy đủ. Các thành phần này, cùng với mã hàm đích, tạo thành ngữ cảnh để LLM phân loại.

## 5. Quy trình phương pháp

Framework gồm ba giai đoạn.

### 5.1. Trích xuất thông tin từ hàm đích

RLV dùng Tree-sitter để lấy các callee và kiểu dữ liệu xuất hiện trong hàm. Sau đó, `gtags` và `ctags` được dùng để đối chiếu với toàn repository, phân biệt thành phần do người dùng định nghĩa với thư viện chuẩn hoặc thư viện bên thứ ba.

Tác giả tập trung vào thành phần do người dùng định nghĩa vì LLM thường đã có kiến thức tốt hơn về thư viện chuẩn/phổ biến, nhưng không thể suy ra chính xác ngữ nghĩa API và kiểu dữ liệu nội bộ của từng dự án.

### 5.2. Truy xuất và tinh lọc tri thức repository

RLV tìm định nghĩa đầy đủ của các callee, data type và caller trong repository. Không phải toàn bộ thông tin đều được đưa vào prompt vì repository quá lớn, ngay cả khi LLM có cửa sổ ngữ cảnh dài.

DeepSeek-R1 được dùng để:

- tóm tắt mục đích của hàm đích từ mã và caller được chọn;
- chọn tối đa 10 callee và 5 data type quan trọng khi số lượng thành phần lớn;
- tạo tóm tắt cho từng callee.

Việc lọc này nhằm giữ thông tin hữu ích nhất thay vì chọn ngẫu nhiên hoặc nạp cả repository.

### 5.3. Phân loại lỗ hổng

Prompt phân loại có bốn phần: hướng dẫn, tri thức repository, hàm đích và chỉ dẫn đầu ra. RLV sử dụng **zero-shot Chain-of-Thought**: trước hết yêu cầu LLM hiểu hàm nhờ ngữ cảnh đã truy xuất, sau đó suy luận về lỗ hổng và cuối cùng chỉ trả về `1` (có lỗ hổng) hoặc `0` (không có lỗ hổng).

Tác giả chọn DeepSeek-R1 vì năng lực suy luận/mã nguồn, khả năng triển khai mở và chi phí phù hợp với thí nghiệm quy mô lớn. Đây là lựa chọn thực nghiệm của bài báo, không phải khẳng định rằng nó luôn tốt nhất trong mọi bối cảnh.

## 6. Dữ liệu và thiết kế đánh giá

Nghiên cứu đánh giá phát hiện lỗ hổng mức hàm trên hai bộ dữ liệu C/C++:

| Bộ dữ liệu | Hàm có lỗ hổng | Hàm không lỗ hổng | Tổng số | Tỷ lệ dương:âm |
| --- | ---: | ---: | ---: | ---: |
| FFmpeg+QEMU | 12.460 | 14.858 | 27.318 | 1:1,19 |
| DiverseVul | 17.976 | 291.411 | 309.387 | 1:16,21 |

Tổng cộng có 30.436 hàm có lỗ hổng và 306.269 hàm không có lỗ hổng. Các chỉ số gồm accuracy, precision, recall và F1-score. Vì DiverseVul mất cân bằng mạnh, accuracy riêng lẻ không phản ánh đầy đủ hiệu quả phát hiện; precision, recall và F1 cần được xem đồng thời.

Các baseline thuộc ba nhóm: học sâu (Devign, REVEAL, MGVD), LLM fine-tuning (UniXcoder, CodeT5, LineVul), và prompt engineering (Qwen3-32B, CodeLlama-70B, DeepSeek-R1-Distill-Llama-70B, Llama-3.1-70B, DeepSeek-R1, Doubao, GPT-4o).

## 7. Câu hỏi nghiên cứu

- **RQ1:** RLV hiệu quả thế nào so với các baseline hiện đại?
- **RQ2:** Khả năng tổng quát hóa trên dự án chưa thấy của RLV so với baseline ra sao?
- **RQ3:** Từng kỹ thuật trong RLV đóng góp như thế nào?

## 8. Kết quả RQ1: hiệu quả trên tập kiểm thử thông thường

Kết quả của RLV và các baseline tiêu biểu:

| Phương pháp | FFmpeg+QEMU F1 | DiverseVul F1 |
| --- | ---: | ---: |
| Devign | 0,5408 | 0,2463 |
| REVEAL | 0,5600 | 0,2751 |
| MGVD | 0,6130 | 0,2822 |
| CodeT5 | 0,6340 | 0,3239 |
| LineVul | 0,6102 | 0,3135 |
| DeepSeek-R1 (prompt trực tiếp) | 0,6162 | 0,2617 |
| GPT-4o (prompt trực tiếp) | 0,6044 | 0,1759 |
| **RLV** | **0,6428** | **0,3258** |

RLV có F1 và recall cao nhất trong các phương pháp được so sánh trên cả hai bộ dữ liệu. Trên FFmpeg+QEMU, RLV có precision 0,5186 và recall 0,8454; trên DiverseVul, các giá trị tương ứng là 0,2527 và 0,4583.

Tuy nhiên, hiệu năng trên DiverseVul vẫn thấp hơn đáng kể do bộ dữ liệu mất cân bằng và nhiều lỗ hổng có tính không cục bộ, tức liên quan đến tương tác giữa nhiều hàm. Đây là giới hạn chung của các phương pháp phân loại ở mức một hàm.

## 9. Kết quả RQ2: tổng quát hóa sang dự án chưa thấy

Tác giả dùng DiverseVul (754 dự án), chọn ngẫu nhiên 100 dự án làm tập kiểm thử chưa thấy; các dự án còn lại được chia 90% huấn luyện và 10% validation. Kết quả:

| Phương pháp | Precision | Recall | F1-score |
| --- | ---: | ---: | ---: |
| REVEAL | 0,1300 | 0,2096 | 0,1605 |
| CodeT5 | 0,1560 | 0,1928 | 0,1725 |
| DeepSeek-R1 | 0,1830 | 0,3874 | 0,2486 |
| GPT-4o | 0,1710 | 0,3520 | 0,2302 |
| **RLV** | **0,2400** | **0,4596** | **0,3153** |

RLV đứng đầu ở cả precision, recall và F1 trong thiết lập này. Bài báo quy kết lợi ích tổng quát hóa cho việc dùng tri thức từ chính repository thay vì chỉ dựa vào mẫu đã học từ các dự án huấn luyện. Theo báo cáo của tác giả, RLV hơn phương pháp prompt-based tốt nhất 31,15% về precision và 26,83% về F1-score.

## 10. Kết quả RQ3: ablation study

RLV đầy đủ được so sánh với các biến thể chỉ dùng một/hai loại ngữ cảnh, bỏ tóm tắt callee, lọc ngẫu nhiên thay vì LLM và zero-shot không có CoT.

| Biến thể | FFmpeg+QEMU F1 | DiverseVul F1 |
| --- | ---: | ---: |
| Chỉ callee (RLV-ce) | 0,6162 | 0,2902 |
| Chỉ data type (RLV-dt) | 0,6200 | 0,2728 |
| Chỉ caller (RLV-cr) | 0,6188 | 0,2568 |
| Không tóm tắt callee (RLV-ns) | 0,6357 | 0,3210 |
| Không lọc bằng LLM (RLV-nf) | 0,6286 | 0,3212 |
| Zero-shot không CoT (RLV-zs) | 0,6347 | 0,3177 |
| **RLV đầy đủ** | **0,6428** | **0,3258** |

Kết luận chính từ ablation:

- Ba loại ngữ cảnh bổ sung cho nhau; callee có đóng góp nổi bật nhất, nhưng dùng cả callee, data type và caller cho kết quả tốt nhất.
- Tóm tắt callee do LLM tạo giúp tăng hiệu quả so với chỉ giữ chữ ký hàm.
- Bộ lọc LLM tốt hơn lấy ngẫu nhiên: với các hàm có nhiều thành phần, trên FFmpeg+QEMU phát hiện thêm 10 hàm lỗi và giảm 53 false positive; trên DiverseVul là thêm 28 hàm lỗi và giảm 75 false positive.
- Zero-shot CoT cải thiện nhẹ nhưng nhất quán so với zero-shot không CoT.

## 11. Ảnh hưởng của lựa chọn LLM

Framework không bảo đảm hiệu quả giống nhau với mọi mô hình. RLV dựa trên GPT-4 Turbo đạt F1 0,6346/0,2944 và RLV dựa trên GPT-4o đạt 0,6291/0,2964 trên FFmpeg+QEMU/DiverseVul. Các mô hình mã nguồn mở nhỏ hơn cho kết quả thấp hơn đáng kể trên DiverseVul. Điều này cho thấy chất lượng LLM nền vẫn là yếu tố quan trọng, dù cấu trúc RLV thường cải thiện baseline prompt-based tương ứng.

## 12. Giá trị và điểm khác biệt

Đóng góp cốt lõi không phải chỉ là thêm nhiều mã nguồn vào prompt, mà là truy xuất **có chọn lọc** thông tin cấp dự án rồi chuẩn hóa nó thành dạng dễ dùng cho LLM: định nghĩa kiểu, chữ ký và tóm tắt callee, cộng với caller đại diện. Cách làm này giúp LLM có căn cứ để hiểu API nội bộ và mục đích của hàm thay vì suy đoán từ mã cục bộ.

So với một bộ phân loại phải huấn luyện lại, RLV có lợi thế thực tế khi áp dụng sang dự án mới vì có thể tận dụng trực tiếp repository đích. Đổi lại, nó cần khả năng phân tích/truy xuất mã nguồn ở cấp repository và chi phí suy luận LLM cho cả bước tinh lọc lẫn phân loại.

## 13. Hạn chế và các mối đe dọa đến tính hợp lệ

- Nghiên cứu chỉ đánh giá trên lỗ hổng C/C++; không thể suy rộng trực tiếp kết quả sang ngôn ngữ khác.
- Giới hạn cửa sổ ngữ cảnh khiến RLV chỉ chọn một phần callee và data type khi hàm dài hoặc phức tạp; việc bỏ sót ngữ cảnh có thể làm giảm chất lượng nhận định.
- Tóm tắt do LLM sinh có thể sai ngữ nghĩa. Trong đánh giá thủ công 50 tóm tắt FFmpeg bởi ba lập trình viên giàu kinh nghiệm, 45 tóm tắt (90%) được cả ba đồng ý là chính xác; lỗi còn lại chủ yếu ở mô tả hành vi callee.
- Kết quả baseline phụ thuộc vào implementation và cách chia dữ liệu. Tác giả tái sử dụng implementation sẵn có và theo cách chia dữ liệu mà nhà cung cấp công bố, nhưng không thể khẳng định tái tạo hoàn toàn kết quả gốc của mọi baseline.
- Các chỉ số classification là thước đo phổ biến, song không thay thế hoàn toàn đánh giá giá trị triển khai trong quy trình phát triển thực tế.

## 14. Kết luận và hướng phát triển

RLV cho thấy phát hiện lỗ hổng bằng LLM ở mức hàm được cải thiện khi LLM nhận ngữ cảnh nội bộ liên quan từ repository, thay vì chỉ nhìn hàm đích. Trên hai bộ dữ liệu đánh giá, framework đạt F1 tốt nhất trong các phương pháp được so sánh và duy trì lợi thế khi kiểm tra dự án chưa thấy.

Hướng tiếp theo tác giả nêu là đưa ngữ cảnh vào theo nhiều lượt/phân đoạn để giảm tác động của giới hạn token, đồng thời xây dựng dữ liệu về đường đi qua nhiều hàm có lỗ hổng. Hướng này phù hợp với quan sát rằng nhiều lỗi trong DiverseVul là không cục bộ và khó phát hiện nếu chỉ xem một hàm.

## 15. Tài liệu tham khảo trực tiếp

1. Fangcheng Qiu et al. (2026), *RLV: LLM-based vulnerability detection by retrieving and refining contextual information*, *The Journal of Systems & Software*, 235, 112756. https://doi.org/10.1016/j.jss.2025.112756
2. Replication package của RLV được bài báo cho biết là mở nguồn (2025); xem liên kết được tác giả cung cấp trong bài báo gốc.
