# 下标范围：0 ~ len - 1
# print(list[0])
# print(list[1])
# ...

name_list = ['python', 'c', 'c++', 'verilog']
print(name_list[0]) # python
print(name_list[1]) # c
print(name_list[2]) # c++
print(name_list[3]) # verilog

# 反向索引
# 下标范围：-len ... -3 -2 -1
# 最后一个元素的索引为-1，倒数第二个元素的索引为-2，...
print(name_list[-4]) # python
print(name_list[-1]) # verilog

# 嵌套列表的下标
my_list_1 = [['c', 'a', 'b'], [1, 2, 3]]
print(my_list_1[0][0]) # c
print(my_list_1[1][2]) # 3

print(my_list_1[-2][-3]) # c
print(my_list_1[-1][-1]) # 3

print(my_list_1[1][-2]) # 2

# 下标索引不能超出范围！