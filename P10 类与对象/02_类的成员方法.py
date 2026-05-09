"""
1 类的定义
class 类名称:
    类的属性（定义在类中的变量——成员变量）
    类的行为（定义在类中的函数——成员方法）

2 成员方法的定义语法
def 方法名(self, 形参1, ... , 形参N):
    方法体
    # self关键字，在定义成员方法时是必须的，调用传参时可忽略

3 创建类对象
对象 = 类名称()
"""

class Student:
    name = None

    # 定义成员方法时，形参列表中必须有self关键字
    def say_hi(self):
        print('Hi, everybody! I am %s' % self.name) # self.成员变量——使用成员变量

    def say_hello(self, msg):
        print(f'Hello, everyone, I\'m {self.name}, {msg}')

stu = Student()
stu.name = "张雪峰"

stu.say_hi() # 无需传参
stu.say_hello('nice to meet you!') # 仅传入了msg参数