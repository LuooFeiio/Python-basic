"""
if 要判断的条件(布尔类型): # 注意冒号:
[缩进4空格]条件成立时，要做的事
"""

age = 60

if age >= 18:
    print("已成年")

if age >= 18:
    print("Time flies!")
    print("即将读研。")

print("而立之年")

print("欢迎来到游乐园，儿童免费，成人收费")
age_str = input("请输入你的年龄：") # input得到的都是字符串

if int(age_str) >= 18: # int()类型转换
    print("你是成人，要收费！")

if int(age_str) < 18:
    print("你是儿童，免费！")

print("祝游玩愉快")