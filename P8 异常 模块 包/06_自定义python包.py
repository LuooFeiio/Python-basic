# 包用于管理模块
# 包是一个文件夹：包含一个__init__.py文件（内容可为空，但该文件必须存在） 与 多个模块文件

# 创建一个包
# 在自建的包中建一些模块

# 1 导入自定义包的模块，并使用
# import my_package.my_module_1
# import my_package.my_module_2
#
# my_package.my_module_1.info_print1()
# my_package.my_module_2.info_print2()

# 2 第二种导入与使用方法
# from my_package import my_module_1
# from my_package import my_module_2
#
# my_module_1.info_print1()
# my_module_2.info_print2()

# 3 第三种导入与使用方法
# from my_package.my_module_1 import info_print1
# from my_package.my_module_2 import info_print2
#
# info_print1()
# info_print2()

# 4 在__init__.py文件中添加 __all__ = [...] ，控制 from 包名 import * 允许导入的模块列表
# __init__.py文件：__all__ = ['my_module_2']
from my_package import * # 只能导入my_module_2
my_module_2.info_print2()

from my_package import my_module_1 # 可以手动导入my_module_1
my_module_1.info_print1()