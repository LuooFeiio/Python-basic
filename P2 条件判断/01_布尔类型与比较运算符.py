# 布尔类型：True表示真，False表示假（仅这两个字面量）

bool_1 = True
bool_2 = False
print(f'bool_1的内容：{bool_1}，类型为{type(bool_1)}')

# 逻辑运算符：and、or、not

print(not(bool_1 or bool_2))
print(not(bool_1 and bool_2))

# 比较运算符：① ==、② !=、③ >、④ <、⑤ >=、⑥ <=
print(1 > 2, type(1 > 2))

result = 1 <= 2
print(result, type(result))

# 字符串也可以比较
name1 = "qwer"
name2 = "asdf"
print(f'name1 == name2 的结果是：{name1 == name2}')