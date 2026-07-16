import pandas as pd

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 4: PHÁT HIỆN & XỬ LÝ OUTLIERS ================")
# Tính Q1, Q3 cho cột ThuNhap
Q1 = df_khachhang['ThuNhap'].quantile(0.25)
Q3 = df_khachhang['ThuNhap'].quantile(0.75)
IQR = Q3 - Q1

# Xác định giới hạn trên và giới hạn dưới
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1 (25%): {Q1:,.0f} VND")
print(f"Q3 (75%): {Q3:,.0f} VND")
print(f"IQR: {IQR:,.0f} VND")
print(f"Giới hạn dưới: {lower_bound:,.0f} VND | Giới hạn trên: {upper_bound:,.0f} VND")
print("-" * 50)

# Lọc bỏ các dòng có ThuNhap là Outlier
df_filtered = df_khachhang[(df_khachhang['ThuNhap'] >= lower_bound) & (df_khachhang['ThuNhap'] <= upper_bound)].copy()

print(f"Số lượng dòng ban đầu: {len(df_khachhang)}")
print(f"Số lượng dòng sau khi lọc Outliers: {len(df_filtered)}")

# Cập nhật và lưu lại dữ liệu sạch
df_khachhang = df_filtered
df_khachhang.to_csv('data_temp.csv', index=False)