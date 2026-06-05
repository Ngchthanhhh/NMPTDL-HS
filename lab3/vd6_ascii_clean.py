import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step5_output.csv")
output_file = os.path.join(data_dir, "step6_output.csv")

df = pd.read_csv(input_file)

# Dùng Regex để loại bỏ các ký tự lạ (như dấu é trong Mickéy, dấu ö trong Scööpy)
df['Firstname'] = df['Firstname'].replace({r'[^\x00-\x7F]+': ''}, regex=True)
df['Lastname'] = df['Lastname'].replace({r'[^\x00-\x7F]+': ''}, regex=True)

print("--- Kết quả Vấn đề 6 (Làm sạch ASCII) ---")
print(df[['Id', 'Firstname', 'Lastname']].head(10))

df.to_csv(output_file, index=False)
print(f"-> Đã lưu thành công: {output_file}")