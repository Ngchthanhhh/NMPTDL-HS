# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split

def run(df=None):
    print("\n--- CÂU 10: CHIA TẬP DỮ LIỆU THÀNH TRAIN VÀ TEST ---")
    if df is None:
        import cau_09
        df = cau_09.run()
        
    X = df.drop('Target', axis=1, errors='ignore')
    y = df['Target'] if 'Target' in df.columns else df.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"Kích thước tập Train (X_train, y_train): {X_train.shape}, {y_train.shape}")
    print(f"Kích thước tập Test (X_test, y_test): {X_test.shape}, {y_test.shape}")
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    run()
