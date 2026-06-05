import pandas as pd
import os

# Gắn cứng đường dẫn thư mục chứa data
data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step3_output.csv")
output_file = os.path.join(data_dir, "step4_output.csv")

# Đọc file
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file {input_file}. Bro check lại xem đã chạy xong Vấn đề 3 chưa nhé!")
    exit()

# Xóa các dòng mà TẤT CẢ các cột đều là NaN (rỗng hoàn toàn)
df.dropna(how="all", inplace=True)

print("--- Kết quả Vấn đề 4 (Xóa dòng rỗng) ---")
print(df.tail()) 

df.to_csv(output_file, index=False)
print(f"-> Đã lưu thành công: {output_file}")