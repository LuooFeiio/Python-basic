"""
递归调用：
def func():
    ...
    if expression:
        func()
    ...
    return ...

演示Python递归操作
需求：通过递归，找出一个指定文件夹内的全部文件

思路：写一个函数，列出文件夹内的全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己，再次判断
"""

import os

def test_os():
    """演示os模块的3个基础方法"""

    # 列出路径下的内容
    print(os.listdir("./Recursion")) # ['1.txt', '2.txt', '3.txt', 'a', 'b']

    # 判断指定路径是不是文件夹
    print(os.path.isdir("./Recursion/a")) # True
    print(os.path.isdir("./Recursion/1.txt")) # False

    # 判断指定路径是否存在
    print(os.path.exists("D:/test")) # False
    print(os.path.exists("./Recursion")) # True

def get_files_recursion_from_dir(path):
    """
    使用递归的方式，获取指定文件夹中全部的文件列表
    :param path: 被判断的文件夹
    :return: list 包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    print(f"当前判断的路径是：{path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f # 路径组装
            if os.path.isdir(new_path):
                # 进入到这里，表明这个目录 是文件夹 不是文件
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list

if __name__ == '__main__':
    # test_os()
    print(f'判断路径下的文件有：{get_files_recursion_from_dir('./Recursion')}')

# 递归注意事项：
# 注意退出的条件，否则容易变成无限递归
# def a():
#     a():
# 注意返回值的传递，确保从最内层，层层传递到最外层