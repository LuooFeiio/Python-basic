# 复写
# 子类继承的父类成员属性和方法，若对其不满意，可以复写
# 即，在子类中重新定义同名的属性或方法（对父类成员属性或方法的重新定义）
class Phone:
    producer = 'apple'

    def call_by_5g(self):
        print('父类的5g通话')

# 子类中，如果想使用被复写的父类成员，需要特殊的调用方式
# 1 父类名.成员变量    父类名.成员方法(self)
# 2 super().成员变量    super().成员方法()

class myPhone(Phone):
    producer = 'Huawei' # 复写父类的属性

    def call_by_5g(self): # 复写父类的方法
        print('子类的5g通话')

        print(f'父类的厂商为：{Phone.producer}') # 调用父类的被复写的属性——方式1
        print(f'父类的厂商为：{super().producer}') # 调用父类的被复写的属性——方式2

        print(f'子类的厂商为：{self.producer}')

        Phone.call_by_5g(self) # 调用父类的被复写的方法——方式1
        super().call_by_5g() # 调用父类的被复写的方法——方式2

pura = myPhone()

pura.call_by_5g()

print(pura.producer)