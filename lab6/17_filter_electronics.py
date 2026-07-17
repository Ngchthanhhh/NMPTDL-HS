count = len(df[(df['Product_Category'] == 'Electronics') & (df['Discount'] == 0)])
print(f'\n--- 4.2: Số đơn Electronics không giảm giá: {count} ---')