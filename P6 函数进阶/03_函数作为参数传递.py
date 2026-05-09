# 任何逻辑都可以自行定义并作为参数传入

def test_func(compute):
    result = compute(3, 2)
    print(f'compute参数的类型是：{type(compute)}')
    print(result)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

test_func(add)
test_func(sub)
test_func(mul)