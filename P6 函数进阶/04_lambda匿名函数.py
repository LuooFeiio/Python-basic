# 匿名函数可临时使用一次
# 语法：
# lambda 传入参数: 函数体（一行代码）
# • lambda是定义匿名函数的关键字
# • 传入参数表示匿名函数的形式参数，如：x, y表示接收两个形式参数
# • 函数体，即函数执行逻辑功能，注意：只能写一行  (？函数体的执行结果直接return，因此不用写return语句？)

def test_func(compute):
    result = compute(3, 2)
    print(f'compute参数的类型是：{type(compute)}')
    print(result)

test_func(lambda x, y: x + y)

test_func(lambda x, y: x - y)

test_func(lambda x, y: x * y)

test_func(lambda x, y: x / y)

test_func(lambda x, y: x ** y)

test_func(lambda x, y: x // y)