# -*- coding: utf-8 -*-
"""
FILE THỰC THI CHÍNH TỔNG HỢP (CÂU 18)
Chạy toàn bộ quy trình từ Câu 1 đến Câu 17 bằng một lần bấm duy nhất.
"""
import sys
import os

# Đảm bảo thư mục hiện tại nằm trong hệ thống tìm kiếm module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("==========================================================================")
    print("   BẮT ĐẦU CHẠY TOÀN BỘ QUY TRÌNH PHÂN TÍCH DỮ LIỆU & HUẤN LUYỆN MÔ HÌNH  ")
    print("==========================================================================")
    
    # Câu 1: Đọc dữ liệu
    import cau_01
    df_raw = cau_01.run()
    
    # Câu 2: Giá trị khuyết thiếu
    import cau_02
    df_clean_missing = cau_02.run(df_raw)
    
    # Câu 3: Dữ liệu trùng lặp
    import cau_03
    df_clean_dup = cau_03.run(df_clean_missing)
    
    # Câu 4: Thống kê mô tả
    import cau_04
    cau_04.run(df_clean_dup)
    
    # Câu 5: Trực quan hóa biến mục tiêu
    import cau_05
    cau_05.run(df_clean_dup)
    
    # Câu 6: Phân tích ma trận tương quan
    import cau_06
    cau_06.run(df_clean_dup)
    
    # Câu 7: Xử lý Outliers
    import cau_07
    df_no_outliers = cau_07.run(df_clean_dup)
    
    # Câu 8: Chuẩn hóa dữ liệu
    import cau_08
    df_scaled, scaler = cau_08.run(df_no_outliers)
    
    # Câu 9: Mã hóa biến phân loại
    import cau_09
    df_encoded = cau_09.run(df_scaled)
    
    # Câu 10: Chia tập Train-Test
    import cau_10
    data_split = cau_10.run(df_encoded)
    
    # Câu 11, 12, 13: Huấn luyện các mô hình
    import cau_11, cau_12, cau_13
    m1 = cau_11.run(data_split)
    m2 = cau_12.run(data_split)
    m3 = cau_13.run(data_split)
    
    # Câu 14: Đánh giá hiệu năng các mô hình
    import cau_14
    models_dict = {
        'Logistic Regression': m1,
        'Decision Tree': m2,
        'Random Forest': m3
    }
    cau_14.run(models_dict, data_split)
    
    # Câu 15: Trực quan hóa ma trận nhầm lẫn cho mô hình tốt nhất hiện tại (Random Forest)
    import cau_15
    cau_15.run(m3, data_split)
    
    # Câu 16: Tối ưu siêu tham số bằng Grid Search
    import cau_16
    best_tuned_model = cau_16.run(data_split)
    
    # Câu 17: Lưu mô hình tối ưu cuối cùng xuống đĩa
    import cau_17
    cau_17.run(best_tuned_model)
    
    print("\n==========================================================================")
    print("   QUY TRÌNH ĐÃ HOÀN THÀNH XUẤT SẮC! TOÀN BỘ 17 CÂU ĐÃ ĐƯỢC THỰC THI.")
    print("==========================================================================")

if __name__ == "__main__":
    main()
