import pandas as pd
import numpy as np

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 8: KỸ NGHỆ ĐẶC TRƯNG ================")
# Tạo cột NhomTuoi dựa vào Tuoi
bins = [18, 30, 45, 60, np.inf]
labels = ['18-30', '31-45', '46-60', 'Trên 60']

df_khachhang['NhomTuoi'] = pd.cut(df_khachhang['Tuoi'], bins=bins, labels=labels, include_lowest=True)

print("Kết quả phân nhóm tuổi (5 dòng đầu):")
print(df_khachhang[['Tuoi', 'NhomTuoi']].head())

df_khachhang.to_csv('data_temp.csv', index=False)