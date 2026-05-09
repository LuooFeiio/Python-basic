"""
if condition1:
    语句
    if condition2:
        语句
"""

# 嵌套要注意空格缩进

if int(input("请确认你的身高（cm）：")) > 120:

    print("你的身高大于120cm，可能要买门票。")
    print("但是如果你的会员等级大于3，则也可以免费游玩。")

    if int(input("请确认你的会员等级（1 ~ 5）：")) > 3:
        print("你是尊贵会员，不用门票")
    else:
        print("你需要支付门票费10￥")

else:
    print("身高小于120cm免费游玩游乐园")

print("祝游玩愉快！")