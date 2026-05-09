"""
if 条件:
    ...
else: # 注意冒号:
[缩进4空格]...
"""

print("欢迎来游乐园！")

age = int(input("请输入你的年龄："))

if age >= 18:
    print("你成年了，门票10￥")
else:
    print("未成年不用门票")

print("游玩愉快")