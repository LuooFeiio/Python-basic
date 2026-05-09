# 字面量：[元素1, 元素2, 元素3, 元素4, 元素5]
name_list = ['python', 'c', 'c++', 'verilog']

print(name_list)
print(type(name_list)) # <class 'list'>

print(name_list[0]) # python
print(name_list[1]) # c

print(len(name_list)) # 4

# 定义变量：变量名称 = [元素1, 元素2, 元素3, 元素4, 元素5]
my_list_1 = ['systemverilog', 666, True] # 元素的类型可以不同，元素甚至可以是列表
print(my_list_1, type(my_list_1))

my_list_2 = ['systemverilog', [1, 2, 3]] # 嵌套列表
print(my_list_2)
print(my_list_2[1]) # [1, 2, 3]

my_list_3 = [my_list_1, my_list_2] # 嵌套列表
print(my_list_3)
print(my_list_3[1])

# 定义空列表
# 变量名称 = []
my_list_4 = []
print(my_list_4)
# 变量名称 = list()
my_list_5 = list()
print(my_list_5)

my_list_6 = list(range(6))
print(my_list_6) # [0, 1, 2, 3, 4, 5]

# 列表的特点：
# 1 可以容纳不同类型的元素
# 2 允许重复元素存在
# 3 数据是有序存储的（有下标序号）
# 4 可以修改（增加或删除元素）