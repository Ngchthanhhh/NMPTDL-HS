# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def run(df=None):
    print("\n--- CÂU 7: PHÁT HIỆN VÀ XỬ LÝ DỮ LIỆU NGOẠI LAI (OUTLIERS) ---")
    if df is None:
        import cau_03
        df = cau_03.run()
        
    df_out = df.copy()
    numeric_cols = df_out.select_dtypes(include=['int64', 'float64']).columns
    
    print("Xử lý Outliers bằng phương pháp IQR (Khoảng biến thiên tứ phân vị):")
    for col in numeric_cols:
        if col == 'Target': continue # Giữ nguyên biến mục tiêu nhị phân
        Q1 = df_out[col].quantile(0.25)
        Q3 = df_out[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Giới hạn giá trị ngoại lai về biên (Winsorization)
        df_out[col] = np.clip(df_out[col], lower_bound, upper_bound)
        print(f" -> Đã xử lý Outliers cho cột '{col}' trong khoảng [{lower_bound:.2f}, {upper_bound:.2f}]")
        
    return df_out

if __name__ == "__main__":
    run()
