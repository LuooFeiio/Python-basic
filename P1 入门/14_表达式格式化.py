print(f'1 + 2 = {1 + 2}')
print('1 + 2 = %d' % (1 + 2))

print(f'我的名字是：{"巨人-戈莱厄斯"}，今年{8}岁了，身高为{3.24 + 3}米。')

name = "兰州牛肉面公司"
price = 9
inflation_rate = 1.05
years = 7

print("%s的当前产品价格为%d￥，经过%d年后，其产品价格变为：%.2f￥" % (name, price, years, price * (inflation_rate ** years)))