# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier

def run(data=None):
    print("\n--- CÂU 13: HUẤN LUYỆN MÔ HÌNH RANDOM FOREST ---")
    if data is None:
        import cau_10
        data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Mô hình Random Forest đã được huấn luyện thành công.")
    return model

if __name__ == "__main__":
    run()
