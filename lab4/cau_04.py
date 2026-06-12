# -*- coding: utf-8 -*-
import pandas as pd

def run(df=None):
    print("\n--- CÂU 4: THỐNG KÊ MÔ TẢ DỮ LIỆU ---")
    if df is None:
        import cau_03
        df = cau_03.run()
        
    print("\nThống kê mô tả đối với các biến số:")
    print(df.describe())
    
    print("\nThống kê mô tả đối với các biến phân loại/định tính:")
    print(df.describe(include=['object', 'category']))
    return df

if __name__ == "__main__":
    run()
