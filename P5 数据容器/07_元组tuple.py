# 定义元组使用小括号()，使用逗号,隔开各个数据，数据可以为不同类型的
# 元组不可修改
# 如果元组中嵌套了一个list，则这个list是可以修改的

# 变量名 = 字面量
t1 = (1, "hello", [True, False])
print(t1, type(t1))

t1[-1][0] = False
t1[-1].insert(1, True)
print(t1, type(t1))

# 定义空元组
# 变量名称 = ()
t2 = ()
# 变量名称 = tuple()
t3 = tuple()

print(t2, type(t2))

# 定义只含一个元素的元组
t4 = ('hello', ) # 需要有逗号,（否则不是元组类型）
print(t4, type(t4))

# 元组也支持嵌套
t5 = (1, 'hello', (3, True))
print(t5, type(t5))

# 下标索引（类似列表）
BOOL = t5[-1][1]
print(BOOL, type(BOOL))

# 元组的操作：
# index()——查找某个数据，如果存在返回对应的下标，否则报错
# count()——统计某个数据在当前元组中出现的次数
# len(元组)——统计元组的元素个数

t6 = ('python', 'c', 'c++', 'c++', 'c++', 'verilog')

index = t6.index('python')
print(index) # 0

count = t6.count('c++')
print(count) # 3

length = len(t6)
print(length) # 6个元素

# 遍历：类似列表