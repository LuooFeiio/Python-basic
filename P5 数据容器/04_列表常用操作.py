"""
• 定义
• 使用下标获取元素

列表的方法：（方法：定义在类class中的函数）
• 查找某元素的下标 index
• 修改元素
• 插入元素 insert
• 追加元素 append、extend
• 删除元素 del、pop、remove
• 清空列表 clear
• 统计某元素个数 count
• 统计列表中全部元素的数量 len
"""

# 1 查找某元素的下标
# 语法：列表.index(元素)——有返回值
# 如果找到，返回（第一个匹配元素的）下标；如果没找到，返回ValueError报错
mylist = ['python', 'c', 'c++', 'verilog']
index_1 = mylist.index('c++')
print(index_1) # 2

# index_2 = mylist.index('cpp') # 报错

# 2 修改元素
mylist[2] = 'cpp'
print(mylist)

# 3 插入元素
# 语法：列表.insert(下标, 元素)
# 在指定的下标位置插入元素
mylist.insert(2, 'java')
print(mylist)

# 4 追加单个元素
# 语法：列表.append(元素)
# 将元素追加到列表尾部
mylist.append('sysverilog')
print(mylist)

# 5 追加一批元素
# 语法：列表.extend(其他数据容器)
# 将其他数据容器中的元素依次追加到列表尾部
mylist.extend(['linux', 'unix', 'windows', 'macos'])
print(mylist)

templist = ['algorithm', 'integratedcircuits']
mylist.extend(templist)
print(mylist)

# 6 删除元素
# 语法1：del 列表[下标]
# 语法2：列表.pop(下标)——有返回值
del mylist[-1]
print(mylist)

element = mylist.pop(2)
print(element, mylist)

# 7 删除某元素在列表中的第一个匹配项
# 语法：列表.remove(元素)
mylist.remove('macos')
print(mylist)

# 8 清空列表
# 语法：列表.clear()
mylist.clear()
print(mylist) # []

# 9 统计某元素在列表中的数量
# 语法：列表.count(元素)——有返回值
mylist_2 = [1, 1, 1, 2, 3]
n = mylist_2.count(1)
print(n) # 3

# 10 统计列表中全部元素的数量
# 语法：len(列表)——有返回值
l = len(mylist_2)
print(l) # 5

# 列表的方法：（方法：定义在类class中的函数）
# • 查找某元素的下标 index
# • 修改元素
# • 插入元素 insert
# • 追加元素 append、extend
# • 删除元素 del、pop、remove
# • 清空列表 clear
# • 统计某元素个数 count
# • 统计列表中全部元素的数量 len