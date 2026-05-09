"""
content = f.read()
count = content.count('itheima')
print(...)
"""

f = open('D:\\Develop\\LearnPython\\File\\word.txt', 'r', encoding = 'UTF-8')

count = 0

for line in f: # type(line) = str
    count += line.count('itheima') # 使用了字符串的count方法

print(f'统计itheima单词出现的次数：{count}')

f.close()