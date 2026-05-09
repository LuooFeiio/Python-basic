# 面向对象三大特性：封装、继承、多态

# 封装
# 对用户开放的属性&行为、对用户隐藏的属性&行为

# 类支持：私有成员变量/方法
# 私有成员定义方法：变量/方法名以__开头（两个下划线）

# 私有成员不对外开放，仅供内部使用
# 私有成员无法以“类对象.成员”的方式调用，可以被其他成员使用

class Phone:
    producer = 'xiaomi' # 生产商

    __current_voltage = 0.5 # 私有变量——手机当前运行电压

    def __keep_single_core(self): # 私有方法
        print('让CPU以单核模式运行')

    def call_by_5G(self): # 公用方法
        if self.__current_voltage > 1: # 成员方法中使用了私有变量
            print('5G通话已开启！')
        else:
            self.__keep_single_core() # 成员方法中使用了私有方法
            print('电量不足，无法使用5G，正在单核模式运行')

    def charge(self):
        print('充电模式')
        self.__current_voltage = 1.5

phone = Phone()

# print(phone.__current_voltage) # 报错
print(phone.producer)

# phone.__keep_single_core() # 使用私有方法：报错
phone.call_by_5G()

phone.charge()
phone.call_by_5G()