import random

account = 10000

for i in range(20):
    if account <= 0:
        print('工资发完了，下个月领取吧。')
        break

    grade = random.randint(1, 10)

    if grade < 5:
        print(f"员工{i + 1}，绩效分数：{grade}，低于5，不发工资，下一位。")
    else:
        account = account - 1000
        print(f"向员工{i + 1}发放工资1000￥，账户余额{account}￥。")