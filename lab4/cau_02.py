# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def run(df=None):
    print("\n--- CÂU 2: KIỂM TRA VÀ XỬ LÝ GIÁ TRỊ KHUYẾT THIẾU ---")
    if df is None:
        import cau_01
        df = cau_01.run()
        
    print("\nSố lượng giá trị khuyết thiếu trong mỗi cột:")
    print(df.isnull().sum())
    
    # Xử lý khuyết thiếu bằng cách điền giá trị Trung vị (Median) cho số và Mode cho phân loại
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].dtype in [np.int64, np.float64]:
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)
        else:
            mode_val = df_clean[col].mode()[0]
            df_clean[col] = df_clean[col].fillna(mode_val)
            
    print("\nSố lượng khuyết thiếu sau khi xử lý:")
    print(df_clean.isnull().sum())
    return df_clean

if __name__ == "__main__":
    run()
