# 正则表达式，又称规则表达式（Regular Expression）
# 是使用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换那些符合某个模式（规则）的文本

# Python正则表达式，使用re模块，并基于re模块中三个基础方法来做正则匹配
# 分别是：match、search、findall三个基础方法

# re.match(匹配规则, 被匹配字符串)
# 从被匹配字符串开头进行匹配，匹配成功返回匹配对象（包含匹配的信息），匹配不成功返回空

# re.search(匹配规则, 被匹配字符串)
# 搜索整个字符串，找出匹配的。从前向后，找到第一个后，就停止，不会继续向后；整个字符串都找不到，返回None

# re.findall(匹配规则, 被匹配字符串)
# 匹配整个字符串，找出全部匹配项；找不到返回空list []

import re

s1 = "1python itheima python python"
s2 = "python itheima python"

# match 从头匹配
result_1 = re.match("python", s1)
print(result_1) # None 下面两行会报错
# print(result_1.span())
# print(result_1.group())

result_2 = re.match("python", s2)
print(result_2) # <re.Match object; span=(0, 6), match='python'>
print(result_2.span()) # (0, 6) 意味着[0, 6)
print(result_2.group()) # python

# search 搜索匹配
result_3 = re.search("python2", s1)
print(result_3) # None

result_4 = re.search("python", s1)
print(result_4) # <re.Match object; span=(1, 7), match='python'>
print(result_4.span()) # (1, 7) 意味着[1, 7)
print(result_4.group())

# findall 搜索全部匹配
result_5 = re.findall("python", s1)
print(result_5) # ['python', 'python', 'python']

s3 = 'whosyourdaddy'
result_6 = re.findall("python", s3)
print(result_6) # []

# re模块的三个主要方法
# re.match 从头开始匹配，匹配第一个命中项
# re.search 全局匹配，匹配第一个命中项
# re.findall 全局匹配，匹配全部命中项