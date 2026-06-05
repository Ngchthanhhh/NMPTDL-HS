import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step4_output.csv")
output_file = os.path.join(data_dir, "step5_output.csv")

df = pd.read_csv(input_file)

# Xóa các dòng trùng lặp dựa trên 4 cột định danh cơ bản
df = df.drop_duplicates(subset=['Firstname', 'Lastname', 'Age', 'Weight'])

print("--- Kết quả Vấn đề 5 (Xóa trùng lặp) ---")
print(f"Số dòng hiện tại sau khi xóa trùng: {len(df)}")
print(df.head(10))

df.to_csv(output_file, index=False)
print(f"-> Đã lưu thành công: {output_file}")