# 面向对象三大特性：封装、继承、多态

# 继承：单继承、多继承

# 单继承
"""
class 类名(父类名):
    类内容体
"""

class Phone_basic:
    IMEI = None
    producer = 'XiaoMi'

    def call_by_4g(self):
        print('4G通话')

class Phone_2026(Phone_basic):
    face_id = '10001' # 专属于子类的成员变量

    def call_by_5g(self): # 专属于子类的成员方法
        print('2026新功能-5G通话')

phone = Phone_2026()

print(phone.producer) # 从父类继承的成员
phone.call_by_4g() # 从父类继承的方法

# 多继承
# class 类名(父类1, 父类2, ..., 父类N):
#     类内容体

# 若多个父类有同名的成员，那么默认以继承顺序（从左到右）为优先级

# pass关键字

class NFCreader:
    nfc_type = '第五代'
    producer = 'HuaWei'

    def read_card(self):
        print('NFC读卡')

    def write_card(self):
        print('NFC写卡')

class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print('红外遥控开启了.')

class Phone_advanced(Phone_basic, NFCreader, RemoteControl): # 多继承
    # Phone_basic类 与 NFCreader类都有producer成员变量
    # 由于优先级的原因，Phone_advanced继承了Phone_basic类的producer成员变量

    pass # pass关键字，占位语句，表示内容体为空，保证定义格式的完整性，避免语法报错

phone_adv = Phone_advanced()

print(phone_adv.nfc_type)
print(phone_adv.producer) # XiaoMi——继承有顺序优先级
phone_adv.read_card()
phone_adv.control()