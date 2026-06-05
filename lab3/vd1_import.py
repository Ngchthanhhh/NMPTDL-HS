import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "patient_heart_rate.csv")
output_file = os.path.join(data_dir, "step1_output.csv")

# Danh sách các cột cần thêm (giống hệt trong slide)
column_names = ["Id", "Name", "Age", "Weight", 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']

# Đọc file và chèn header
df = pd.read_csv(input_file, names=column_names)

print("Dữ liệu sau khi giải quyết Vấn đề 1 (Thêm Header):")
print(df.head())

df.to_csv(output_file, index=False)