# LAB 2 - PHẦN 5: KHẢO SÁT PHÂN PHỐI CHUẨN (FILE REAL CSV)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from lab2_phandanhgia_helper import load_real_data

print("--- PHẦN 5: MÔ TẢ DỮ LIỆU VÀ KHẢO SÁT DẠNG PHÂN PHỐI ---")
df = load_real_data()

# 1. Mô tả tập trung và phân tán của T1
print("\n1. Mô tả các đại lượng thống kê biến T1:\n", df['T1'].describe())
print("Độ lệch (Skewness):", df['T1'].skew())
print("Độ nhọn (Kurtosis):", df['T1'].kurt())

# Biểu đồ Box-Plot, Histogram và QQ-Plot của T1
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.boxplot(y=df['T1'], ax=axes[0], color='cyan')
axes[0].set_title("Box-Plot của T1")

sns.histplot(df['T1'], kde=True, ax=axes[1], color='darkblue')
axes[1].set_title("Histogram của T1")

stats.probplot(df['T1'], dist="norm", plot=axes[2])
axes[2].set_title("QQ-Plot kiểm chứng phân phối chuẩn")

plt.tight_layout()
plt.show()

# 3. Khảo sát tương quan giữa biến DH1 và T1
cov_val = df['DH1'].cov(df['T1'])
corr_val = df['DH1'].corr(df['T1'])
print(f"\n3. Hiệp phương sai (Covariance) giữa DH1 và T1: {cov_val:.4f}")
print(f"   Hệ số tương quan (Correlation) giữa DH1 và T1: {corr_val:.4f}")

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='T1', y='DH1', color='purple')
plt.title("Biểu đồ Scatter tương quan giữa điểm xét tuyển DH1 và điểm toán T1")
plt.show()

# 5. Khảo sát ma trận tương quan giữa các biến DH1, DH2, DH3
print("\n5. Ma trận tương quan giữa 3 biến thi đại học DH1, DH2, DH3:\n", df[['DH1', 'DH2', 'DH3']].corr())