# 集合：不支持元素重复（集合会自动去重），且内容无序（没法下标索引访问）
# {元素1, 元素2, 元素3, 元素4, ...}
# 可以修改，元素类型可以不同

# 变量名 = 集合字面量
set_1 = {"python", "python", "c", "c", "c++", "c++", "verilog"}
print(set_1, type(set_1)) # 自动去重

# 空集合：变量名 = set()
set_2 = set()
print(set_2, type(set_2))

# 集合的方法
# • 添加新元素——add()
# • 移除元素——remove()
# • 随机取出元素——pop()
# • 清空集合——clear()
# • 取出两个集合的差集
# • 消除差集
# • 合并
# • 统计集合元素数量——len(集合)

# 1 添加新元素——add()
# 语法：集合.add(元素)——集合本身被修改
set_1.add("windows")
print(set_1)

set_1.add(True)
print(set_1)

set_1.add(100)
print(set_1)

# 2 移除元素——remove()
# 语法：集合.remove(元素)——集合本身被修改
set_1.remove('c++')
print(set_1)

# 3 随机取出元素——pop()
# 语法：集合.pop()
# 结果：会得到一个元素的结果，同时集合本身被修改，元素被移除
ele_1 = set_1.pop()
print(ele_1, type(ele_1))
print(set_1)

# 4 清空集合
# 语法：集合.clear()
set_1.clear()
print(set_1) # set()

# 5 取出两个集合的差集
# 语法：集合1.difference(集合2)
# 功能：取出集合1和集合2的差集（集合1有而集合2没有的）
# 结果：得到一个新集合，集合1与集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3) # {2, 3}

# 6 消除差集
# 语法：集合1.difference_update(集合2)
# 功能：集合1内，删除和集合2相同的元素
# 结果：集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1) # {2, 3}
print(set2)

# 7 合并
# 语法：集合1.union(集合2)
# 功能：将集合1与集合2组合成新集合
# 结果：得到新集合，集合1与集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set1)
print(set2)
print(set3) # {1, 2, 3, 5, 6}

# 8 统计集合元素数量——len(集合)
set_4 = {1, 2, 3, 5, 6, 1, 2, 3, 5, 6}
print(len(set_4)) # 5

# 遍历 没法用while循环
for item in set_4:
    print(f'集合set_4的元素有：{item}')

# 不要死记硬背，会查阅笔记
# 集合的方法
# • 添加新元素——add()
# • 移除元素——remove()
# • 随机取出元素——pop()
# • 清空集合——clear()
# • 取出两个集合的差集
# • 消除差集
# • 合并
# • 统计集合元素数量——len(集合)