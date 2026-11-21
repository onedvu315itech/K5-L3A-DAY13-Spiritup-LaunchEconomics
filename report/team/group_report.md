# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Spiritup
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Vũ Lê Đức, Lê Hữu Toàn, Trần Việt Thịnh)

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí LogiX-VN trình hội đồng **Gate 2a** nhằm trả lời bốn câu hỏi cốt lõi bằng dữ liệu giả lập (1.200 yêu cầu / 1.624 lần chạy từ `src/logix_requests.csv` và `src/logix_runs.csv`): (1) chi phí thật mỗi việc thành công so với mức nhân viên tự làm `12.000 đ`; (2) chỉ số sử dụng và hệ thống event có `trace_id`; (3) phân loại lỗi Google PAIR và cách khắc phục; (4) thiết kế kế hoạch pilot tách được tác động, đủ cỡ mẫu và có luật dừng rõ ràng.

## 3. Giải pháp

- **Nhiệm vụ A & B (`src/lab13.py`, `report/team/bang_chi_phi.md`):** Hoàn thiện mô hình `mo_hinh()`, vượt qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính chi phí theo toàn mẫu, tách 4 loại yêu cầu (A3), cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang` (A4), và phân tích độ nhạy 9 kịch bản B1, cặp B2, giới hạn chạy lại B3, xem lại 100% B4.
- **Nhiệm vụ C (`report/team/bang_loi.md`):** Hai người gắn nhãn độc lập 20 ca lỗi trong 8 phút không trao đổi, đạt đồng thuận **20/20 (100%)**, và lập bảng khắc phục 5 ca đại diện đủ 5 loại PAIR với cách phát hiện đo được và vai trò phụ trách cụ thể.
- **Nhiệm vụ D (`report/team/pilot_plan.yaml`):** Tính cỡ mẫu D1 bằng `src/lab13.py`, chọn đơn vị chia theo `staff` (20 cụm/nhóm, đối chứng song song 50/50), chấp nhận đánh đổi MDE +6 điểm để phù hợp quy mô 40 nhân viên, và thiết lập 3 luật dừng đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ`.
- **Nhiệm vụ E (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`):** Đặc tả 5 chỉ số E1, 7 event có `trace_id`, 3 rủi ro kinh tế E2, và tổng hợp thành hồ sơ 1 trang kèm đề xuất cuối.

## 4. Kết quả

- **Chi phí (`simulated`):** Toàn mẫu **4.472 đ/việc thành công** (gấp **16,28×** hóa đơn token + tool `275 đ/yc`; thời gian nhân viên chiếm **92,5%**). Phạm vi chọn lọc `noi_dia + hang_nang` đã cộng cố định 40 triệu đ/tháng là **4.599 đ** (45.000 yc/tháng) hoặc **5.784 đ** (giảm nửa khối lượng), đều rẻ hơn mức **12.000 đ** nhân viên tự làm. Giới hạn chạy tối ưu chi phí cả hệ thống là **2 lần chạy** (**6.901.220 đ**, `simulated`); loại `quoc_te` (**22.515 đ**, `simulated`) và `doi_tac` (**10.215 đ**, `simulated`).
- **Độ nhạy & rủi ro (`simulated`):** Top 3 yếu tố nhạy nhất là **Làm lại (+51,77%)**, **Xem lại (+40,70%)**, **Lương NV (+23,12%)**. Kịch bản bất lợi **xem lại 100%** đẩy CPS lên **11.743–12.516 đ** (`0,98×–1,04×`, hòa vốn ở `4,76–5,12 phút/gợi ý`).
- **Chỉ số thử nghiệm & lỗi:** Đóng 24h không mở lại 7 ngày **82,83%** (`994/1.200`); bỏ qua gợi ý `sua/bo` **27,12%** (`48/177`); mở lại 7 ngày **4,25%** (`51/1.200`, phạm vi pilot **3,97%**). Đồng thuận gắn nhãn lỗi **20/20 (100%)**.
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang`, giới hạn tối đa **2 lần chạy**, chia ngẫu nhiên theo `staff` (**20 cụm/nhóm**, `5.980 yc/nhóm`, **MDE +6 điểm**), kèm 4 điều kiện kiểm tra trước ngày `2026-11-28` và `2026-12-05`.
- **Kết quả duyệt chéo nhóm nhận được từ hội đồng:** *(cập nhật kết quả/nhận xét từ nhóm hội đồng tại buổi nếu có)*.

## 5. Khó khăn và cách xử lý

- **Giới hạn cỡ mẫu theo cụm:** Với 40 nhân viên toàn công ty (20 người/nhóm), không thể đạt power 80% cho MDE +5 điểm ở `ICC = 0,02` (tiệm cận tối đa 1.000 < 1.251). Nhóm xử lý bằng cách nâng MDE lên **+6 điểm** (859 hiệu dụng/nhóm, 299 yc/nhân viên) và ghi rõ đánh đổi power ở +5 điểm (`64,17%`) vào hồ sơ.
- **Dữ liệu thời gian giả lập:** Các cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated` là giả lập, nhóm gắn nhãn `simulated` ở mọi con số liên quan và bổ sung event `review_decision_submitted` có `review_duration_sec` để thay thế bằng số đo thật sau tuần 1 pilot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và các file báo cáo cá nhân `report/team/2A202603683_VuLeDuc.md`, `report/team/2A202603660_LeHuuToan.md`, `report/team/2A202603661_TranVietThinh.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Thời gian xem lại và làm lại hiện dựa trên dữ liệu `simulated`; power phát hiện mức chênh +5 điểm chỉ đạt `64,17%` khi chia theo `staff`.
- **Hướng cải thiện:** Bật đủ 7 event có `trace_id` ngay từ tuần 1 pilot để đo thời gian thao tác thực tế; sửa dứt điểm lỗi hoàn trùng/sổ cái (ca 7, 20) và bộ nhớ đệm bảng giá (ca 17); tối ưu giao diện gợi ý để giữ tỉ lệ xem lại ≤ 35% và thời gian xem lại < 4,8 phút/ca.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, `arxiv.org/abs/2504.13359`.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
- Tài liệu nội bộ lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
