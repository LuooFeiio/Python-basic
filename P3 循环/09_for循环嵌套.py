# 注意空格缩进
# 打印九九乘法表
for i in range(1, 10): # 1 ~ 9
    for j in range(1, i + 1): # 1 ~ i
        print(f'{j} * {i} = {i * j}\t', end = '')
    print()

# for与while也可相互嵌套