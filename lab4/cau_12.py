# -*- coding: utf-8 -*-
from sklearn.tree import DecisionTreeClassifier

def run(data=None):
    print("\n--- CÂU 12: HUẤN LUYỆN MÔ HÌNH DECISION TREE ---")
    if data is None:
        import cau_10
        data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    print("Mô hình Decision Tree đã được huấn luyện thành công.")
    return model

if __name__ == "__main__":
    run()
