# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Spiritup
- Nhóm được chấm: XYZ

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** khớp với CPS phạm vi chọn lọc (**4.599 đ**, `simulated`, rẻ hơn `12.000 đ`); nêu đủ số bất lợi (`quoc_te` **22.515 đ**, xem lại 100% **11.743–12.516 đ**, power +5 điểm **64,17%**) và có 4 điều kiện xử lý cụ thể |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ `_simulated` đều có nhãn `simulated`; thu hẹp phạm vi về `noi_dia` (**2.696 đ**) + `hang_nang` (**8.221 đ**), loại `quoc_te` (**22.515 đ**) và `doi_tac` (**10.215 đ**) có lý do bằng số |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên song song 50/50 theo `staff` (**20 cụm/nhóm**, **5.980 yc/nhóm**, DE = 6,96, MDE +6 điểm); đủ 3 luật dừng 4 vế có ngưỡng (`> 6,0%`, `> 9.000 đ` / `> 35%`, `< 50%`), thời hạn (`3/5/7 ngày`) và vai trò có quyền dừng |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp toàn bộ số liệu, thu hẹp phạm vi hợp lý (`noi_dia + hang_nang`, CPS **4.599 đ** `simulated`), không che giấu số bất lợi (xem lại 100% **11.743–12.516 đ**, power +5 điểm **64,17%**), và kế hoạch pilot tách được tác động với 3 luật dừng định lượng rõ người bấm dừng (rollback ≤ 15 phút).

**Một câu hỏi cho đội trình:** Khi thời gian xem lại hiện tại là số `simulated` (chiếm **40,70%** tổng chi phí), nhóm làm gì trong tuần 1 pilot để đo thời gian thật và tránh kịch bản xem lại 100% đẩy CPS lên **11.743–12.516 đ**?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội trình xác nhận bật đủ 7 event có `trace_id` (gồm `review_duration_sec` trong `review_decision_submitted`) ngay từ ngày đầu pilot để thay thế số `simulated` sau tuần 1, đồng thời áp dụng luật dừng nếu tỉ lệ xem lại > **35%** trong 5 ngày.
