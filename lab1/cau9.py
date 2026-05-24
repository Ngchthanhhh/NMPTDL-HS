import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()

df["DT"] = df["DT"].fillna(0).astype(int)
for col in (
    [f"{m}{i}" for i in range(1, 7) for m in ["T", "L", "H", "S", "V", "X", "D", "N"]]
    + ["DH1", "DH2", "DH3"]
):
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())


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

print("=== CÂU 9 (SỬA ĐỔI): CHUYỂN ĐỔI MIN-MAX CHUẨN THEO DỮ LIỆU THỰC TẾ ===")


# Định nghĩa hàm chuẩn hóa Min-Max thực tế: (X - min) / (max - min) * 4
def bieu_dien_min_max(series):
    v_min = series.min()
    v_max = series.max()
    return ((series - v_min) / (v_max - v_min)) * 4


df["US_TBM1"] = bieu_dien_min_max(df["TBM1"])
df["US_TBM2"] = bieu_dien_min_max(df["TBM2"])
df["US_TBM3"] = bieu_dien_min_max(df["TBM3"])

print("-> Kết quả: Quy đổi điểm số dựa trên min/max thực tế của tập dữ liệu:")
print(df[["TBM1", "US_TBM1", "TBM2", "US_TBM2", "TBM3", "US_TBM3"]].head(5))