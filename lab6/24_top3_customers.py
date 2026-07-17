print('\n--- 5.4: Top 3 khách hàng chi tiêu cao nhất ---')
print(df[df['CustomerID'] != 'GUEST'].groupby('CustomerID')['Revenue'].sum().nlargest(3))