# 位置参数
# 关键字参数
# 缺省参数（默认值）
# 不定长参数

def user_info(name, age, gender):
    """
    函数-打印信息
    :param name: 名字-字符串
    :param age: 年龄-整数
    :param gender: 性别-字符串
    :return: None
    """
    print(f'用户名字是：{name}，年龄是：{age}，性别是：{gender}')

# 位置参数：根据参数的位置来传递参数——实参要符合形参的顺序与个数
user_info('python', 50, 'male')

# 关键字参数：通过“键(形参) = 值(实参)”形式传参，可以打乱参数顺序
user_info(gender = 'female', name = 'lily', age = 20)

# 关键字参数可以和位置参数混用：位置参数必须在关键字参数的前面
user_info('wilder', gender = 'male', age = 22)

# 缺省参数（默认值）：定义函数时，参数有默认值，调用函数时可以不用为有默认值的参数传参
# 注意：所有位置参数必须出现在默认参数之前，包括函数的定义与调用
def user_info_2(name, age, gender = '男'):
    print(f'用户名字是：{name}，年龄是：{age}，性别是：{gender}')

user_info_2('wang', 18)
user_info_2('li', 19, '女')

# 不定长参数（可变参数）
# 不定长参数的分类：1 位置传递 2 关键字传递

# 位置传递的不定长参数：*
# 传进的所有参数都会被args变量收集，它会将传进的参数合并为一个元组，即args是元组类型
def user_info_3(*args):
    print(args, type(args))

user_info_3('tom') # ('tom',)
user_info_3('tom', 18) # ('tom', 18)

# 关键字传递的不定长参数：**
# 传入的参数是“键 = 值”的形式，所有的“键 = 值”参数被kwargs接收合并为字典，即kwargs是字典类型
def user_info_4(**kwargs):
    print(kwargs, type(kwargs))

user_info_4(age = 20, name = 'lily', gender = 'male') # {'age': 20, 'name': 'lily', 'gender': 'male'}
user_info_4(str1 = 'we', bool2 = True) # {'str1': 'we', 'bool2': True}