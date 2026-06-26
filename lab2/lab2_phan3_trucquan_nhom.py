# LAB 2 - PHẦN 3: TRỰC QUAN HÓA THEO NHÓM (FILE REAL CSV)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lab2_phandanhgia_helper import load_real_data

print("--- PHẦN 3: TRỰC QUAN HÓA DỮ LIỆU THEO NHÓM PHÂN LOẠI ---")
df = load_real_data()

# 1. Học sinh nữ trên các nhóm XL1, XL2, XL3 dạng unstacked
female_val = 'F' if 'F' in df['GT'].values else ('nu' if 'nu' in df['GT'].values else df['GT'].unique()[-1])
df_female = df[df['GT'] == female_val]

cols_xl = [c for c in ['XL1', 'XL2', 'XL3'] if c in df.columns]
if cols_xl:
    xl_melted = df_female.melt(value_vars=cols_xl, var_name='Nhom_XL', value_name='Xep_Loai')
    plt.figure(figsize=(9, 5))
    sns.countplot(data=xl_melted, x='Nhom_XL', hue='Xep_Loai', palette='Set2')
    plt.title(f"Trực quan học sinh Nữ ({female_val}) trên các nhóm Xếp Loại (Unstacked)")
    plt.xlabel("Nhóm Xếp Loại")
    plt.ylabel("Số lượng học sinh")
    plt.show()

# Trực quan các phân hệ Đậu/Rớt và Khối thi / Khu vực
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.countplot(data=df, x='KT', hue='KV', ax=axes[0, 0], palette='pastel')
axes[0, 0].set_title("Số lượng thí sinh từng KV dựa trên Khối thi")

# Kiểm tra nếu file có cột KQXT (Kết quả xét tuyển)
if 'KQXT' in df.columns:
    sns.countplot(data=df, x='KT', hue='KQXT', ax=axes[0, 1], palette='Set1')
    axes[0, 1].set_title("Số lượng thí sinh Đậu/Rớt theo Khối thi")
    
    sns.countplot(data=df, x='KV', hue='KQXT', ax=axes[1, 0], palette='Set1')
    axes[1, 0].set_title("Số lượng thí sinh Đậu/Rớt theo Khu vực")
    
    sns.countplot(data=df, x='GT', hue='KQXT', ax=axes[1, 1], palette='Set1')
    axes[1, 1].set_title("Số lượng thí sinh Đậu/Rớt theo Giới tính")
else:
    print("Mẹo: File dữ liệu thật của ní không có cột 'KQXT', hệ thống vẽ phân bố mặc định thay thế.")
    sns.countplot(data=df, x='KT', ax=axes[0, 1], palette='Set1')
    sns.countplot(data=df, x='KV', ax=axes[1, 0], palette='Set3')
    sns.countplot(data=df, x='GT', ax=axes[1, 1], palette='pastel')

plt.tight_layout()
plt.show()