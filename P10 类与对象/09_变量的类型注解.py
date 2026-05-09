# 为变量设置类型注解的语法
# 变量: 类型
import json

var_1: int = 10
var_2: float = 12.3
var_3: bool = True
var_4: str = 'helloworld'

class Student:
    pass

# 对象的类型注解
stu: Student = Student()

# 数据容器的类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {'num': 100}
my_str: str = 'hello'

# 容器类型的详细注解
_list: list[int] = [1, 2, 3]

# 注意：元组的详细注解，需要将每一个元素都标记出来
_tuple: tuple[str, int, bool] = ('hello', 2, True)

_set: set[int] = {1, 2, 3}

# 注意：字典的详细注解，需要2个类型，第一个对应key，第二个对应value
_dict: dict[str, int] = {'num': 100}

# 在注释中进行类型注解
# 语法 # type: 类型

import random
_var1 = random.randint(1, 10) # type: int

_var2 = 'ABC' # type: str
_var3 = Student() # type: Student

# [alt] + [enter] 导入包
_var4 = json.loads('{"num": 100}') # type: dict

def func():
    return random.randint(1, 10)

_var5 = func() # type: int

# 类型注解的限制
# 一般情况下，无法看出变量类型时，会添加类型注解
# 类型注解仅仅是提示性质的
_var6: str = random.randint(1, 10) # IDE会高亮警告，但运行不报错