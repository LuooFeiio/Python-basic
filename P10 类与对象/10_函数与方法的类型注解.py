# 形参的类型注解：写代码时可以出现提示
# 语法：
# def 函数方法名(形参名: 类型, 形参名: 类型, ...):
#   pass
def add(a: int, b: int):
    return a + b

result = add(1, 2)
print(result)

# 返回值的类型注解：不是强制性的
# 语法：
# def 函数方法名(形参名: 类型, 形参名: 类型, ...) -> 返回值类型:
#   pass
def func(data: list) -> list:
    return data

print(func(1)) # IDE高亮警告，但不报错