"""
if condition1:
    ...
elif condition2: # 注意冒号:
    ...
elif condition3:
    ...
...
elif conditionN:
    ...
else:
    ...
"""

print("欢迎来游乐园！")

height = int(input("请输入你身高（cm）："))
vip_level = int(input("请输入你的vip等级（1 ~ 5）"))

if height < 120:
    print("您的身高小于120cm，可以免费游玩！")
elif vip_level > 3:
    print("您的会员等级大于3，可以免费游玩！")
else:
    print("不好意思，你不满足上面两个条件，需要付费10￥")

# 下面的写法更优雅
"""
if int(input("请输入你身高（cm）：")) < 120:
    print("您的身高小于120cm，可以免费游玩！")
elif int(input("请输入你的vip等级（1 ~ 5）")) > 3:
    print("您的会员等级大于3，可以免费游玩！")
else:
    print("不好意思，你不满足上面两个条件，需要付费10￥")
"""

print("游玩愉快")

# 可以有多个elif
# 可以没有else

# python用缩进来表示代码块，C语言用{}来表示代码块

# CTRL + / 注释/解除注释