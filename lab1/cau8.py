import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()

# Pipeline làm sạch và tính TBM chuẩn học kỳ
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

print("=== CÂU 8 (CẬP NHẬT): TẠO CÁC BIẾN XẾP LOẠI XL1, XL2, XL3 ===")


def phan_loai_hl(tbm):
    if tbm < 5.0:
        return "Y"
    elif tbm < 6.5:
        return "TB"
    elif tbm < 8.0:
        return "K"
    elif tbm < 9.0:
        return "G"
    else:
        return "XS"


df["XL1"] = df["TBM1"].apply(phan_loai_hl)
df["XL2"] = df["TBM2"].apply(phan_loai_hl)
df["XL3"] = df["TBM3"].apply(phan_loai_hl)

print("-> Kết quả: Đã cập nhật xong bảng xếp loại XL1, XL2, XL3 thực tế.")
print(df[["TBM1", "XL1", "TBM2", "XL2", "TBM3", "XL3"]].head(5))