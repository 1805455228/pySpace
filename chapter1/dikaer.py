
#笛卡尔积 和 列表推导 示例
#列表推导的作用只有一个：生成列表
colors=['black', 'white']
sizes=['S','M','L']

tshirts=[(color, size) for color in colors for size in sizes]
print(tshirts)



#生成器表达式
symbols = '$¢£¥€¤'
aa=tuple(ord(symbol) for symbol in symbols)
print(aa)
