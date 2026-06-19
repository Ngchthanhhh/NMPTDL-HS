print('\n--- 5.2: TB Số lượng & Đơn giá theo Danh mục ---')
print(df.groupby('Product_Category')[['Quantity', 'UnitPrice']].mean())