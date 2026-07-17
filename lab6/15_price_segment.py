def get_segment(p):
    if p >= 150: return 'High'
    elif p >= 50: return 'Medium'
    else: return 'Low'
df['Price_Segment'] = df['UnitPrice'].apply(get_segment)
print('3.5: Đã tạo cột Price_Segment.')