# 字符串无法修改

# 字符串的下标索引
name = 'python'
print(name[0]) # p
print(name[-1]) # n

# 字符串的常用操作
# • 查找特定字符串的下标索引 index()
# • 字符串的替换 replace()
# • 字符串的分割 split()
# • 字符串的规整 strip()
# • 统计字符串中某个字符串出现的次数 count()
# • 字符串的长度 len(字符串)

# 1 查找特定字符串的下标索引
# 语法：字符串.index(字符串)
my_str = 'python and c'
print(my_str.index('and')) # 7：返回了‘and’在my_str中的起始下标

# 2 字符串的替换
# 语法：字符串.replace(字符串1, 字符串2)
# 功能：将字符串中的字符串1，替换为字符串2
# 注意：不是修改字符串本身，而是得到一个新的字符串
new_str = my_str.replace('python', 'cpp')
print(my_str)
print(new_str)

# 3 字符串的分割
# 语法：字符串.split(分隔字符串)
# 功能：按指定的分隔字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不变，而是得到一个新的列表
new_list = my_str.split(' and ')
print(new_list) # ['python', 'c']

# 4 字符串的规整
# 语法1：字符串.strip() —— 去掉前后空格
# 语法2：字符串.strip(指定字符串) —— 去掉前后指定字符串
# 注意：不是修改字符串本身，而是得到一个新的字符串
str1 = '  python and verilog  ' # 注意前后有空格
print(str1.strip()) # strip方法没有传入参数

str2 = '12c v.s. verilog21'
print(str2.strip('12')) # "c v.s. verilog"：str2前后的'1'和'2'都会移除

# 5 统计字符串中某个字符串出现的次数
# 语法：字符串.count(某个字符串)
str3 = "cpp cpp python c"
print(str3.count('cpp')) # 2

# 6 字符串的长度
# 语法：len(字符串)
print(len(str3)) # 16

# 字符串的遍历：类似列表与元组