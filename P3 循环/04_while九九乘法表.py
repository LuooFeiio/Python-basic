# print输出不换行的方法
# print("helloworld", end = '')

# print打印水平制表符
# print("\t")

# print打印换行
# print("\n") 与 print() 效果有差别

i = 1

while i <= 9:

    j = 1

    while j <= i:
        print(f'{j} * {i} = {i * j}\t', end = '')
        j += 1

    print() # 换行
    i += 1