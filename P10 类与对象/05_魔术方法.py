# 魔术方法：python类的内置方法
# __init__ 构造方法
# __str__ 字符串方法
# __lt__ 小于<（大于>）符号比较方法
# __le__ 小于等于<=（大于等于>=）符号比较方法
# __eq__ 等于==（？不等于!=？）符号比较方法

class Student:
    # __init__方法：构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__方法：控制类转换为字符串的行为 print(对象) & print(str(对象))
    def __str__(self):
        return f'Student类对象，学生姓名：{self.name}，学生年龄：{self.age}'

    # __lt__方法：小于、大于符号比较
    def __lt__(self, other):
        # 传入参数other是另一个对象
        return self.age < other.age

    # __le__方法：小于等于<=（大于等于>=）符号比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__方法：等于==（（？不等于!=？）符号比较
    def __eq__(self, other):
        return self.age == other.age

# __init__ 构造方法 创建对象
stu = Student("飞", 22)

# __str__ 字符串方法 作用效果
print(stu) # Student类对象，学生姓名：飞，学生年龄：22
print(str(stu)) # Student类对象，学生姓名：飞，学生年龄：22

# __lt__ 小于（大于）符号比较方法 作用效果
stu1 = Student('zhang', 18)
stu2 = Student('liu', 22)
print(stu1 > stu2) # False
print(stu1 < stu2) # True

# __le__ 小于等于<=（大于等于>=）符号比较方法 作用效果
stu3 = Student('zen', 22)
print(stu1 >= stu2) # False
print(stu1 <= stu2) # True
print(stu3 <= stu2) # True

# __eq__ 等于==（？不等于!=？）符号比较方法 作用效果
print(stu1 == stu2) # False
print(stu1 != stu2) # True
print(stu2 != stu3) # False