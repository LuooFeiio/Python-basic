# 如果函数没有使用return语句，那么函数有返回值么？
# 有的
# 字面量 None，表示“空、没有意义”，其类型：<class 'NoneType'>

print(type(None))

def say_hi():
    print('Hi!')

result = say_hi()
print(result, type(result)) # None, <class 'NoneType'>

# 也可以在定义函数时，主动写入return None，其效果与不写return语句是相同的
def say_hello():
    print('Hello!')
    return None

result = say_hello()
print(result, type(result))

# if判断中，None等同于False
def check_age(age):
    if age >= 18:
        return "Success"
    return None

result = check_age(int(input('Enter your age: ')))

if not result: # result为None值
    print('未成年人不可进入')
else:
    print(result)

# None用于声明无初始内容的变量
name = None