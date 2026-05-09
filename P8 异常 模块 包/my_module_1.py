# __all__变量 —— 列表类型
# 如果一个模块文件中有__all__变量，当使用from 模块名 import *导入时，只能导入这个列表中的元素
# 如果模块文件中没写__all__变量，则使用from 模块名 import *导入时，导入所有方法、函数 等

__all__ = ['test']

def test(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

# 只在当前文件中调用test函数
# 其他导入my_module_1模块test函数的文件内不符合__name__ == '__main__'的条件，不执行test函数调用
if __name__ == '__main__':
    test(1, 2)
# __name__是文件的内置变量，只有运行该文件时，__name__ == '__main__'是成立的（True）
# 作为模块被调用时，？不成立？