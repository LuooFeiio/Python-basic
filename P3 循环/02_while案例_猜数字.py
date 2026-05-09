# 随机数生成
import random
# 产生 1 ~ 100 范围的随机数
num = random.randint(1,100)
# print(num)

print("猜一个1 ~ 100的随机数，猜对了程序结束")

count = 1

guess_num = int(input(f"第{count}次输入你猜的数："))

while guess_num != num:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")

    count += 1
    guess_num = int(input(f"第{count}次输入你猜的数："))

print(f"第{count}次猜中了，你猜的数：{guess_num}，随机数为：{num}")
print("Game over")