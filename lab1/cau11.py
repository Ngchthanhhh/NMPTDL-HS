import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
output_path = r"D:\NMPTDL\Lab1\processed_dulieuxettuyendaihoc.csv"

df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()

# 1. Xử lý khuyết thiếu (Câu 4, 5, 6)
df["DT"] = df["DT"].fillna(0).astype(int)
for col in (
    [f"{m}{i}" for i in range(1, 7) for m in ["T", "L", "H", "S", "V", "X", "D", "N"]]
    + ["DH1", "DH2", "DH3"]
):
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())


# 2. Tính TBM tích hợp 2 học kỳ (Câu 7)
def hk_calc(d, k):
    return (
        d[f"T{k}"] * 2
        + d[f"L{k}"]
        + d[f"H{k}"]
        + d[f"S{k}"]
        + d[f"V{k}"] * 2
        + d[f"X{k}"]
        + d[f"D{k}"]
        + d[f"N{k}"]
    ) / 10


df["TBM1"] = (hk_calc(df, 1) + hk_calc(df, 2)) / 2
df["TBM2"] = (hk_calc(df, 3) + hk_calc(df, 4)) / 2
df["TBM3"] = (hk_calc(df, 5) + hk_calc(df, 6)) / 2


# 3. Phân loại Học lực (Câu 8)
def xl(tbm):
    return (
        "Y"
        if tbm < 5
        else (
            "TB" if tbm < 6.5 else ("K" if tbm < 8 else ("G" if tbm < 9 else "XS"))
        )
    )


df["XL1"] = df["TBM1"].apply(xl)
df["XL2"] = df["TBM2"].apply(xl)
df["XL3"] = df["TBM3"].apply(xl)


# 4. Chuẩn hóa Min-Max thực tế theo dải dữ liệu (Câu 9)
def min_max_norm(series):
    return ((series - series.min()) / (series.max() - series.min())) * 4


df["US_TBM1"] = min_max_norm(df["TBM1"])
df["US_TBM2"] = min_max_norm(df["TBM2"])
df["US_TBM3"] = min_max_norm(df["TBM3"])


# 5. Thuật toán Xét tuyển Đại học (Câu 10)
def xt(row):
    k = str(row["KT"]).strip()
    d1, d2, d3 = row["DH1"], row["DH2"], row["DH3"]
    diem = (
        (d1 * 2 + d2 + d3) / 4
        if k in ["A", "A1"]
        else ((d1 + d2 * 2 + d3) / 4 if k == "B" else (d1 + d2 + d3) / 3)
    )
    return 1 if diem >= 5.0 else 0


df["KQXT"] = df.apply(xt, axis=1)

# 6. Xuất lưu trữ file hoàn chỉnh (Câu 11)
print("=== CÂU 11 (CẬP NHẬT): TIẾN HÀNH XUẤT FILE KẾT QUẢ THỰC TẾ ===")
df.to_csv(output_path, index=False)
print(f"\n[SUCCESS] Đã sửa đổi và xuất file dữ liệu chuẩn tại: {output_path}")