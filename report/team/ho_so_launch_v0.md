# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Spiritup · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: **4.472 đ** (`simulated`, gấp 16,28× hoá đơn 275 đ/yc; công NV chiếm 92,5%). Phạm vi `noi_dia` + `hang_nang` đã cộng cố định 40 tr/tháng: **4.599 đ** (45.000 yc/tháng) hoặc **5.784 đ** (giảm nửa khối lượng) [`simulated`] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Làm lại (+51,77%) · 2. Xem lại (+40,70%) · 3. Lương NV (+23,12%)** [`simulated`] (token ×2 chỉ +5,62%). Bất lợi: **xem lại 100%** đẩy CPS lên **11.743 đ (0,98×)**–**12.516 đ (1,04×)** [`simulated`] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chuẩn NV tự làm: **12.000 đ/yc**. Chi phí cả hệ thống rẻ nhất ở giới hạn **2 lần chạy: 6.901.220 đ** (5.751 đ/yc = 0,48×; 3 lần: 7.037.585 đ = 0,49×) [`simulated`]. Chọn `noi_dia` (2.696 đ = 0,22×) + `hang_nang` (8.221 đ = 0,69×); loại `quoc_te` (22.515 đ = 1,88×) & `doi_tac` (10.215 đ = 0,85×) [`simulated`] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | `[Chờ CP5 · E1: 3 chỉ số trong đợt chạy thử (không viết "đã nâng") + số event có trace_id]` | Chưa | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận độc lập **20/20 (100%)** (đạt ≥ 80%; phân bổ: Người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3). Bảng khắc phục **5 ca đại diện đủ 5 loại PAIR** (ca 9, 7, 18, 4, 17) có event, ngưỡng, tần suất đo được và 1 vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | `[Chờ CP4 · D: Đơn vị chia, cỡ mẫu, MDE, đánh đổi power, ≥ 3 luật dừng đủ 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ]` | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | `[Chờ CP5 · E2: ≥ 2 rủi ro chính lấy số từ bảng độ nhạy + dấu hiệu theo dõi & hành động, nhãn simulated]` | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** `[Chốt cùng nhóm trước 17:00 — giữ đúng 1 lựa chọn: Go | Go có điều kiện | No-go]`

- `[Điều kiện 1 — VD: sửa lỗi nghiêm trọng trước khi mở pilot] · Phụ trách: Kỹ sư trưởng agent · Kiểm tra trước: [ngày]`
- `[Điều kiện 2 — VD: ký chấp nhận đánh đổi MDE/power của pilot] · Phụ trách: Giám đốc vận hành LogiX-VN · Kiểm tra trước: [ngày]`
- `[Điều kiện 3 — VD: bật đủ event có trace_id, thay phút simulated bằng phút đo thật sau tuần 1] · Phụ trách: Kỹ sư trưởng agent · Kiểm tra trước: [ngày]`
- `[Điều kiện 4 — VD: lộ trình giảm tỉ lệ xem lại theo bậc] · Phụ trách: Trưởng nhóm CSKH · Kiểm tra trước: [ngày]`
