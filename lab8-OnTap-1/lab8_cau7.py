import pandas as pd

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 7: GOM NHÓM VÀ THỐNG KÊ ================")
# Tạo lại cột thành phố tạm từ các cột One-hot để dễ dùng groupby
def get_city(row):
    if row['ThanhPho_Hà Nội'] == 1: return 'Hà Nội'
    elif row['ThanhPho_Đà Nẵng'] == 1: return 'Đà Nẵng'
    else: return 'TP.HCM'

df_khachhang['ThanhPho_Temp'] = df_khachhang.apply(get_city, axis=1)

# Tính Mean và Sum của TongChiTieu tương ứng từng ThanhPho
thong_ke = df_khachhang.groupby('ThanhPho_Temp')['TongChiTieu'].agg(['mean', 'sum'])

print("Thống kê chi tiêu theo từng Thành Phố:")
print(thong_ke)