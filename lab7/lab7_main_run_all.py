# FILE CHẠY CHÍNH TỔNG HỢP TOÀN BỘ CÁC BÀI TẬP LAB 7 (BẢN FIX LỖI CACHE)
import os
import sys

print("=========================================================")
print("     BẮT ĐẦU CHẠY KIỂM TRA TOÀN BỘ BÀI TẬP LAB 7        ")
print("=========================================================\n")

print("--- ĐANG CHẠY FILE 1 (BÀI 1, 2, 3) ---")
os.system(f'"{sys.executable}" lab7_bai1_2_3.py')
print("\n" + "="*55 + "\n")

print("--- ĐANG CHẠY FILE 2 (BÀI 4, 5) ---")
os.system(f'"{sys.executable}" lab7_bai4_5.py')
print("\n" + "="*55 + "\n")

print("--- ĐANG CHẠY FILE 3 (BÀI 6, 7) ---")
os.system(f'"{sys.executable}" lab7_bai6_7.py')
print("\n" + "="*55 + "\n")

print("--- ĐANG CHẠY FILE 4 (BÀI 8, 9, 10) ---")
os.system(f'"{sys.executable}" lab7_bai8_9_10.py')
print("\n" + "="*55 + "\n")

print("--- ĐANG CHẠY FILE 5 (BÀI 11, 12, 13) ---")
os.system(f'"{sys.executable}" lab7_bai11_12_13.py')
print("\n" + "="*55 + "\n")

print("=========================================================")
print(" CHÚC MỪNG! ĐÃ HOÀN THÀNH CHẠY THỬ TOÀN BỘ BÀI LAB 7! ")
print("=========================================================")