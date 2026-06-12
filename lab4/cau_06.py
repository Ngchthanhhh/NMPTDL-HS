# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

def run(df=None):
    print("\n--- CÂU 6: PHÂN TÍCH MA TRẬN HỆ SỐ TƯƠNG QUAN ---")
    if df is None:
        import cau_03
        df = cau_03.run()
        
    # Lọc lấy các cột dữ liệu số
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    corr_matrix = numeric_df.corr()
    
    print("\nMa trận hệ số tương quan giữa các biến số:")
    print(corr_matrix)
    
    # Trực quan hóa ma trận hệ số tương quan
    plt.figure(figsize=(8, 6))
    plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.title('Ma trận hệ số tương quan (Correlation Matrix)')
    plt.tight_layout()
    plt.show()
    return corr_matrix

if __name__ == "__main__":
    run()
