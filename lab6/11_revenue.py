df['Revenue'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])
print('3.1: Đã tạo cột Revenue.')