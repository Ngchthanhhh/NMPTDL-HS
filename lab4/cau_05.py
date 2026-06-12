# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

def run(df=None):
    print("\n--- CÂU 5: TRỰC QUAN HÓA PHÂN PHỐI BIẾN MỤC TIÊU ---")
    if df is None:
        import cau_03
        df = cau_03.run()
        
    # Giả định biến mục tiêu là cột cuối cùng hoặc cột có tên 'Target'
    target_col = 'Target' if 'Target' in df.columns else df.columns[-1]
    
    plt.figure(figsize=(6, 4))
    df[target_col].value_counts().plot(kind='bar', color=['#34495e', '#e74c3c'])
    plt.title(f'Phân phối của biến mục tiêu: {target_col}')
    plt.xlabel(target_col)
    plt.ylabel('Số lượng')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print(f"Đã vẽ và hiển thị biểu đồ phân phối cho biến: {target_col}")
    return df

if __name__ == "__main__":
    run()
