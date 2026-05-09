# 异常有传递性

def fun1():
    print('fun1开始执行')
    num = 1 / 0
    print('fun1结束执行')

def fun2():
    print('fun2开始执行')
    fun1()
    print('fun2结束执行')

def main():
    print('main开始执行')
    fun2()
    print('main结束执行')

try:
    main()
except Exception as e:
    print(e)

# main开始执行
# fun2开始执行
# fun1开始执行
# division by zero