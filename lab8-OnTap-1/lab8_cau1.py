import numpy as np
import pandas as pd

# Thiết lập seed để kết quả ngẫu nhiên có thể tái lập được
np.random.seed(42)

# 1. Tạo MaKH từ 'KH001' đến 'KH500'
ma_kh = [f'KH{i:03d}' for i in range(1, 501)]

# 2. Tuoi: Ngẫu nhiên từ 18 đến 70. Chèn cố tình 10 giá trị NaN
tuoi = np.random.randint(18, 71, size=500).astype(float)
nan_indices_tuoi = np.random.choice(500, 10, replace=False)
tuoi[nan_indices_tuoi] = np.nan

# 3. ThuNhap: Ngẫu nhiên từ 5tr đến 50tr. Chèn 5 giá trị cực trị lên tới 200tr
thu_nhap = np.random.uniform(5_000_000, 50_000_000, size=500)
outlier_indices = np.random.choice(500, 5, replace=False)
thu_nhap[outlier_indices] = 200_000_000

# 4. GioiTinh: Ngẫu nhiên ['Nam', 'Nữ']. Chèn 15 giá trị NaN
gioi_tinh = np.random.choice(['Nam', 'Nữ'], size=500).astype(object)
nan_indices_gioi = np.random.choice(500, 15, replace=False)
gioi_tinh[nan_indices_gioi] = np.nan

# 5. ThanhPho: Ngẫu nhiên ['Hà Nội', 'Đà Nẵng', 'TP.HCM']
thanh_pho = np.random.choice(['Hà Nội', 'Đà Nẵng', 'TP.HCM'], size=500)

# 6. TongChiTieu: Tương quan nhẹ với ThuNhap
tong_chi_tieu = 0.3 * thu_nhap + np.random.normal(5_000_000, 3_000_000, size=500)
tong_chi_tieu = np.clip(tong_chi_tieu, a_min=1_000_000, a_max=None) # Đảm bảo chi tiêu không âm

# Tạo DataFrame
df_khachhang = pd.DataFrame({
    'MaKH': ma_kh,
    'Tuoi': tuoi,
    'ThuNhap': thu_nhap,
    'GioiTinh': gioi_tinh,
    'ThanhPho': thanh_pho,
    'TongChiTieu': tong_chi_tieu
})

print("================ CÂU 1: KHỞI TẠO DỮ LIỆU =========
# Xuất ra file csv tạm để các câu sau đọc lại kế thừa dữ liệu
df_khachhang.to_csv('data_temp.csv', index=False)
print("\n[OK] Đã lưu dữ liệu tạm vào file 'data_temp.csv' để phục vụ các câu sau.")=======")
print(df_khachhang.head(10))