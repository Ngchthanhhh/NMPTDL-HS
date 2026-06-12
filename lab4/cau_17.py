# -*- coding: utf-8 -*-
import os
import joblib

def run(model=None):
    print("\n--- CÂU 17: LƯU MÔ HÌNH ĐÃ HUẤN LUYỆN ---")
    if model is None:
        import cau_16
        model = cau_16.run()
        
    model_path = "best_model.pkl"
    joblib.dump(model, model_path)
    print(f"Mô hình tốt nhất đã được lưu thành công tại file: {os.path.abspath(model_path)}")
    return model_path

if __name__ == "__main__":
    run()
