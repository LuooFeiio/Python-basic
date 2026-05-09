# break：直接结束循环

for i in range(1, 10):
    print(f'循环体执行了{i}次')
    break
    print('这里的语句执行了么？')
print('Loop Over!')

# 循环嵌套的情况下，如果break语句在内层循环中，则内层循环直接结束，但外层循环仍继续

for i in range(1, 5):
    print("sentence1")
    for j in range(1, 5):
        print("\tsentence2")
        break
        print("\tsentence3")