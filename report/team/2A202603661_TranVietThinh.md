# Báo cáo cá nhân — TranVietThinh-2A202603661

## 1. Thông tin thành viên

- Họ tên: Trần Việt Thịnh
- MSSV: 2A202603661
- Email: thinhkesat@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **CP3 · Nhiệm vụ C (`report/team/bang_loi.md`):**
  - Đọc và tự gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR (*Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*) theo nguyên nhân gốc.
  - Đối chiếu với Người gắn nhãn 1, tính tỉ lệ đồng thuận, thống nhất nhãn và viết quy tắc phân biệt cho các ca không trùng.
  - Phối hợp chọn 5 ca (đủ 5 loại) và xây dựng bảng khắc phục có cách phát hiện đo được cùng 1 vai trò phụ trách.
- **Xuyên suốt CP1–CP5 · Giữ hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
  - Dựng khung và cập nhật dần 7 mục của hồ sơ launch v0 (1 trang) từ kết quả đã chốt của các thành viên qua từng checkpoint.
  - Đảm bảo tuân thủ các quy tắc hồ sơ: gắn nhãn `simulated` cho mọi số liệu từ cột `*_simulated`, cột trạng thái đúng 3 giá trị quy định (`Xong, có bằng chứng` · `Chưa` · `Giả lập`), người phụ trách là 1 vai trò cụ thể, đúng phạm vi Gate 2a (chỉ duyệt kế hoạch pilot).
  - Phối hợp cùng nhóm chốt đề xuất cuối (`Go` / `Go có điều kiện` / `No-go`) trước 17:00 để duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **CP3 · Bảng lỗi và cách khắc phục (`report/team/bang_loi.md`):**
  - Tự gắn nhãn độc lập đủ **20/20 ca lỗi** (cột `Nhãn người 2`) theo nguyên nhân gốc trên 5 loại của Google PAIR (*Do người dùng: 4 · Hệ thống: 5 · Ngữ cảnh: 4 · Giới hạn hệ thống: 4 · Ngầm: 3*). Khi đối chiếu với Người gắn nhãn 1 (Vũ Lê Đức), đạt đồng thuận **20/20 = 100%** (vượt ngưỡng ≥ 80%).
  - Soạn **Bảng khắc phục cho 5 ca đại diện** đủ 5 loại lỗi (ca 9, 7, 18, 4, 17), đảm bảo mỗi dòng có event, ngưỡng, tần suất đo được và gán đúng 1 vai trò phụ trách cụ thể.
- **CP1–CP5 · Giữ và hoàn thiện Hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
  - Dựng khung hồ sơ 1 trang (7 mục) ngay từ đầu buổi, phân định rõ cột Trạng thái (`Giả lập` cho mục 1, 2, 3, 7; `Xong, có bằng chứng` cho mục 4, 5, 6) và vai trò phụ trách cho từng mục.
  - Cập nhật liên tục từng checkpoint ngay khi đồng đội chốt số: Mục 1–3 (CP1–CP2 từ `bang_chi_phi.md`), Mục 5 (CP3 từ `bang_loi.md`), Mục 6 (CP4 từ `pilot_plan.yaml`), Mục 4 & 7 (CP5 từ `chi_so.md`).
  - Hoàn thiện **Đề xuất cuối: `Go có điều kiện`** cho kế hoạch pilot phạm vi `noi_dia` + `hang_nang` (giới hạn 2 lần chạy, loại `quoc_te` và `doi_tac`) kèm 4 điều kiện xử lý các con số bất lợi (xem lại 100% lên 11.743–12.516 đ `simulated`; power ở +5 điểm là 64,17%), có người phụ trách và ngày kiểm tra cụ thể.

## 4. Bằng chứng

- **Các file trực tiếp thực hiện/cập nhật:**
  - `report/team/bang_loi.md` (cột `Nhãn người 2` và Bảng khắc phục 5 ca)
  - `report/team/ho_so_launch_v0.md` (toàn bộ 7 mục và Đề xuất cuối)
  - `report/team/2A202603661_TranVietThinh.md` và mục cá nhân trong `TEAM.md`
- **Các Pull Request & commit đã merge vào `main`:**
  - PR #1 (`5d6450e` / `61a0a1d`): Gắn nhãn độc lập 20 ca lỗi (CP3)
  - PR #3 (`d6eb330`): Dựng khung `report/team/ho_so_launch_v0.md`
  - PR #5 (`f11ad4e`): Tạo file báo cáo cá nhân `2A202603661_TranVietThinh.md`
  - PR #6 (`7173108`): Soạn bảng khắc phục 5 ca lỗi đại diện trong `bang_loi.md`
  - PR #8 (`346462a`): Cập nhật Mục 1, 2, 3 (CP1 & CP2) vào `ho_so_launch_v0.md`
  - PR #10 (`a7b4c75`): Cập nhật Mục 5 (CP3) vào `ho_so_launch_v0.md`
  - PR #12 (`7bb8fc8`): Cập nhật Mục 6 (CP4) vào `ho_so_launch_v0.md`
  - PR #14 (`9ef4bf9`): Hoàn thiện Mục 4, 7 (CP5) và Đề xuất `Go có điều kiện` trong `ho_so_launch_v0.md`

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:**
  - Tóm tắt yêu cầu đề bài, rubric và phân tách rạch ròi phạm vi vai trò *Người gắn nhãn 2, kiêm giữ hồ sơ*.
  - Trích xuất 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, gợi ý phân loại theo nguyên nhân gốc 5 loại Google PAIR và soạn bảng khắc phục 5 ca.
  - Hỗ trợ tổng hợp số liệu từ `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` vào `ho_so_launch_v0.md` và rà soát checklist quy tắc.
- **Cách tự kiểm tra kết quả:**
  - Tự đọc lại từng mô tả trong 20 ca lỗi để kiểm chứng lý do phân loại theo nguyên nhân gốc (đặc biệt các ca ranh giới: ca 6, 9, 12, 13, 18) và đối chiếu độc lập với Người gắn nhãn 1 (đạt 20/20 = 100%).
  - Đối chiếu chéo từng con số trong `ho_so_launch_v0.md` với file nguồn tương ứng của đồng đội (`bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`), kiểm tra đủ nhãn `simulated`, đúng 3 giá trị cột Trạng thái, mỗi mục 1 vai trò phụ trách, và quét kiểm tra không vi phạm từ cấm quy tắc 5.

## 6. Tự đánh giá

- Hoàn thành đúng và đầy đủ phạm vi vai trò được giao (CP3 và giữ hồ sơ xuyên suốt CP1–CP5), cập nhật hồ sơ kịp thời theo từng checkpoint thông qua quy trình nhánh riêng và Pull Request rõ ràng.
- Điểm mạnh: nắm chắc ranh giới 5 loại lỗi Google PAIR, đảm bảo tính nhất quán giữa hồ sơ 1 trang và toàn bộ bằng chứng của nhóm, nêu thẳng các con số bất lợi kèm điều kiện kiểm soát.
- Điểm cần cải thiện: chủ động đồng bộ sớm hơn với các bạn ở mốc chuyển tiếp CP1–CP2 để hồ sơ luôn cập nhật sát giờ hơn.
