# while更灵活，适用任何场景

def while_list_func():
    """
    用while循环遍历列表
    :return: None
    """
    mylist = ['python', 'c', 'c++', 'verilog']
    index = 0
    while index < len(mylist):
        print(f'列表索引为{index}的元素为：{mylist[index]}')
        index += 1 # 循环控制：索引自加1

while_list_func()

# for循环写法较简单，但场景也受限

# for 临时变量 in 数据容器:
#     对临时变量进行处理

def for_list_func():
    """
    用for循环遍历列表
    :return: None
    """
    mylist = ['windows', 'linux', 'unix', 'macos']
    i = 0 # 索引不是必需的
    for element in mylist:
        print(f'列表索引为{i}的元素为：{element}')
        i += 1 # 索引不是必需的

for_list_func()

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_forpick_list(list_whole):
    """
    用for循环挑选偶数形成新的列表后返回
    :param list_whole: 元素为 1 ~ 10 的列表
    :return: list_even 将偶数元素组成新的列表并返回
    """
    list_even = []
    for ele in list_whole:
        if ele % 2 == 0:
            list_even.append(ele)
    return list_even

list_2 = even_forpick_list(list_1)
print(list_2)

def even_whilepick_list(list_whole):
    list_even = []
    i = 0
    while i < len(list_whole):
        if list_whole[i] % 2 == 0:
            list_even.append(list_whole[i])
        i += 1
    return list_even

list_3 = even_whilepick_list(list_1)
print(list_3)