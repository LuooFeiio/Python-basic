my_list = ['python', 'c', 'c++', 'verilog', 'python', 'c', 'c++', 'verilog']

my_set = set() # 空集合

for item in my_list:
    my_set.add(item) # 集合添加元素，自动去重

print(my_set)