import pandas as pd
input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()
print("=== CÂU 4: THỐNG KÊ VÀ XỬ LÝ KHUYẾT CỘT DÂN TỘC (DT) ===")
dieu_kien_rieng_biet = df["DT"].unique()
print(f"1. Các dữ liệu riêng biệt (pandas unique): {dieu_kien_rieng_biet}")
tanso_dt = df["DT"].value_counts(dropna=False)
tansuat_dt = df["DT"].value_counts(dropna=False, normalize=True) * 100
thongke_dt = pd.DataFrame({"Tần số": tanso_dt, "Tần suất (%)": tansuat_dt})
print("\n2. Bảng thống kê tần số & tần suất của cột DT trước khi xử lý:")
print(thongke_dt)
df["DT"] = df["DT"].fillna(0).astype(int)
print("\n3. Kiểm tra 10 dòng đầu của cột DT trong RAM sau khi điền:")
print(df["DT"].head(10))
print("\n-> Kết quả: Đã xử lý điền số 0 thành công trong bộ nhớ!")