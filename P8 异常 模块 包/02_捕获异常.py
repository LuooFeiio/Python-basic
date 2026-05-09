"""
基本的异常捕获——省事的写法：
try:
    可能发生Bug的代码
except:
    如果出现异常执行的代码

全面的语法：
try:
    可能发生Bug的代码
except:
    如果出现异常执行的代码
else:
    # else是可选的语句（可写可不写）
    没有异常时执行的代码
finally:
    # 可选语句
    无论是否有异常都会执行的代码
"""

# 捕获指定的异常
try:
    print(name) # name是未定义的变量
except NameError as e:
    print(e) # 异常信息
    print('出现了变量未定义的异常')

try:
    1 / 0
except ZeroDivisionError:
    print('出现了除数为0的异常')

# 捕获多个异常
try:
    print(1 / 0)
except (NameError, ZeroDivisionError): # 以元组的形式，列出多个异常
    print('出现了异常...（变量未定义 或 除0 异常）')

# 捕获所有异常
try:
    f = open('Laugh.txt', 'r', encoding = "UTF-8")
except Exception as e: # Exception是“顶级的异常”，其余的异常都是他的小弟
    print(f'出现异常了，异常信息为：{e}')

# 异常捕获——全面的写法
try:
    f = open('Try.txt', 'r', encoding = "UTF-8")
except Exception as e:
    print(f'出现异常：{e}')
    f = open('Try.txt', 'w', encoding = "UTF-8")
    f.write('打开文件\nHello!')
else:
    print('打开文件过程中没有出现异常！')
    for line in f:
        print(line)
finally:
    print('有没有出现异常都要执行finally语句块！')
    f.close()