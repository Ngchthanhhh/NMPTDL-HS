import pandas as pd
import os

def load_real_data():
    # Đường dẫn chính xác do ní cung cấp
    path = r"D:\lab5_CNN_ipynb\DuLieu\processed_dulieuxettuyendaihoc.csv"
    if not os.path.exists(path):
        # Dự phòng nếu chạy thử môi trường khác, nhưng ưu tiên đường dẫn của ní
        raise FileNotFoundError(f"Không tìm thấy file dữ liệu tại đường dẫn: {path}. Ní kiểm tra lại ổ D nhé!")
    
    df = pd.read_csv(path)
    return df

# Cấu hình hàm phân vị để pivot table gọi
def q1(x): return x.quantile(0.25)
def q2(x): return x.quantile(0.50)
def q3(x): return x.quantile(0.75)

agg_funcs = ['count', 'sum', 'mean', 'median', 'min', 'max', 'std', q1, q2, q3]