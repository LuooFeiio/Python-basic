# 文件操作：打开、读or写、关闭

# 三步骤：
# ① 打开文件
# open()函数：
# open(name, mode, encoding)
# name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)
# mode：设置打开文件的模式：只读 r、写入 w、追加 a 等
# encoding：编码格式，推荐使用UTF-8 参数的顺序不是第三位，不能用位置参数，用关键字参数指定

# ② 读or写文件

# ③ 关闭文件
# 文件的关闭：close()方法
# 如果不用close，同时程序没有停止运行，那么这个文件将一直被Python程序占用

f = open('Test.txt', 'r', encoding = 'UTF-8')
print(type(f))

# 1 read()方法：
# 文件对象.read(num)
# num —— 从文件中读取数据的长度（单位：字节） 如果没有传入num，则读取文件所有的数据
print(f'读取5个字节的结果：{f.read(5)}')
print(f'read方法读取剩余全部内容的结果：{f.read()}') # 从上次read的结束后开始读取

f.close()

# 2 readlines()方法：
# 按照行的方式把整个文件的内容一次性读取，返回一个列表，其中每一行的数据为一个元素
f = open('Test.txt', 'r', encoding = 'UTF-8')

lines = f.readlines()
print(lines) # ['I Love Python.\n', 'It is very useful!']
print(type(lines))

f.close()

# 3 readline()方法：
# 一次读取一行内容
f = open('Test.txt', 'r', encoding = 'UTF-8')

l1 = f.readline()
l2 = f.readline()
print(type(l1), l1)
print(type(l2), l2)

f.close()

# 4 for循环读取文件行
f = open('Test.txt', 'r', encoding = 'UTF-8')

for line in f: # for line in open("python.txt", "r"):
    print(line)

f.close()

# 5 with open语法：
# 在with open的语句块中对文件进行操作
# 操作完成后自动关闭文件，避免遗忘使用close方法
with open('Test.txt', 'r', encoding = 'UTF-8') as f:
    print('使用with open方式读取文件')
    for line in f:
        print(line)
    print('自动关闭文件')