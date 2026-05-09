# 装饰器：创建一个闭包函数，在闭包函数内调用目标函数
# 可以达到不改动目标函数的同时，增加额外的功能

def outer(func):

    def inner():
        print('我要睡觉了...')
        func()
        print('我要起床了.')

    return inner

# 装饰器的语法糖写法
@outer
def sleep():
    import random
    import time
    print('sleep...', end='\t')
    t = random.randint(1, 5)
    time.sleep(t)
    print(f'({t})')
# 注意调用效果：相当于将sleep函数传入outer函数，再调用outer函数的返回函数
sleep()

def stayup():
    print('睡不着stayup...')
# 传统的写法：将stayup函数传入outer函数，再调用outer函数的返回函数
fn = outer(stayup)
fn()

sleep() # 增加的功能仍在