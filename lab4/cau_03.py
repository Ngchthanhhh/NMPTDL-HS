# -*- coding: utf-8 -*-
import pandas as pd

def run(df=None):
    print("\n--- CÂU 3: KIỂM TRA VÀ XỬ LÝ DỮ LIỆU TRÙNG LẶP ---")
    if df is None:
        import cau_02
        df = cau_02.run()
        
    duplicate_count = df.duplicated().sum()
    print(f"Số lượng dòng trùng lặp phát hiện: {duplicate_count}")
    
    # Loại bỏ dữ liệu trùng lặp
    df_no_dup = df.drop_duplicates().reset_index(drop=True)
    print(f"Kích thước dữ liệu sau khi xóa trùng lặp: {df_no_dup.shape}")
    return df_no_dup

if __name__ == "__main__":
    run()
