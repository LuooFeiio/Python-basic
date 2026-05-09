# 面向对象三大特性：封装、继承、多态
# 多态：同样的行为（函数），传入不同的对象，得到不同的行为状态

# 多态常作用在继承关系上。
# 比如：函数（方法）形参声明接收父类对象，实际调用传入了子类实参 （？且 函数体中调用的父类成员方法在子类中被复写了？）
# ？python的变量没有类型？

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self): # 复写父类方法
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()
# 多态效果
make_noise(dog)
make_noise(cat)

# 抽象类：含有抽象方法的类（抽象类可以比作标准接口）
# 抽象方法：方法体是空的（pass）
# 使用场景：抽象类作为父类，用来确定有哪些方法；具体的方法实现，由子类完成