# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (`51/1.200`; phạm vi `noi_dia + hang_nang`: **3,97%**, `39/982`) |
| Dùng | Nhóm tự đề xuất: Thời gian xem lại thực tế mỗi gợi ý (phút) | Tổng `review_duration_sec / 60` ÷ số event `review_decision_submitted` (thay thế `phut_xem_lai_simulated`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ lệch đối soát sổ cái hoàn tiền | Số tin nhắn "đã hoàn" không có `refund_ledger_write` (`ket_qua = ok`) ÷ tổng lệnh hoàn | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `assistant_suggestion_shown` | Agent | `request_id, staff_id, loai, attempt, trace_id` | Khi trợ lý hiển thị gợi ý cho nhân viên |
| `review_decision_submitted` | Giao diện CSKH | `request_id, staff_id, quyet_dinh (giu/sua/bo), review_duration_sec, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `ticket_closed` | Hệ thống ticket | `request_id, loai, created_at, closed_at, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Hệ thống ticket | `request_id, loai, reason, reopened_within_7d, trace_id` | Khi khách hoặc CSKH mở lại yêu cầu |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id, ket_qua (ok/loi_503), amount_vnd, pricing_version, trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id, loai, reason, attempt, trace_id` | Khi trợ lý chuyển yêu cầu về nhân viên |
| `audit_sample_checked` | Hệ thống kiểm toán | `request_id, is_mismatch, diff_vnd, pricing_version, trace_id` | Khi kiểm tra mẫu 100 đơn/tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** tính từ `ticket_closed` (`closed_at - created_at ≤ 24h`) đối chiếu không có `ticket_reopened` (`reopened_within_7d = true`) theo `request_id` và `trace_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `review_decision_submitted` (`quyet_dinh ∈ {sua, bo}`) ÷ tổng `review_decision_submitted` (hoặc `assistant_suggestion_shown` có xem lại).
- **Chỉ số an toàn (tỉ lệ lỗi lọt đến khách):** tính từ `ticket_reopened` (`reopened_within_7d = true`) ÷ tổng `ticket_closed`.
- **Chỉ số dùng đề xuất (thời gian xem lại thực tế):** tính trực tiếp từ `review_duration_sec` trong `review_decision_submitted`.
- **Chỉ số an toàn đề xuất (lệch đối soát sổ cái):** đối chiếu `ticket_closed` / thông báo "đã hoàn" với `refund_ledger_write` (`ket_qua = ok`) qua `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Tỉ lệ xem lại cao hoặc phải xem lại 100% | Xem lại gấp đôi làm CPS tăng **+40,70%** lên **6.292 đ**; xem lại 100% ở `noi_dia + hang_nang` đẩy CPS lên **11.743–12.516 đ** (`0,98×–1,04×` mức 12.000 đ; hòa vốn 4,76–5,12 phút) [`simulated`] | Tỉ lệ xem lại > **35%** hoặc `review_duration_sec` > **4,8 phút/ca** trong 5 ngày liên tiếp | Dừng tăng tỉ lệ rollout, rút gọn tóm tắt gợi ý và bật luồng tự duyệt với ca độ tin cậy cao | PM trợ lý hoàn phí |
| Số ca làm lại tăng (yếu tố nhạy nhất) | Làm lại chiếm **51,77%** tổng chi phí (`2.264.000 đ`); nếu ca làm lại gấp đôi, CPS tăng **+51,77%** lên **6.787 đ** [`simulated`] | Tỉ lệ `sua/bo` > **30%** trên `review_decision_submitted` hoặc `ticket_reopened` > **6,0%** trong 3 ngày | Kích hoạt luật dừng an toàn, rà soát nguyên nhân sai (VD hàng nặng vs hàng thường) trước khi mở lại | Trưởng nhóm CSKH |
| Lương nhân viên tăng hoặc lỗi ngầm kéo dài | Lương NV tăng 25% làm CPS tăng **+23,12%** lên **5.506 đ** [`simulated`] (do công NV chiếm **92,5%** tổng chi phí) | `audit_sample_checked` lệch > **1%** hoặc thời gian xử lý trung bình tăng | Sửa lỗi ngầm (cache bảng giá, tool theo depot) và tối ưu thao tác CSKH | Kỹ sư trưởng agent |
