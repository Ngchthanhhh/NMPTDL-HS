# LAB 2 - PHẦN 1: THỐNG KÊ DỮ LIỆU (FILE REAL CSV)
import pandas as pd
from lab2_phandanhgia_helper import load_real_data, agg_funcs

print("--- PHẦN 1: THỐNG KÊ DỮ LIỆU ---")
df = load_real_data()

# 1. Sắp xếp điểm DH1 theo thứ tự tăng dần
df_sorted_dh1 = df.sort_values(by='DH1')
print("\n1. Top 5 dòng sau khi sắp xếp điểm DH1 tăng dần:\n", df_sorted_dh1[['GT', 'KT', 'DH1']].head())

# 2. Sắp xếp điểm DH2 tăng dần theo nhóm giới tính
df_sorted_dh2_gt = df.sort_values(by=['GT', 'DH2'])
print("\n2. Top 5 dòng sau khi sắp xếp DH2 tăng dần theo Giới tính:\n", df_sorted_dh2_gt[['GT', 'DH2']].head())

# 3. Pivot-table thống kê DH1 theo KT
pivot_kt = df.pivot_table(values='DH1', index='KT', aggfunc=agg_funcs)
print("\n3. Bảng Pivot-table thống kê điểm DH1 theo KT:\n", pivot_kt.head())

# 4. Pivot-table thống kê DH1 theo KT và KV
pivot_kt_kv = df.pivot_table(values='DH1', index=['KT', 'KV'], aggfunc=agg_funcs)
print("\n4. Bảng Pivot-table thống kê điểm DH1 theo KT và KV:\n", pivot_kt_kv.head())

# 5. Pivot-table thống kê DH1 theo KT, KV và DT
# Kiểm tra nếu file có cột DT thì chạy, tránh lỗi lệch cấu trúc file
if 'DT' in df.columns:
    pivot_kt_kv_dt = df.pivot_table(values='DH1', index=['KT', 'KV', 'DT'], aggfunc=agg_funcs)
    print("\n5. Bảng Pivot-table thống kê điểm DH1 theo KT, KV và DT:\n", pivot_kt_kv_dt.head())
else:
    print("\n5. Cảnh báo: File CSV không chứa cột 'DT' (Dân tộc).")