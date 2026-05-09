# 列表的sort方法：
# 列表.sort(key = 选择排序依据的函数, reverse = True|False)
# 参数key：要求传入一个函数，将列表的每一个元素都传入函数中，返回排序的依据
# 参数reverse：是否反转排序结果，True表示降序，False表示升序

# 通过lambda匿名函数使用sort方法
my_list = [['a', 33], ['b', 55], ['c', 66]]
my_list.sort(key = lambda element: element[1], reverse = True)
print(my_list)

# 通过自定义函数使用sort方法
def choose_sort_key(element):
    return element[1]

my_list.sort(key = choose_sort_key) # reverse = False
print(my_list)

# 字典的一些基操
my_dict = {} # 空字典
print(my_dict)

my_dict['a'] = 33
print(my_dict)

my_dict[2001] = []
print(my_dict)

my_dict[2001].append(33)
print(my_dict)

my_dict[2001].append(['China', "No.1"])
print(my_dict)

# float()方法
print(float('\n1.234\n'))