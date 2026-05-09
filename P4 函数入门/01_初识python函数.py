# 如何提高代码的复用性和开发效率？——函数是其中一个答案

# print(f'Hello, {input("随便在键盘上输入些什么：")}')

# 统计字符串长度——len()——官方提供的函数
name = 'luofei'
length = len(name)
print(length)

str1 = 'qwer'
str2 = 'helloworld'
str3 = 'lanzhouuniversity'

count = 0
for s in str1:
    count += 1
print(f'字符串\"{str1}\"的长度是：{count}')

count = 0
for s in str2:
    count += 1
print(f'字符串\"{str2}\"的长度是：{count}')

count = 0
for s in str3:
    count += 1
print(f'字符串\"{str3}\"的长度是：{count}')

# 自己定义一个函数，优化上述过程
def my_len(str):
    count = 0
    for c in str:
        count += 1
    print(f'字符串\"{str}\"的长度是：{count}')

# 使用自定义的函数
my_len(str1)
my_len(str2)
my_len(str3)