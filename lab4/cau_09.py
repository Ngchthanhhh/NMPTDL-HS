# -*- coding: utf-8 -*-
import pandas as pd

def run(df=None):
    print("\n--- CÂU 9: MÃ HÓA BIẾN PHÂN LOẠI (ENCODING) ---")
    if df is None:
        import cau_08
        df, _ = cau_08.run()
    elif isinstance(df, tuple):
        df = df[0]
        
    # Áp dụng One-Hot Encoding cho các biến định tính
    df_encoded = pd.get_dummies(df, drop_first=True)
    print("\nDữ liệu sau khi mã hóa One-Hot Encoding:")
    print(df_encoded.head())
    return df_encoded

if __name__ == "__main__":
    run()
