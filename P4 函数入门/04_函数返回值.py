"""
定义：
def 函数(传入参数):
    函数体
    return 返回值

调用：
变量 = 函数(参数)
"""

def add(a, b):
    result = a + b
    return result # return语句后的函数体不会执行
    print('Func finish') # 这个语句不会执行

r = add(5, 6)
print(r) # 11