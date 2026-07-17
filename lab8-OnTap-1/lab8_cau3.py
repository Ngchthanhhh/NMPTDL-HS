import pandas as pd

# Đọc tiếp dữ liệu đã được điền khuyết
df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 3: MÃ HÓA BIẾN PHÂN LOẠI ================")
# Áp dụng One-Hot Encoding cho cột ThanhPho và gộp vào DataFrame gốc
df_khachhang = pd.get_dummies(df_khachhang, columns=['ThanhPho'], prefix='ThanhPho', dtype=int)

print("Dữ liệu sau khi One-Hot Encoding cột 'ThanhPho':")
print(df_khachhang.head(5))

# Lưu lại tiến trình
df_khachhang.to_csv('data_temp.csv', index=False)