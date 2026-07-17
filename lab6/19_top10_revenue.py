print('\n--- 4.4: Top 10 đơn hàng doanh thu cao nhất ---')
print(df.nlargest(10, 'Revenue')[['OrderID', 'Product_Name', 'Revenue']])