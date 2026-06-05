import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step6_output.csv")
output_file = os.path.join(data_dir, "step7_output.csv")

df = pd.read_csv(input_file)

# 1. Thống kê thông tin dữ liệu thiếu
print("--- THỐNG KÊ DỮ LIỆU THIẾU (Trước xử lý) ---")
print(df[['Age', 'Weight']].isnull().sum())

# 2. Xử lý logic tính toán cho Weight (Tách chữ 'kgs' để lấy số)
weight_num = df['Weight'].astype(str).str.replace('kgs', '', regex=False)
weight_num = pd.to_numeric(weight_num, errors='coerce')
df['Weight_num'] = weight_num

# 3. Xóa dòng nếu thiếu cả Age và Weight
df.dropna(subset=['Age', 'Weight_num'], how='all', inplace=True)

# 4. Điền giá trị trung bình (mean) cho Age và Weight_num
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Weight_num'] = df['Weight_num'].fillna(df['Weight_num'].mean())

# 5. Định dạng lại cột Weight cho đẹp (ví dụ 70.0 -> 70kgs)
df['Weight'] = df['Weight_num'].round(0).astype(int).astype(str) + "kgs"
df = df.drop('Weight_num', axis=1) # Xóa cột tạm

print("\n--- KẾT QUẢ VẤN ĐỀ 7 (Sau xử lý) ---")
print(df[['Id', 'Age', 'Weight']].head())

df.to_csv(output_file, index=False)
print(f"-> Đã lưu thành công: {output_file}")