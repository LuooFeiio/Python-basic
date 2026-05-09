"""
    函数说明
    :param x: 形参x的说明
    :param y: 形参y的说明
    :return: 返回值的说明
"""

def add(x, y):
    """
    add函数是一个自定义的两数相加的函数
    :param x: 形参x表示一个加数
    :param y: 形参y也表示一个加数
    :return: 返回值是两数相加的结果
    """
    result = x + y
    return result

result = add(1, 2) # 鼠标悬停至“add”，查看说明文档
print(f'两数相加的结果为{result}')

print(f'两数相加的结果为{add(3, 4)}')