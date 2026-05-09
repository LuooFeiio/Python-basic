"""
循环内套循环
while condition1:
    condition1满足时执行语句
    ...省略...
    while condition2:
        condition1满足时执行语句
        ...省略...
"""

i = 1
while i < 5:
    print(f"今天是第{i}天")

    j = 1
    while j < 4:
        print(f'\t这是第{i}天第{j}次学python')
        j += 1

    i += 1

print("Loop Over!")