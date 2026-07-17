import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_khachhang = pd.read_csv('data_temp.csv')

print("================ CÂU 9: MA TRẬN TƯƠNG QUAN ================")
# Tính ma trận tương quan Pearson
correlation_matrix = df_khachhang[['Tuoi', 'ThuNhap', 'TongChiTieu']].corr(method='pearson')
print("Ma trận tương quan Pearson:")
print(correlation_matrix)

# Vẽ heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Ma trận tương quan Pearson giữa Tuoi, ThuNhap và TongChiTieu')
plt.show()