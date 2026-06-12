# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def run(best_model=None, data=None):
    print("\n--- CÂU 15: TRỰC QUAN HÓA MA TRẬN NHẦM LẪN (CONFUSION MATRIX) ---")
    if data is None:
        import cau_10
        data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    if best_model is None:
        import cau_13
        best_model = cau_13.run(data)
        
    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    print("\nMa trận nhầm lẫn:")
    print(cm)
    
    plt.figure(figsize=(5, 4))
    plt.imshow(cm, cmap='Blues', interpolation='nearest')
    plt.title('Confusion Matrix')
    plt.colorbar()
    plt.xlabel('Dự đoán (Predicted)')
    plt.ylabel('Thực tế (Actual)')
    plt.tight_layout()
    plt.show()
    return cm

if __name__ == "__main__":
    run()
