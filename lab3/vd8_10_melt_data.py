import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step7_output.csv")
output_file = os.path.join(data_dir, "step8_10_output.csv")

df = pd.read_csv(input_file)

# 1. Melt dataframe (Chuyển dữ liệu từ dạng rộng ngang sang dạng dài dọc)
df = pd.melt(df, 
             id_vars=['Id', 'Age', 'Weight', 'Firstname', 'Lastname'], 
             value_name="PulseRate", 
             var_name="sex_and_time").sort_values(['Id', 'Age', 'Weight', 'Firstname', 'Lastname'])

# 2. Extract (Tách) giới tính và thời gian bằng Regex giống hệt trong slide
tmp_df = df["sex_and_time"].str.extract(r'(\D)(\d{2})(\d{2})', expand=True)
tmp_df.columns = ["Sex", "hours_lower", "hours_upper"]

# 3. Tạo cột Time chuẩn (Ví dụ: 00-06)
tmp_df["Time"] = tmp_df["hours_lower"] + "-" + tmp_df["hours_upper"]

# 4. Gộp vào dataframe gốc và dọn dẹp các cột dư thừa
df = pd.concat([df, tmp_df], axis=1)
df = df.drop(['sex_and_time', 'hours_lower', 'hours_upper'], axis=1)

# Xử lý các dấu '-' trong PulseRate thành định dạng NaN (Khuyết) chuẩn của Pandas
df['PulseRate'] = df['PulseRate'].replace('-', pd.NA)
df['PulseRate'] = pd.to_numeric(df['PulseRate'], errors='coerce')

print("--- KẾT QUẢ VẤN ĐỀ 8 & 10 (Melt Data) ---")
print(df[['Id', 'Firstname', 'PulseRate', 'Sex', 'Time']].head(6))

df.to_csv(output_file, index=False)
print(f"-> Đã lưu thành công: {output_file}")