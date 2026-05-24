import pandas as pd
input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()
df["DT"] = df["DT"].fillna(0).astype(int)
print("=== CÂU 5: THỐNG KÊ VÀ XỬ LÝ KHUYẾT CỘT ĐIỂM TOÁN LỚP 10 (T1) ===")
tanso_t1 = df["T1"].value_counts(dropna=False)
tansuat_t1 = df["T1"].value_counts(dropna=False, normalize=True) * 100
thongke_t1 = pd.DataFrame({"Tần số": tanso_t1, "Tần suất (%)": tansuat_t1})
print("Bảng thống kê tần số & tần suất của T1 (5 dòng đầu):")
print(thongke_t1.head(5))
gia_tri_mean = df["T1"].mean()
df["T1"] = df["T1"].fillna(gia_tri_mean)
print(
    f"\n-> Kết quả: Đã điền giá trị Mean ({gia_tri_mean:.2f}) cho các vị trí thiếu ở cột T1 (nếu có)."
)