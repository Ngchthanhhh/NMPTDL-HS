import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()

# Pipeline làm sạch câu trước
df["DT"] = df["DT"].fillna(0).astype(int)
for col in (
    [f"{m}{i}" for i in range(1, 7) for m in ["T", "L", "H", "S", "V", "X", "D", "N"]]
    + ["DH1", "DH2", "DH3"]
):
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())

print("=== CÂU 10: TẠO BIẾN KẾT QUẢ XẾP TUYỂN (KQXT) ===")


def thuat_toan_xet_tuyen(row):
    khoi_thi = str(row["KT"]).strip()
    dh1, dh2, dh3 = row["DH1"], row["DH2"], row["DH3"]
    if khoi_thi in ["A", "A1"]:
        diem_tong_ket = (dh1 * 2 + dh2 + dh3) / 4
    elif khoi_thi == "B":
        diem_tong_ket = (dh1 + dh2 * 2 + dh3) / 4
    else:
        diem_tong_ket = (dh1 + dh2 + dh3) / 3
    return 1 if diem_tong_ket >= 5.0 else 0


df["KQXT"] = df.apply(thuat_toan_xet_tuyen, axis=1)
print("-> Kết quả: Thống kê số lượng học sinh Đậu (1) / Rớt (0):")
print(df["KQXT"].value_counts())