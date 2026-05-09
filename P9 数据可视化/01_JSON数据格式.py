# JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据
# JSON本质上是一个带有特定格式的字符串
# 各种编程语言存储数据的容器不尽相同，在Python中有字典dict这样的数据类型，而其它语言可能没有对应的字典
# 为了让不同的语言能够互传数据，JSON就是一种非常良好的中转数据格式

# 导入json模块
import json

# 准备符合json格式要求的python数据
# 元素都是字典的列表
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]

# 通过 json.dumps(data) 方法把python数据转化为json数据
# json_str = json.dumps(data)
json_str = json.dumps(data, ensure_ascii = False) # 可以显示中文字符
print(json_str)
print(type(json_str)) # str

# 通过 json.loads(data) 方法把json数据转化为python数据
python_data = json.loads(json_str)
print(python_data)
print(type(python_data)) # list

# 准备符合json格式要求的python数据
# 字典
my_dict = {"name": "老王", "age": 16}
json_data = json.dumps(my_dict, ensure_ascii = False)
print(json_data)
print(type(json_data))

python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict))