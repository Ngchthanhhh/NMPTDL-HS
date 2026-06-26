# LAB 2 - PHẦN 4: TRỰC QUAN NÂNG CAO (FILE REAL CSV)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lab2_phandanhgia_helper import load_real_data

print("--- PHẦN 4: TRỰC QUAN HÓA DỮ LIỆU NÂNG CAO ---")
df = load_real_data()

# 1. Biểu đồ đường Simple cho biến T1
plt.figure(figsize=(8, 4))
plt.plot(df['T1'].sort_values().values, color='purple', label='Môn Toán (T1)')
plt.title("Biểu đồ đường Simple cho biến T1 (Đang tăng dần)")
plt.ylabel("Điểm số")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 2. Tạo biến phân loại phanlopt1
def phan_lop_t1(score):
    if score < 5: return 'k'
    elif score < 7: return 'tb'
    elif score < 8: return 'kh'
    else: return 'g'

df['phanlopt1'] = df['T1'].apply(phan_lop_t1)

# 3. Lập bảng tần số cho biến phanlopt1
print("\n3. Bảng tần số biến phân lớp phanlopt1:\n", df['phanlopt1'].value_counts())

# 4. Biểu đồ đường Multiple Line cho biến T1 được phân loại bởi phanlopt1
plt.figure(figsize=(8, 4))
for label, group in df.groupby('phanlopt1'):
    plt.plot(group['T1'].index, group['T1'].values, 'o', label=f'Học lực: {label}')
plt.title("Biểu đồ phân bộ điểm theo các nhóm học lực phân loại")
plt.xlabel("Index dòng")
plt.ylabel("Điểm T1")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 5. Biểu đồ Drop-line cho biến T1
plt.figure(figsize=(11, 4))
colors = {'k': 'red', 'tb': 'orange', 'kh': 'blue', 'g': 'green'}
for i in range(min(len(df), 100)): # Giới hạn tối đa 100 dòng đầu để tránh drop-line quá dày đặc
    row = df.iloc[i]
    plt.vlines(x=i, ymin=0, ymax=row['T1'], colors=colors[row['phanlopt1']], alpha=0.6)
plt.title("Biểu đồ Drop-line cho biến T1 phân loại bởi phanlopt1 (Trích xuất chuỗi)")
plt.ylabel("Điểm T1")
plt.show()