import os
import time

print("Bắt đầu khởi chạy pipeline 26 files...")
time.sleep(1)

# Không gian bộ nhớ chung để biến 'df' được truyền từ file 1 sang các file sau
shared_env = {}

# Quét tất cả các file python bắt đầu bằng số (01 -> 26) trong thư mục hiện tại
files = [f for f in os.listdir('.') if f.endswith('.py') and f[:2].isdigit() and int(f[:2]) <= 26]
files.sort()

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
        exec(code, shared_env)

print("\n[!] ĐÃ CHẠY XONG TẤT CẢ 26 YÊU CẦU.")
