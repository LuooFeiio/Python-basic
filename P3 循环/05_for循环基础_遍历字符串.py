# for循环遍历字符串

"""
for 临时变量 in 待处理数据集（序列）:
    循环满足条件时执行的代码
"""

name = "luofei"

count = 0

for x in name:
    # 将name中的内容，挨个取出赋予临时变量x
    # 然后在循环体内操作x
    print(x)
    count += 1

print(f'\"{name}\"中有{count}个字母')

# python的for循环没法定义循环条件
# 这个比C方便点