# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Lê Đức · Người gắn nhãn 2: Trần Việt Thịnh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (đồng thuận 20/20 = 100%, đạt ngưỡng ≥ 80%). Ghi chú ranh giới áp dụng: **Hệ thống** là sai thiết kế/chính sách và lộ ra (ca 2, 7, 8, 15, 20), còn **Ngầm** là sai/tốn kém nhưng cả người dùng lẫn hệ thống không nhận ra tới khi kiểm tra (ca 5, 12, 17).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (`reason = invalid_waybill_format`, có `trace_id`), đo hằng ngày; cảnh báo khi > 2% tổng yêu cầu/ngày | Tự nhận diện mã sàn TMĐT để tra chéo sang mã vận đơn; nếu không tra được thì trả hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn "đã hoàn" và event `refund_ledger_write` (`ket_qua = ok`) cùng `trace_id`; ngưỡng cảnh báo ≥ 1 ca lệch (mục tiêu 0 ca) | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok`; sau 3 lần lỗi 503 thì báo "đang xử lý" và chuyển nhân viên qua `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` (`reason = sai_so_tien`) nhưng đối soát thấy số tiền đúng chính sách, đo hằng tuần; cảnh báo khi > 1% số đơn đóng/tuần | Bắt buộc mẫu phản hồi hiển thị rõ cách tính (VD: `30.000 đ × 50% = 15.000 đ`) kèm điều kiện trễ giờ áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason = thieu_du_lieu`, có `trace_id`) tách theo `loai`, đo hằng tuần; cảnh báo khi > 15% trong phạm vi pilot | Loại nhóm `quoc_te` khỏi phạm vi pilot; giữ cơ chế chuyển thẳng nhân viên kèm tóm tắt khi thiếu dữ liệu chặng giao | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; cảnh báo khi > 1% số đơn kiểm tra bị lệch tiền | Tự động xoá bộ nhớ đệm khi có bảng giá mới và ghi trường `pricing_version` vào mọi trace để truy vết | Kế toán trưởng |
