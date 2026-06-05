import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step2_output.csv")
output_file = os.path.join(data_dir, "step3_output.csv")

df = pd.read_csv(input_file)

# Ép kiểu về chuỗi để xử lý text
df['Weight'] = df['Weight'].astype(str)

# Tìm những dòng nào có chứa chữ 'lbs'
is_lbs = df['Weight'].str.contains('lbs', na=False)

# Xóa các chữ 'lbs' và 'kgs' để lấy phần số nguyên
weight_numeric = df['Weight'].str.replace('lbs', '', regex=False).str.replace('kgs', '', regex=False)
weight_numeric = pd.to_numeric(weight_numeric, errors='coerce')

# Áp dụng công thức chuyển đổi của giảng viên: chia 2.2 và lấy phần nguyên
weight_numeric[is_lbs] = (weight_numeric[is_lbs] / 2.2).astype(int)

# Gắn lại chữ 'kgs' vào phía sau và cập nhật lại cột
df['Weight'] = weight_numeric.astype(str).replace('nan', '') + 'kgs'
# Xử lý các dòng rỗng bị biến thành 'kgs'
df['Weight'] = df['Weight'].replace('kgs', pd.NA)

print("Dữ liệu sau khi giải quyết Vấn đề 3 (Đồng bộ đơn vị Weight):")
print(df[['Id', 'Weight']].head(10))

df.to_csv(output_file, index=False)