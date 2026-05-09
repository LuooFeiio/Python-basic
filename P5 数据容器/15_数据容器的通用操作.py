# 通用操作：
# • len()、max()、min()
# • 类型转换：list(容器)、tuple(容器)、str(容器)、set(容器)
# • 容器排序：sorted(容器, [reverse = True])

# 1 len(数据容器) max(数据容器) min(数据容器)

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = 'abcdefg'
my_set = {1, 2, 3, 4, 5}
my_dict = {'key1': 6, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}

print('len:', len(my_list), 'min:', min(my_list), 'max:', max(my_list))
print('len:', len(my_tuple), 'min:', min(my_tuple), 'max:', max(my_tuple))
print('len:', len(my_str), 'min:', min(my_str), 'max:', max(my_str)) # 7 a g
print('len:', len(my_set), 'min:', min(my_set), 'max:', max(my_set))
print('len:', len(my_dict), 'min:', min(my_dict), 'max:', max(my_dict)) # 5 key1 key5

# 2 类型转换：
# list(容器) —— 将容器转换为列表
# tuple(容器) —— 将容器转换为元组
# str(容器) —— 将容器转换为字符串
# set(容器) —— 将容器转换为集合

# 容器转换为列表
print(f'列表2列表：{list(my_list)}')
print(f'元组2列表：{list(my_tuple)}')
print(f'字符串2列表：{list(my_str)}') # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f'集合2列表：{list(my_set)}')
print(f'字典2列表：{list(my_dict)}') # ['key1', 'key2', 'key3', 'key4', 'key5']

# 容器转换为元组
print(f'列表2元组：{tuple(my_list)}')
print(f'元组2元组：{tuple(my_tuple)}')
print(f'字符串2元组：{tuple(my_str)}') # ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(f'集合2元组：{tuple(my_set)}')
print(f'字典2元组：{tuple(my_dict)}') # ('key1', 'key2', 'key3', 'key4', 'key5')

# 容器转换为字符串
list_str = str(my_list)
print(f'列表2字符串：{list_str}, {type(list_str)}')

tuple_str = str(my_tuple)
print(f'元组2字符串：{tuple_str}, {type(tuple_str)}')

print(f'字符串2字符串：{str(my_str)}')

set_str = str(my_set)
print(f'集合2字符串：{set_str}, {type(set_str)}')

dict_str = str(my_dict)
print(f'字典2字符串：{dict_str}, {type(dict_str)}')
# {'key1': 6, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}

# 容器转换为集合
print(f'列表2集合：{set(my_list)}')
print(f'元组2集合：{set(my_tuple)}')
print(f'字符串2集合：{set(my_str)}') # {'f', 'g', 'c', 'd', 'a', 'e', 'b'} 乱序
print(f'集合2集合：{set(my_set)}')
print(f'字典2集合：{set(my_dict)}') # {'key1', 'key2', 'key4', 'key5', 'key3'} 乱序

# 3 容器排序
# 语法：sorted(容器, [reverse = True])
# 结果：返回列表对象

# 升序
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(sorted(my_set))
print(sorted(my_dict)) # ['key1', 'key2', 'key3', 'key4', 'key5']

# 降序
print(sorted(my_list, reverse = True))
print(sorted(my_tuple, reverse = True))
print(sorted(my_str, reverse = True)) # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(sorted(my_set, reverse = True))
print(sorted(my_dict, reverse = True)) # ['key5', 'key4', 'key3', 'key2', 'key1']

# 通用操作：
# • len()、max()、min()
# • 类型转换：list(容器)、tuple(容器)、str(容器)、set(容器)
# • 容器排序：sorted(容器, [reverse = True])