# 设计一个类
class Student:
    name = None # 成员变量
    gender = None
    nationality = None
    native_place = None
    age = None

# 基于类创建对象
stu_1 = Student()
stu_2 = Student()

# 对象属性赋值
stu_1.name = 'Fee'
stu_1.gender = '男'
stu_1.nationality = 'china'
stu_1.native_place = '甘肃'
stu_1.age = 18

stu_2.name = '张'

print(stu_1.name, stu_1.native_place, stu_1.age, stu_1.nationality, stu_1.gender)
print(stu_1) # 打印对象的内存地址
print(stu_2.name)
print(stu_2)