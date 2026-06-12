# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run(df=None):
    print("\n--- CÂU 8: CHUẨN HÓA DỮ LIỆU SỐ (SCALING) ---")
    if df is None:
        import cau_07
        df = cau_07.run()
        
    df_scaled = df.copy()
    numeric_cols = df_scaled.select_dtypes(include=['int64', 'float64']).columns.drop('Target', errors='ignore')
    
    scaler = StandardScaler()
    df_scaled[numeric_cols] = scaler.fit_transform(df_scaled[numeric_cols])
    
    print("\nDữ liệu số sau khi được chuẩn hóa bằng StandardScaler (Z-score):")
    print(df_scaled[numeric_cols].head())
    return df_scaled, scaler

if __name__ == "__main__":
    run()
