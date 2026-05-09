class Person:
    pass

class Student(Person):
    def __init__(self):
        print('学生对象创建了')

class Teacher(Person):
    def __init__(self):
        print('老师对象创建了')

class Worker(Person):
    def __init__(self):
        print('工人对象创建了')

class PearsonFactory:
    def get_person(self, p_type):
        if p_type == 's':
            return Student()
        elif p_type == 't':
            return Teacher()
        elif p_type == 'w':
            return Worker()
        else:
            pass

pf = PearsonFactory() # 创建工厂对象
student = pf.get_person('s') # 由工厂创建Student类实例
teacher = pf.get_person('t')
worker = pf.get_person('w')