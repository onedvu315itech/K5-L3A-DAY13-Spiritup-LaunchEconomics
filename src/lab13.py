"""Mô hình chi phí và cỡ mẫu Lab 13. Chạy từ src/: python lab13.py."""
import math
import sys
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize


GIA_VAO = 26
GIA_RA = 130
GIA_TOOL = 15
LUONG_PHUT = 2000
BASELINE = 12000
CAC_LOAI = ("noi_dia", "hang_nang", "quoc_te", "doi_tac")


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy kỳ vọng với xác suất thành công p trên mỗi lần."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất có ít nhất một lần thành công trong giới hạn k."""
    if k == 0 or p == 0:
        return 0.0
    if k is None or p == 1:
        return 1.0
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Số lần chạy kỳ vọng chia cho xác suất thành công."""
    ti_le = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / ti_le if ti_le else math.inf


def kiem_tra_dap_an_biet_truoc():
    assert math.isclose(so_lan_chay_ky_vong(0.8, 2), 1.20)
    assert math.isclose(so_lan_chay_ky_vong(0.8), 1.25)
    assert math.isclose(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25)
    print("Ba phép thử đáp án biết trước: ĐẠT (1,20 · 1,25 · 1,25)")


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Tính chi phí trên các lần chạy của phạm vi yêu cầu được chọn."""
    runs = runs[runs["request_id"].isin(reqs["request_id"])]
    if max_lan_chay is not None:
        runs = runs[runs["attempt"] <= max_lan_chay]
        # Ca bị cắt chuyển thẳng cho nhân viên, tính phí chuyển ở B3.
        reqs_xu_ly = reqs[reqs["so_lan_chay"] <= max_lan_chay]
    else:
        reqs_xu_ly = reqs

    tien_token = (runs["tokens_in"] * gia_vao + runs["tokens_out"] * gia_ra) / 1000
    tien_tool = runs["tool_calls"] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs_xu_ly["phut_xem_lai_simulated"].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_xu_ly["phut_lam_lai_simulated"].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = (reqs_xu_ly["ket_qua"] == "thanh_cong").sum()
    return dict(
        token=token, tool=tool, xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
        thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
        chay_lai=(tien_token + tien_tool)[runs["attempt"] > 1].sum(),
        hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan,
        so_lan_chay=len(runs),
    )


def in_bang(tieu_de, dong):
    print(f"\n{tieu_de}")
    print(pd.DataFrame(dong).to_string(index=False))


def in_chi_phi(runs, reqs, goc, pham_vi):
    hang_muc = {
        "Token (đ)": "token",
        "Tool (đ)": "tool",
        "Token + tool lần 2 trở đi (đ)": "chay_lai",
        "Xem lại (đ, simulated)": "xem_lai",
        "Làm lại (đ, simulated)": "lam_lai",
        "Tổng (đ, simulated)": "tong",
        "Số việc thành công": "thanh_cong",
        "CPS (đ, simulated)": "cps",
        "Hóa đơn token + tool / yêu cầu (đ)": "hoa_don_moi_yc",
    }
    in_bang("A2 · Chi phí từ trace", [
        {"Khoản": ten, "Giá trị": f"{goc[khoa]:,.2f}"} for ten, khoa in hang_muc.items()
    ])
    lon_nhat = max(("token", "tool", "xem_lai", "lam_lai"), key=goc.__getitem__)
    print(f"CPS / hóa đơn mỗi yêu cầu (simulated): {goc['cps'] / goc['hoa_don_moi_yc']:.2f}×")
    print(f"Khoản lớn nhất (simulated): {lon_nhat}, {goc[lon_nhat] / goc['tong']:.2%}")

    dong = []
    for loai in CAC_LOAI:
        nhom = reqs[reqs["loai"] == loai]
        kq = mo_hinh(runs, nhom)
        dong.append({
            "Loại": loai,
            "Yêu cầu": len(nhom),
            "Thành công": f"{kq['thanh_cong'] / len(nhom):.2%}",
            "Lần chạy / yêu cầu": f"{kq['so_lan_chay'] / len(nhom):.2f}",
            "CPS (đ, simulated)": f"{kq['cps']:,.2f}",
            "So với 12.000 đ (simulated)": f"{kq['cps'] / BASELINE:.4f}×",
        })
    in_bang("A3 · Chi phí theo loại", dong)

    trace = runs.merge(reqs[["request_id", "loai"]], on="request_id")
    trace["ok"] = trace["status"] == "ok"
    ti_le_ok = trace.pivot_table(index="loai", columns="attempt", values="ok")
    print("\nA3 · Tỉ lệ status = ok trên các lần chạy thực hiện ở mỗi attempt")
    print(ti_le_ok.to_string(float_format="{:.2%}".format))

    kq = mo_hinh(runs, pham_vi)
    dong = []
    for khoi_luong in (45000, 22500):
        # Khối lượng toàn hệ thống, với cơ cấu yêu cầu như trong mẫu.
        thanh_cong_thang = khoi_luong * kq["thanh_cong"] / len(reqs)
        co_dinh = 40_000_000 / thanh_cong_thang
        cps = kq["cps"] + co_dinh
        dong.append({
            "Yêu cầu/tháng": khoi_luong,
            "Việc thành công/tháng": f"{thanh_cong_thang:,.0f}",
            "Cố định/việc (đ)": f"{co_dinh:,.2f}",
            "CPS + cố định (đ, simulated)": f"{cps:,.2f}",
            "So với 12.000 đ (simulated)": f"{cps / BASELINE:.4f}×",
        })
    in_bang("A4 · Chi phí cố định cho noi_dia + hang_nang", dong)



def in_do_nhay(runs, reqs, goc, pham_vi):
    token_gap_doi = dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA)
    kich_ban = [
        ("Giá token", "Giá token gấp đôi", token_gap_doi),
        ("Giá token", "Giá token giảm một nửa", dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)),
        ("Xem lại", "Xem lại gấp đôi", dict(he_so_xem_lai=2)),
        ("Xem lại", "Xem lại giảm một nửa", dict(he_so_xem_lai=0.5)),
        ("Làm lại", "Làm lại gấp đôi", dict(he_so_lam_lai=2)),
        ("Làm lại", "Làm lại giảm một nửa", dict(he_so_lam_lai=0.5)),
        ("Lương", "Lương tăng 25%", dict(luong_phut=LUONG_PHUT * 1.25)),
        ("Giới hạn chạy", "Tối đa 2 lần chạy", dict(max_lan_chay=2)),
        ("Giới hạn chạy", "Chỉ 1 lần chạy", dict(max_lan_chay=1)),
    ]
    dong, tac_dong = [], {}
    for yeu_to, ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        thay_doi = cps / goc["cps"] - 1
        tac_dong[yeu_to] = max(tac_dong.get(yeu_to, 0), abs(thay_doi))
        dong.append({
            "Kịch bản": ten,
            "CPS (đ, simulated)": f"{cps:,.2f}",
            "Thay đổi (simulated)": f"{thay_doi:+.2%}",
        })
    in_bang(f"B1 · Độ nhạy (CPS gốc {goc['cps']:,.2f} đ, simulated)", dong)

    cps = mo_hinh(runs, reqs, **token_gap_doi, he_so_xem_lai=2)["cps"]
    print(f"\nB2 · Token và xem lại gấp đôi (simulated): {cps:,.2f} đ, "
          f"{cps / goc['cps'] - 1:+.2%}")
    hang = sorted(tac_dong, key=tac_dong.get, reverse=True)[:3]
    print("Ba yếu tố mạnh nhất (simulated): "
          + " · ".join(f"{ten} {tac_dong[ten]:.2%}" for ten in hang))

    dong, he_thong, cps_theo_k = [], {}, {}
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq["thanh_cong"]
        he_thong[k] = kq["tong"] + BASELINE * khong_thanh_cong
        cps_theo_k[k] = kq["cps"]
        dong.append({
            "Giới hạn": k,
            "Trợ lý (đ, simulated)": f"{kq['tong']:,.2f}",
            "Không thành công": khong_thanh_cong,
            "Cả hệ thống (đ, simulated)": f"{he_thong[k]:,.2f}",
            "CPS trợ lý (đ, simulated)": f"{kq['cps']:,.2f}",
        })
    in_bang("B3 · Chi phí theo giới hạn chạy", dong)
    print(f"Thấp nhất (simulated): hệ thống {min(he_thong, key=he_thong.get)} lần, "
          f"CPS trợ lý {min(cps_theo_k, key=cps_theo_k.get)} lần.")

    kq = mo_hinh(runs, pham_vi)
    co_goi_y = runs["request_id"].isin(pham_vi["request_id"]) & (runs["status"] == "ok")
    so_xem_lai = runs.loc[co_goi_y, "request_id"].nunique()
    so_lam_lai = (pham_vi["ket_qua"] == "lam_lai").sum()
    trung_binh = reqs.loc[reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"].mean()
    xem_lai = so_xem_lai * 5 * LUONG_PHUT
    hoa_don = kq["token"] + kq["tool"]
    dong = []
    for nhan, lam_lai in (
        ("9 phút/ca theo đề", so_lam_lai * 9 * LUONG_PHUT),
        (f"{trung_binh:.4f} phút/ca toàn mẫu (simulated)", so_lam_lai * trung_binh * LUONG_PHUT),
        ("Phút làm lại trong phạm vi (simulated)", kq["lam_lai"]),
    ):
        cps = (hoa_don + xem_lai + lam_lai) / kq["thanh_cong"]
        hoa_von = (BASELINE * kq["thanh_cong"] - hoa_don - lam_lai) / (so_xem_lai * LUONG_PHUT)
        dong.append({
            "Cách tính làm lại": nhan,
            "Làm lại (đ, simulated)": f"{lam_lai:,.2f}",
            "CPS (đ, simulated)": f"{cps:,.2f}",
            "So với 12.000 đ (simulated)": f"{cps / BASELINE:.4f}×",
            "Hòa vốn (phút xem lại, simulated)": f"{hoa_von:.2f}",
        })
    print(f"\nB4 · {len(pham_vi)} yêu cầu, {so_xem_lai} có lần chạy ok, "
          f"{so_lam_lai} làm lại, {kq['thanh_cong']} thành công.")
    print(f"Token + tool: {hoa_don:,.2f} đ. Xem lại 5 phút/gợi ý: {xem_lai:,.2f} đ (simulated).")
    in_bang("B4 · Xem lại 100% yêu cầu có gợi ý trong noi_dia + hang_nang", dong)



def co_mau(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm theo công thức hai tỉ lệ trong đề."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu_so = za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil((tu_so / (p2 - p1)) ** 2)


def in_co_mau():
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n5 = co_mau(p1, 0.75, alpha, power)
    n6 = co_mau(p1, 0.76, alpha, power)
    m, nhan_vien, depot = 75, 20, 6
    de = 1 + (m - 1) * icc
    n_cum = math.ceil(n5 * de)
    m6 = math.ceil(n6 * (1 - icc) / (nhan_vien - n6 * icc))
    de6 = 1 + (m6 - 1) * icc
    power5 = NormalIndPower().power(
        abs(proportion_effectsize(p1, 0.75)), nobs1=n6, alpha=alpha, ratio=1,
    )

    print("\nD1 · Cỡ mẫu mỗi nhóm (baseline 0,70, alpha 0,05, power 0,80, ICC 0,02)")
    print(f"a) Chia theo yêu cầu, +5 điểm: {n5:,} yêu cầu mỗi nhóm (DE = 1).")
    print(f"b) Theo nhân viên, m = {m}: DE = {de:.2f}, cần {n_cum:,} yêu cầu "
          f"và {math.ceil(n_cum / m)} nhân viên mỗi nhóm.")
    print(f"c) {nhan_vien} nhân viên mỗi nhóm: {nhan_vien * m / de:.2f} yêu cầu hiệu dụng "
          f"ở m = {m}, giới hạn tiệm cận {nhan_vien / icc:,.0f}.")
    print(f"d) {depot} depot mỗi nhóm: giới hạn tiệm cận {depot / icc:,.0f} yêu cầu hiệu dụng.")
    print(f"e) +6 điểm: cần {n6} yêu cầu hiệu dụng mỗi nhóm, tối thiểu {m6} yêu cầu/nhân viên "
          f"với {nhan_vien} nhân viên/nhóm, DE = {de6:.2f}, "
          f"hiệu dụng {nhan_vien * m6 / de6:.2f}, thu thập {nhan_vien * m6:,} yêu cầu/nhóm.")
    print(f"Power phát hiện +5 điểm với n hiệu dụng = {n6} mỗi nhóm: {power5:.2%}.")


def in_chi_so(reqs, pham_vi):
    print("\nD3/E1 · Chỉ số tính từ mẫu")
    for ten, nhom in (("Toàn mẫu", reqs), ("noi_dia + hang_nang", pham_vi)):
        mo_lai = nhom["mo_lai_trong_7_ngay"] == 1
        print(f"{ten}, mở lại trong 7 ngày: {mo_lai.sum()}/{len(nhom)} ({mo_lai.mean():.2%}).")
    chinh = (reqs["dong_trong_24h"] == 1) & (reqs["mo_lai_trong_7_ngay"] == 0)
    da_xem = reqs[reqs["duoc_xem_lai"] == 1]
    bo_qua = da_xem["quyet_dinh_xem_lai"].isin(["sua", "bo"])
    print(f"Đóng trong 24 giờ và không mở lại: {chinh.sum()}/{len(reqs)} ({chinh.mean():.2%}).")
    print(f"Sửa hoặc bỏ gợi ý trong số đã xem: {bo_qua.sum()}/{len(da_xem)} ({bo_qua.mean():.2%}).")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv("logix_runs.csv")
    reqs = pd.read_csv("logix_requests.csv", keep_default_na=False)
    goc = mo_hinh(runs, reqs)
    pham_vi = reqs[reqs["loai"].isin(("noi_dia", "hang_nang"))]
    in_chi_phi(runs, reqs, goc, pham_vi)
    in_do_nhay(runs, reqs, goc, pham_vi)
    in_co_mau()
    in_chi_so(reqs, pham_vi)
