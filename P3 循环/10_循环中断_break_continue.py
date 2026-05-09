# continue：中断本次循环，进入下次循环
"""
for i in range(1, 100):
    语句1
    continue
    语句2 # 语句2不会执行
"""
for i in range(1, 10):
    print("语句1")
    continue
    print("语句2") # 语句2不会执行

# continue在嵌套循环中的作用
"""
语句1和语句2会执行
for i in range(1, 100):
    语句1
    for j in range(1, 100):
        语句2
        continue
        语句3 # 语句3不会执行
"""
for i in range(1, 5):
    print("sentence1")
    for j in range(1, 5):
        print("\tsentence2")
        continue
        print("\tsentence3") # 语句3不会执行