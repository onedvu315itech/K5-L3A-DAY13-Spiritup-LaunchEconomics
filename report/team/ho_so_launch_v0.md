# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Spiritup · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: **4.472 đ** (`simulated`, gấp 16,28× hoá đơn 275 đ/yc; công NV chiếm 92,5%). Phạm vi `noi_dia` + `hang_nang` đã cộng cố định 40 tr/tháng: **4.599 đ** (45.000 yc/tháng) hoặc **5.784 đ** (giảm nửa khối lượng) [`simulated`] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Làm lại (+51,77%) · 2. Xem lại (+40,70%) · 3. Lương NV (+23,12%)** [`simulated`] (token ×2 chỉ +5,62%). Bất lợi: **xem lại 100%** đẩy CPS lên **11.743 đ (0,98×)**–**12.516 đ (1,04×)** [`simulated`] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chuẩn NV tự làm: **12.000 đ/yc**. Chi phí cả hệ thống rẻ nhất ở giới hạn **2 lần chạy: 6.901.220 đ** (5.751 đ/yc = 0,48×; 3 lần: 7.037.585 đ = 0,49×) [`simulated`]. Chọn `noi_dia` (2.696 đ = 0,22×) + `hang_nang` (8.221 đ = 0,69×); loại `quoc_te` (22.515 đ = 1,88×) & `doi_tac` (10.215 đ = 0,85×) [`simulated`] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (chưa có đối chứng): Chính (đóng 24h & không mở lại 7 ngày) **82,83%** (`994/1.200`); Dùng (bỏ qua gợi ý `sua/bo`) **27,12%** (`48/177`); An toàn (mở lại 7 ngày) **4,25%** (`51/1.200`; phạm vi pilot **3,97%**). Thêm 2 chỉ số đề xuất (phút xem lại thật, lệch đối soát sổ cái) & **7 event** có `trace_id` (`chi_so.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận độc lập **20/20 (100%)** (đạt ≥ 80%; phân bổ: Người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3). Bảng khắc phục **5 ca đại diện đủ 5 loại PAIR** (ca 9, 7, 18, 4, 17) có event, ngưỡng, tần suất đo được và 1 vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia ngẫu nhiên theo **`staff`** 50/50 (**20 cụm/nhóm**, đối chứng song song), rollout `10% → 25% → 50%`; cỡ mẫu **5.980 yc/nhóm** (**859 hiệu dụng**, DE = 6,96). Đánh đổi: **MDE +6 điểm** (power ở +5 điểm = **64,17%**). Đủ **3 luật dừng** (mở lại 7 ngày > 6,0%/3 ngày; CPS > 9.000 đ [`simulated`] hoặc xem lại > 35%/5 ngày; giữ gợi ý < 50%/7 ngày), rollback ≤ 15 phút (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 rủi ro từ bảng độ nhạy (`chi_so.md`): (1) **Xem lại 100%** đẩy CPS lên **11.743–12.516 đ** (`0,98×–1,04×`, hòa vốn 4,76–5,12 phút); (2) **Làm lại ×2** tăng CPS **+51,77%** lên **6.787 đ**; (3) **Lương NV +25%** tăng CPS **+23,12%** lên **5.506 đ** [`simulated`] — kèm dấu hiệu cảnh báo & hành động | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho kế hoạch pilot trong phạm vi **`noi_dia` + `hang_nang`** (giới hạn tối đa **2 lần chạy**, loại `quoc_te` và `doi_tac`).

- Sửa lỗi hoàn trùng & đối soát sổ cái (ca 7, 20), chỉ báo "đã hoàn" khi `refund_ledger_write` trả `ok`, và xoá bộ nhớ đệm bảng giá kèm `pricing_version` (ca 17) · **Phụ trách:** Kỹ sư trưởng agent · **Kiểm tra trước:** 2026-11-28.
- Ký xác nhận chấp nhận đánh đổi cỡ mẫu **MDE +6 điểm** (power ở mức +5 điểm là **64,17%**) và cấu hình giới hạn **2 lần chạy** để tối ưu chi phí cả hệ thống · **Phụ trách:** Giám đốc vận hành LogiX-VN · **Kiểm tra trước:** 2026-11-28.
- Bật đủ **7 event** có `trace_id` (gồm `review_duration_sec` trong `review_decision_submitted`) để thay thế các cột `*_simulated` bằng thời gian đo thật sau tuần 1 · **Phụ trách:** Kỹ sư trưởng agent · **Kiểm tra trước:** 2026-12-05.
- Ban hành lộ trình giảm tỉ lệ xem lại theo bậc xuống **≤ 35%** và giữ thời gian xem lại dưới ngưỡng hòa vốn **4,8 phút/ca** (tránh kịch bản xem lại 100% lên **11.743–12.516 đ**, `simulated`) · **Phụ trách:** Trưởng nhóm CSKH · **Kiểm tra trước:** 2026-12-05.
