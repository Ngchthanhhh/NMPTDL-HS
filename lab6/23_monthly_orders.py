orders_m = df.groupby('Month').size()
print('\n--- 5.3: Số lượng đơn theo tháng ---')
print(orders_m)
print(f'Tháng nhiều đơn nhất: {orders_m.idxmax()}')