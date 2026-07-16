import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 10: TRỰC QUAN HÓA DỮ LIỆU ================")
# Vẽ Scatter Plot thể hiện mối quan hệ ThuNhap và TongChiTieu
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_khachhang, 
    x='ThuNhap', 
    y='TongChiTieu', 
    hue='GioiTinh', 
    palette={'Nam': 'blue', 'Nữ': 'pink'},
    alpha=0.8
)

plt.title('Mối quan hệ giữa Thu Nhập và Tổng Chi Tiêu')
plt.xlabel('Thu Nhập (VND)')
plt.ylabel('Tổng Chi Tiêu (VND)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()