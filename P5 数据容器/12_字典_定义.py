# dict
# key: value 键值对，key是不可以重复的
"""
姓名  成绩
key——value
小明  89
李白  91
张三  94
"""

# 字典定义：使用{}，存储的元素是一个个键值对
my_dict_1 = {"jack": 99, 'tom': 100, 'smith': 98}
print(my_dict_1, type(my_dict_1))

# 空字典：1 my_dict = {} 2 my_dict = dict()
my_dict_2 = {}
print(my_dict_2, type(my_dict_2))
my_dict_3 = dict()
print(my_dict_3, type(my_dict_3))

# 字典中的key是不可以重复的
my_dict_4 = {"jack": 99, "jack": 88, 'smith': 98}
print(my_dict_4) # {'jack': 88, 'smith': 98} （自动覆盖）

# 通过key值来获得对应的value
score = my_dict_1['jack']
print(score)

# 字典的嵌套：key不可以是字典，value可以是字典或其他类型数据
nested_dict = {
    'jack': {"math": 99, "english": 88, 'chinese': 100},
    'tom': {"math": 80, "english": 98, 'chinese': 90},
    'elk': {"math": 96, "english": 91, 'chinese': 93}
}
print(nested_dict)
print(nested_dict['jack'])
print(nested_dict['jack']['math'], type(nested_dict['jack']['math'])) # 99 int