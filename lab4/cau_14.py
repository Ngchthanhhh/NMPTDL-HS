# -*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score, classification_report

def run(models=None, data=None):
    print("\n--- CÂU 14: ĐÁNH GIÁ HIỆU NĂNG CÁC MÔ HÌNH ---")
    if data is None:
        import cau_10
        data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    if models is None:
        import cau_11, cau_12, cau_13
        m1 = cau_11.run(data)
        m2 = cau_12.run(data)
        m3 = cau_13.run(data)
        models = {'Logistic Regression': m1, 'Decision Tree': m2, 'Random Forest': m3}
        
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = acc
        print(f"\nHiệu năng mô hình [{name}] - Accuracy: {acc:.4f}")
        print(classification_report(y_test, y_pred))
    return results

if __name__ == "__main__":
    run()
