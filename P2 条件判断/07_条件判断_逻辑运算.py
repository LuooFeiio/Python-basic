age = int(input("确认你的年龄："))

"""
and：(a and b)

or：(a or b)

not：not(a or b)
"""

if age >= 18 and age <= 30:

    print("年龄至少符合资格！")

    if int(input("确认你的工作年限")) > 2:
        print("工作年限也符合（> 2），可以申请奖金！")
    elif int(input("确认你的等级：")) > 3:
        print("级别 > 3，可以申请奖金！")
    else:
        print("尽管年龄合格，但工作年限和职称等级不合要求，不能申请奖金。")

else:
    print("不符合年龄要求（>= 18 and <= 30）")