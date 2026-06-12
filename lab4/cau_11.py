# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression

def run(data=None):
    print("\n--- CÂU 11: HUẤN LUYỆN MÔ HÌNH LOGISTIC REGRESSION ---")
    if data is None:
        import cau_10
        data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    print("Mô hình Logistic Regression đã được huấn luyện thành công.")
    return model

if __name__ == "__main__":
    run()
