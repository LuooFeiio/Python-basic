# python的数据是有类型的，而变量是没有类型的？变量中存储的数据有类型！

# 1 使用print直接输出类型信息
print(type(666)) # int
print(type(12.34)) # float
print(type("你好世界 HelloWorld")) # str

# 2 使用变量存储type()的返回结果
int_type = type(666)
print(int_type) # <class 'int'>
print(type(int_type)) # <class 'type'>

# 3 type()语句也可以查看变量的类型信息
name = "你好"
print(type(name))
print(name)