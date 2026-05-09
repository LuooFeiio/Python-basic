a = 10

if int(input("请输入第一次猜的数字：")) == a:
    print("第一次就猜对了")
elif int(input("不对，再猜一次：")) == a:
    print("第二次猜对了")
elif int(input("不对，再猜最后一次：")) == a:
    print("第三次终于猜对了")
else:
    print(f'Sorry，全部猜错了，我想的是{a}')