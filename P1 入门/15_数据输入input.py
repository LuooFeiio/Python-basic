# input()：功能为获取键盘敲入的数据
# input(提示信息)：可以在输入前给出提示内容
# 得到字符串类型数据

print("告诉我你是谁：")

name = input()

print("哦~你是：%s" % name)

# input语句可以直接在输入前给出提示内容
age = input("请输入你的年龄：") # 得到的age是字符串
print(type(age)) # str
print(f"哦~你 {age} 岁了") # print("哦~你 %d 岁了" % int(age))