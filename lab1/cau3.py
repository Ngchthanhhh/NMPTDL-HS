import pandas as pd
input_path = r"D:\NMPTDL\Lab1\dulieuxettuyendaihoc.csv"
df = pd.read_csv(input_path)
print("=== 10 DÒNG ĐẦU TIÊN ===")
print(df.head(10))
print("\n=== 10 DÒNG CUỐI CÙNG ===")
print(df.tail(10))