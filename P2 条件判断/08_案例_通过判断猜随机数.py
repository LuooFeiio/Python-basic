# 随机数生成
import random
# 产生 1 ~ 10 范围的随机数
num = random.randint(1,10)
# print(num)

guess_num = int(input("输入你猜的数："))

if num == guess_num:
    print("恭喜，第一次就猜对了！")
else:
    if num > guess_num:
        print("猜小了")
    else:
        print("猜大了")

    guess_num = int(input("第二次输入你猜的数："))

    if num == guess_num:
        print("恭喜，第二次猜对了！")
    else:
        if num > guess_num:
            print("猜小了")
        else:
            print("猜大了")

        guess_num = int(input("第三次输入你猜的数："))

        if num == guess_num:
            print("恭喜，第三次猜对了！")
        else:
            print(f"最终没猜对，生成的随机数是：{num}")

print("Game over!")