rev_by_reg = df.groupby('Region')['Revenue'].sum()
print('\n--- 5.1: Doanh thu theo khu vực ---')
print(rev_by_reg)
print(f'Khu vực mang lại doanh thu cao nhất: {rev_by_reg.idxmax()}')