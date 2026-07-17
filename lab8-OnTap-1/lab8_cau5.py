import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 5: CHUẨN HÓA DỮ LIỆU ================")
# Khởi tạo MinMaxScaler
scaler = MinMaxScaler()

# Chuẩn hóa cột TongChiTieu về dải [0, 1] và lưu vào cột mới TongChiTieu_Scaled
df_khachhang['TongChiTieu_Scaled'] = scaler.fit_transform(df_khachhang[['TongChiTieu']])

print("5 dòng đầu tiên sau khi chuẩn hóa TongChiTieu:")
print(df_khachhang[['TongChiTieu', 'TongChiTieu_Scaled']].head())

df_khachhang.to_csv('data_temp.csv', index=False)