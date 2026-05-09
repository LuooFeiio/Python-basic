# 1.打开文件
f = open('python.txt', 'w', encoding = 'utf-8')
# w模式：若文件不存在，则新建文件并打开；若文件存在，则清空并打开

# 2.文件写入——write方法
f.write('Hello world!\nThis is python.\nNice to meet you!') # 其实是写入了内存中

# 3.内容刷新——flush方法
f.flush() # 将内存中积攒的内容写入到硬盘的文件中

# 注意：
# 直接调用write，内容并未真正写入文件，而是会积攒在内存中，称之为缓冲区
# 当调用flush的时候，内容会真正写入文件
# 这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）

# 4.关闭文件
f.close() # close方法内置了flush功能

f = open('python.txt', 'w', encoding = 'utf-8')
f.write('Hello world!\nThis is python.\nNice to meet you!\nHa.')
f.close()

# import time
# time.sleep(60000)