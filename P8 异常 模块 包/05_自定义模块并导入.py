# 1 基本演示
# import my_module_1
# my_module_1.test(3, 4)

# 2 注意事项：
# 当导入多个模块的时候，且模块内有同名功能，则当调用这个同名功能的时候，调用到的是后面导入的模块的功能
# from my_module_1 import test
# from my_module_2 import test
# test(3, 4) # 使用的是my_module_2的test

# 3 __all__变量的作用
# from my_module_1 import *
# test(3, 4) # 只能用test函数，sub函数用不了
# 但是可以手动导入sub函数
# from my_module_1 import sub
# sub(1, 2)

# 4 __name__变量的作用