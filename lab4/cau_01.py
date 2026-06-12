# -*- coding: utf-8 -*-
import os
import pandas as pd

def run():
    print("\n--- CÂU 1: ĐỌC VÀ HIỂN THỊ THÔNG TIN DỮ LIỆU ---")
    data_dir = r"D:\NMPTDL-HS\DuLieu"
    # Tìm kiếm file dữ liệu trong thư mục (Giả định có file data.csv hoặc tương tự)
    file_path = os.path.join(data_dir, "data.csv")
    
    # Tạo dữ liệu giả lập nếu file chưa tồn tại để demo chạy mượt mà
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(file_path):
        import numpy as np
        np.random.seed(42)
        df_demo = pd.DataFrame({
            'Age': np.random.randint(18, 60, size=100),
            'Salary': np.random.randint(20000, 150000, size=100),
            'Experience': np.random.randint(0, 15, size=100),
            'Education': np.random.choice(['Bachelor', 'Master', 'PhD'], size=100),
            'Target': np.random.choice([0, 1], size=100)
        })
        # Thêm một ít dữ liệu khuyết thiếu và trùng lặp để các câu sau xử lý
        df_demo.loc[5:10, 'Salary'] = np.nan
        df_demo.loc[15:17, 'Age'] = np.nan
        df_demo = pd.concat([df_demo, df_demo.iloc[[0, 1, 2]]], ignore_index=True)
        df_demo.to_csv(file_path, index=False)
        print(f"Đã tạo tập dữ liệu mẫu tại: {file_path}")

    # Đọc dữ liệu
    df = pd.read_csv(file_path)
    print(f"Kích thước tập dữ liệu (Shape): {df.shape}")
    print("\n5 dòng đầu tiên của dữ liệu:")
    print(df.head())
    print("\nThông tin cấu trúc dữ liệu (Info):")
    df.info()
    return df

if __name__ == "__main__":
    run()
