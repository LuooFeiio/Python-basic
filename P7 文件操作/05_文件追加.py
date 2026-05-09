# a模式：文件不存在会创建文件；文件存在会在最后追加写入

# 1.打开文件，通过a模式打开即可
f = open('python.txt', 'a', encoding = 'utf-8')

# 2.文件写入
f.write('\n追加写入测试！')

# 3.内容刷新
f.flush()

# 4.关闭文件
f.close()