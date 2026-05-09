# 字符串有三种定义方式
# 1 单引号定义
name_1 = '雒飞'
# 2 三引号定义
name_2 = """luo
fei"""
# 3 双引号定义
name_3 = "luofei"

print(type(name_1), name_1)
print(type(name_2), name_2)
print(type(name_3), name_3)

# 字符串包含 ' " ——转义字符法\（与C语言类似）
name_4 = "\""
print(type(name_4), name_4)

print("\\") # 打印\

# 字符串包含 ' " ——用单引号包含双引号、用双引号包含单引号
name_5 = "sgsha'jkkk"
print(type(name_5), name_5)

name_6 = '"cc"'
print(type(name_6), name_6)