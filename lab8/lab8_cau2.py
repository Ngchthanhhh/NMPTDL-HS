import pandas as pd

# Đọc lại dữ liệu từ câu 1
df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 2: XỬ LÝ GIÁ TRỊ KHUYẾT ================")
print("Số lượng giá trị khuyết TRƯỚC khi xử lý:")
print(df_khachhang.isnull().sum())
print("-" * 50)

# 1. Điền khuyết cột Tuoi bằng giá trị Trung vị (Median)
median_tuoi = df_khachhang['Tuoi'].median()
df_khachhang['Tuoi'] = df_khachhang['Tuoi'].fillna(median_tuoi)

# 2. Điền khuyết cột GioiTinh bằng giá trị xuất hiện nhiều nhất (Mode)
mode_gioitinh = df_khachhang['GioiTinh'].mode()[0]
df_khachhang['GioiTinh'] = df_khachhang['GioiTinh'].fillna(mode_gioitinh)

print("Số lượng giá trị khuyết SAU khi xử lý:")
print(df_khachhang.isnull().sum())

# Lưu lại tiến trình
df_khachhang.to_csv('data_temp.csv', index=False)