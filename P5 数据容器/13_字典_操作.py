# 字典的方法：
# • 新增/修改 元素
# • 删除元素
# • 清空字典
# • 获取全部的key
# • 统计字典元素数量——len(字典)

# 1 新增/修改 元素
# 语法：字典[key] = Value    如果key不存在，则新增；若存在，则修改
my_dict_1 = {"jack": 99, 'tom': 100, 'smith': 98}
print(my_dict_1)

my_dict_1['elk'] = 60 # 新增
print(my_dict_1)

my_dict_1['jack'] = 95 # 修改
print(my_dict_1)

# 2 删除元素
# 语法：字典.pop(key)
# 结果：返回指定key的value，同时字典被修改
value = my_dict_1.pop('jack')
print(value)
print(my_dict_1)

# 3 清空字典
# 语法：字典.clear()
my_dict_1.clear()
print(my_dict_1) # {}

# 4 获取全部的key
# 语法：字典.keys()
# 结果：返回字典全部的key
# 用处：遍历字典
my_dict_2 = {"jack": 99, 'tom': 100, 'smith': 98}
keys = my_dict_2.keys()
print(keys, type(keys))

for key in keys:
    print(f'字典的key为{key}，对应的value值为{my_dict_2[key]}')

# 遍历方式2 —— 直接对字典用for循环，每次循环都是得到key
for key in my_dict_2:
    print(f'字典的key为{key}，对应的value值为{my_dict_2[key]}')

# 遍历字典，不用while循环

# 5 统计字典元素数量——len(字典)
num = len(my_dict_2)
print("字典my_dict_2中的元素个数为：%d" % num)

# 字典特点：
# 1 可容纳多个数据
# 2 可容纳不同类型数据
# 3 每个元素都是键值对
# 4 key不可重复，可通过key获取value
# 5 不支持下标索引
# 6 可修改
# 7 支持for循环