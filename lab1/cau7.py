import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()

# Pipeline làm sạch tự động dữ liệu khuyết
df["DT"] = df["DT"].fillna(0).astype(int)
for col in (
    [f"{m}{i}" for i in range(1, 7) for m in ["T", "L", "H", "S", "V", "X", "D", "N"]]
    + ["DH1", "DH2", "DH3"]
):
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())

print("=== CÂU 7 (SỬA ĐỔI): TẠO BIẾN ĐIỂM TRUNG BÌNH CẢ NĂM TBM1, TBM2, TBM3 ===")


# Hàm phụ trợ tính điểm trung bình môn cho một học kỳ cụ thể (kỳ 1 đến kỳ 6)
def tinh_tbm_hk(df_data, hk):
    return (
        df_data[f"T{hk}"] * 2
        + df_data[f"L{hk}"]
        + df_data[f"H{hk}"]
        + df_data[f"S{hk}"]
        + df_data[f"V{hk}"] * 2
        + df_data[f"X{hk}"]
        + df_data[f"D{hk}"]
        + df_data[f"N{hk}"]
    ) / 10


# TBM cả năm = Trung bình cộng của 2 học kỳ trong năm học đó
df["TBM1"] = (tinh_tbm_hk(df, 1) + tinh_tbm_hk(df, 2)) / 2  # Lớp 10 (HK1 & HK2)
df["TBM2"] = (tinh_tbm_hk(df, 3) + tinh_tbm_hk(df, 4)) / 2  # Lớp 11 (HK3 & HK4)
df["TBM3"] = (tinh_tbm_hk(df, 5) + tinh_tbm_hk(df, 6)) / 2  # Lớp 12 (HK5 & HK6)

print("-> Kết quả: Đã gộp điểm 2 học kỳ để tạo biến TBM1, TBM2, TBM3 hoàn chỉnh.")
print(df[["TBM1", "TBM2", "TBM3"]].head(5))