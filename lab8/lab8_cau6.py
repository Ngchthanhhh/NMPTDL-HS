import pandas as pd

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 6: LỌC DỮ LIỆU THEO ĐIỀU KIỆN ================")
# Lọc: Khách hàng là 'Nữ', Tuoi > 30, và ở 'Hà Nội' (ThanhPho_Hà Nội == 1)
df_filtered_nu_hn = df_khachhang[
    (df_khachhang['GioiTinh'] == 'Nữ') & 
    (df_khachhang['Tuoi'] > 30) & 
    (df_khachhang['ThanhPho_Hà Nội'] == 1)
]

print(f"Tìm thấy {len(df_filtered_nu_hn)} khách hàng thỏa mãn điều kiện.")
print("In ra 5 dòng đầu tiên:")
print(df_filtered_nu_hn.head(5))