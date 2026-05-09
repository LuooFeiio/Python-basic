age = 18
salary = 0

# %s：%表示占位，s表示将变量变成字符串放入占位的地方 —— 与C语言的含义可能不同

message = "今年多少岁？%s。工资多少？%s" % (age, salary) # 多个变量占位
print(message)

m1 = "他今年也%s了" % age # 仅一个变量占位
print(m1)

# %d：将内容转换成整数，放入占位位置
# %f：将内容转换成浮点数，放入占位位置

height = 1.77
year = 2026
name = "雒飞"
m2 = "我是%s，出生于%d年，身高是%f米" % (name, year, height)
print(m2)