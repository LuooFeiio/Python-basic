# 函数定义中的参数，称为形式参数
# 函数调用中的参数，称为实际参数

def add(x, y): # 参数之间用逗号(,)分开，参数数量不限
    result = x + y
    print(f'x = {x}, y = {y}')
    print(f'{x} + {y} = {result}.')

a = 3
b = 4
c = 5
add(a, b) # 传入变量

add(1, 2) # 传入字面量

def add_plus(x, y, z):
    result = x + y + z
    print(f'x = {x}, y = {y}, z = {z}')
    print(f'{x} + {y} + {z} = {result}.')

add_plus(1, 2, 3)

add_plus(a, b, c)