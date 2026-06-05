import pandas as pd
import os

data_dir = r"D:\NMPTDL-HS\DuLieu"
input_file = os.path.join(data_dir, "step8_10_output.csv")
output_file = os.path.join(data_dir, "patient_heart_rate_clean.csv")

df = pd.read_csv(input_file)

# --- VẤN ĐỀ 11: XỬ LÝ KHUYẾT NHỊP TIM/HUYẾT ÁP ---
# Đảm bảo dữ liệu được sắp xếp đúng bệnh nhân và đúng thứ tự thời gian trước khi tính toán
df = df.sort_values(['Id', 'Time'])

def fill_pulse_rate(group):
    # Bước 1: Thay bằng trung bình liền trước và liền sau
    group = group.fillna((group.shift(1) + group.shift(-1)) / 2)
    # Bước 2: Thay bằng trung bình 2 giá trị liền trước
    group = group.fillna((group.shift(1) + group.shift(2)) / 2)
    # Bước 3: Thay bằng trung bình 2 giá trị liền sau
    group = group.fillna((group.shift(-1) + group.shift(-2)) / 2)
    # Bước 4: Trung bình của toàn bộ các lần đo của người đó
    group = group.fillna(group.mean())
    return group

# Áp dụng hàm điền khuyết cho TỪNG bệnh nhân (groupby Id)
df['PulseRate'] = df.groupby('Id')['PulseRate'].transform(fill_pulse_rate)

# Bước 5: Nếu người đó không đo được lần nào, lấy trung bình theo nhóm giới tính
df['PulseRate'] = df['PulseRate'].fillna(df.groupby('Sex')['PulseRate'].transform('mean'))

# Bước 6: Nếu nhóm giới tính cũng không có, lấy trung bình toàn dữ liệu hoặc mức ổn định y học (ví dụ: 70)
df['PulseRate'] = df['PulseRate'].fillna(df['PulseRate'].mean()).fillna(70)

# Làm tròn huyết áp/nhịp tim cho thực tế
df['PulseRate'] = df['PulseRate'].round(0)


# --- VẤN ĐỀ 12: REINDEX VÀ LƯU TRỮ ---
df = df.sort_values(['Id', 'Time']).reset_index(drop=True)

print("--- KẾT QUẢ VẤN ĐỀ 11 & 12 (Hoàn thành Lab 3) ---")
print(df.head(10))

df.to_csv(output_file, index=False)
print(f"-> Đã lưu file cuối cùng thành công: {output_file}")