import pandas as pd

input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()
df["DT"] = df["DT"].fillna(0).astype(int)
df["T1"] = df["T1"].fillna(df["T1"].mean())
print("=== CÂU 6: XỬ LÝ DỮ LIỆU THIẾU FOR TOÀN BỘ CỘT ĐIỂM CÒN LẠI ===")
cac_cot_diem = []
for i in ["1", "2", "6"]:
    for mon in ["T", "L", "H", "S", "V", "X", "D", "N"]:
        cac_cot_diem.append(f"{mon}{i}")
cac_cot_diem.extend(["DH1", "DH2", "DH3"])
so_luong_cot_xu_ly = 0
for col in cac_cot_diem:
    if col in df.columns and col != "T1":
        if df[col].isna().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())
            so_luong_cot_xu_ly += 1

print(
    f"-> Kết quả: Đã xử lý dữ liệu thiếu bằng Mean cho {so_luong_cot_xu_ly} cột điểm còn lại."
)