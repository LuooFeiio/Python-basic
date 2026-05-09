"""
for 临时变量 in 待处理数据集（序列）:
    循环满足条件时执行的代码
"""
# 序列类型：其中的内容可以一个一个依次取出
# 字符串、列表、元组 等

# 通过range语句获得一个序列

# 语法1：range(num)
# 获得从 0 ~ num - 1 范围的数字序列。如：range(5)得到[0 1 2 3 4]

for x in range(10):
    print(x) # 0 ~ 9

# 语法2：range(num1, num2)
# 获得从 num1 ~ num2 - 1 范围的数字序列。如：range(5, 10)得到[5 6 7 8 9]

for x in range(5, 10):
    print(x) # 5 ~ 9

# 语法3：range(num1, num2, step)
# 获得从 [num1, num2)（左闭右开区间）范围内，步长为step的数字序列。如：range(5, 10, 2)得到[5 7 9]

for x in range(5, 10, 2):
    print(x) # 5 7 9

for x in range(1, 10):
    print(f'第{x}次学习range语句') # 执行9次
    # 循环体打印时也可以不用临时变量x

num = 100
count = 0
for x in range(1, num + 1):
    if x % 2 == 0:
        count += 1
print(f'从 1 ~ {num} 有{count}个偶数')