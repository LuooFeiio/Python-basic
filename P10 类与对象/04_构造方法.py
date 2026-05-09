class Student:
    # name = None # 可省略
    # age = None # 可省略
    # tel = None # 可省略

    # 构造方法：__init__
    # 可以实现：1 创建对象时会自动执行 2 创建对象时将传入的参数传递给__init__方法使用
    def __init__(self, name, tel): # 定义构造方法时也需要self关键字
        self.name = name # 创建成员变量并赋值
        self.age = int(input('请输入学生的年龄：'))
        self.tel = tel
        print(f'Student类创建了一个对象，信息为：学生姓名——{self.name}，年龄——{self.age}，电话——{self.tel}')

# 使用构造方法创建对象
stu = Student('张三', '18235647891')