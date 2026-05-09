"""
thread_obj = threading.Thread([group[, target[, name[, args[, kwargs]]]]])
-group：暂时无用，预留参数
-target：执行的目标函数名
-name：线程名，一般不用设置
-args：以元组的方式给执行的任务传参
-kwargs：以字典的方式给执行的任务传参
"""

import time
import threading

def sing(msg):
    while True:
        print(msg) # '我在唱歌，啦啦啦...'
        time.sleep(1)

def dance(msg):
    while True:
        print(msg) # '我在跳舞，呱呱呱...'
        time.sleep(1)

if __name__ == '__main__':
    # sing()
    # dance() # 这句不执行

    # 分别创建两个任务的线程
    sing_thread = threading.Thread(target = sing, \
                                   args = ('我在唱歌，啦啦啦...', )) # 元组中只有一个元素时(ele, )
    dance_thread = threading.Thread(target = dance, \
                                    kwargs = {'msg': '我在跳舞，呱呱呱...'})

    # 启动线程
    sing_thread.start()
    dance_thread.start()