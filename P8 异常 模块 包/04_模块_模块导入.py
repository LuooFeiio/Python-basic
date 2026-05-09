# 模块是python的一个文件，内含类、函数、变量等
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# 常用的形式：
# import 模块名
# from 模块名 import 类、变量、方法 等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# 基本语法：
# import 模块名
# import 模块名1, 模块名2
# 模块名.功能名()
import time # 导入时间模块
print("开始")
time.sleep(1) # 让程序睡眠1秒(阻塞)
print("结束")

# 基本语法：
# from 模块名 import 功能名
# 功能名()
from time import sleep # 导入时间模块中的sleep方法
print("开始")
sleep(1) # 让程序睡眠1秒(阻塞)
print("结束")

# 基本语法：
# from 模块名 import *
# 功能名()
from time import * # 导入时间模块中所有的方法
print("开始")
sleep(1) # 让程序睡眠1秒(阻塞)
print("结束")

# 模块定义别名
# import 模块名 as 别名
# 功能定义别名
# from 模块名 import 功能 as 别名

import time as tt # 模块别名
tt.sleep(2)
print('hello')

from time import sleep as sl # 功能别名
sl(2)
print('hello')