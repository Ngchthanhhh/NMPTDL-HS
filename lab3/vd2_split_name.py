import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step1_output.csv")
output_file = os.path.join(data_dir, "step2_output.csv")

df = pd.read_csv(input_file)

# Tách cột Name thành Firstname và Lastname, sau đó xóa cột Name gốc
df[['Firstname', 'Lastname']] = df['Name'].str.split(expand=True)
df = df.drop('Name', axis=1)

print("Dữ liệu sau khi giải quyết Vấn đề 2 (Tách cột Name):")
print(df.head())

df.to_csv(output_file, index=False)