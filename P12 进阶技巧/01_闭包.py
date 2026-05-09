# 闭包：定义双层嵌套函数，内层函数可以访问外层函数的变量
# 将内层函数作为外层函数的返回，此内层函数就是闭包函数
# nonlocal关键字

# 简单闭包
def outer(logo: str):

    def inner(msg: str):
        print(f'<{logo}> {msg} <{logo}>') # 内层函数访问了外层函数的变量

    return inner # 将内层函数作为外层函数的返回

fn1 = outer('华为') # fn1是一个函数inner
print(type(fn1))

fn1('海思') # <华为> 海思 <华为>
fn1('鸿蒙') # <华为> 鸿蒙 <华为>

outer('Huawei')('海思') # <Huawei> 海思 <Huawei>
outer('Huawei')('鸿蒙') # <Huawei> 鸿蒙 <Huawei>
outer('小米')('Redmi') # <小米> Redmi <小米>

# nonlocal关键字：声明函数外部的变量，使外部变量在函数内部可修改
def outside(num1):

    def inside(num2):
        nonlocal num1 # 对于inside函数而言，num1是外部变量
        num1 += num2 # 修改了num1外部变量
        print(num1)

    return inside

fout = outside(10) # fout是一个函数inside
fout(5) # 15
fout(5) # 20，持续对num1修改
fout(5) # 25

outside(10)(5) # 15
outside(10)(5) # 15

# ATM取钱案例
def accout_create(initial_amount = 0):

    def ATM(num: int, deposit: bool = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f'存款：+{num}，账户余额：{initial_amount}')
        else:
            initial_amount -= num
            print(f'取款：-{num}，账户余额：{initial_amount}')

    return ATM

atm = accout_create(1000)
atm(100)
atm(120, True)
atm(200, False)

# 闭包的优点：
# 无需定义全局变量即可实现通过函数，持续地访问或修改某个值
# 闭包使用的变量的作用域在函数内，难以被错误地调用或修改
# 闭包的缺点：
# 由于内部函数持续地引用外部函数的值，会导致这一部分内存空间一直被占用