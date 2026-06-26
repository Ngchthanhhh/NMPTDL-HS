# LAB 2 - PHẦN 2: TRÌNH BÀY DỮ LIỆU (FILE REAL CSV)
import pandas as pd
import matplotlib.pyplot as plt
from lab2_phandanhgia_helper import load_real_data

print("--- PHẦN 2: TRÌNH BÀY DỮ LIỆU ---")
df = load_real_data()

# 1. Trình bày dữ liệu biến GT
freq_gt = df['GT'].value_counts()
pct_gt = df['GT'].value_counts(normalize=True) * 100
table_gt = pd.DataFrame({'Tần số': freq_gt, 'Tần suất (%)': pct_gt})
print("\n1. Bảng tần số & tần suất biến GT:\n", table_gt)

# Vẽ biểu đồ biến GT
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
df['GT'].value_counts().plot(kind='bar', ax=axes[0], color=['skyblue', 'salmon'])
axes[0].set_title("Biểu đồ tần số biến GT (Cột)")
axes[0].set_ylabel("Số lượng")

df['GT'].value_counts().plot(kind='pie', ax=axes[1], autopct='%1.1f%%', colors=['skyblue', 'salmon'])
axes[1].set_title("Biểu đồ tần suất biến GT (Tròn)")
axes[1].set_ylabel("")
plt.tight_layout()
plt.show()

# 2. Trình bày dữ liệu các biến US_TBM1, US_TBM2, US_TBM3 nếu có sẵn trong file
cols_tbm = [c for c in ['US_TBM1', 'US_TBM2', 'US_TBM3'] if c in df.columns]
if cols_tbm:
    print(f"\n2. Mô tả thống kê cho các biến {cols_tbm}:\n", df[cols_tbm].describe())
else:
    print("\n2. Không tìm thấy các cột US_TBM trong file CSV.")

# 3. Biến DT với học sinh nam (Giả định 'M' hoặc 'nam' là Nam trong dữ liệu thật)
male_val = 'M' if 'M' in df['GT'].values else ('nam' if 'nam' in df['GT'].values else df['GT'].unique()[0])
df_male = df[df['GT'] == male_val]
if 'DT' in df.columns:
    print(f"\n3. Tần số biến Dân tộc (DT) đối với học sinh Nam ({male_val}):\n", df_male['DT'].value_counts())

# 4. Trình bày biến KV với học sinh Nam, dân tộc Kinh thỏa điều kiện điểm số
cond_dt = df['DT'] == 'Kinh' if 'DT' in df.columns else True
cond_4 = (df['GT'] == male_val) & cond_dt & (df['DH1'] >= 5.0) & (df['DH2'] >= 4.0) & (df['DH3'] >= 4.0)
df_cond_4 = df[cond_4]
print(f"\n4. Số lượng học sinh thỏa mãn điều kiện 4 (Điểm đạt chuẩn): {len(df_cond_4)}")
if len(df_cond_4) > 0:
    print(df_cond_4['KV'].value_counts())

# 5. Trình bày biến DH1, DH2, DH3 >= 5.0 và thuộc khu vực 2NT
kv_2nt_val = '2NT' if '2NT' in df['KV'].values else df['KV'].unique()[0]
cond_5 = (df['DH1'] >= 5.0) & (df['DH2'] >= 5.0) & (df['DH3'] >= 5.0) & (df['KV'] == kv_2nt_val)
df_cond_5 = df[cond_5]
print(f"\n5. Số lượng học sinh đạt điểm >= 5.0 tại Khu vực {kv_2nt_val}: {len(df_cond_5)}")