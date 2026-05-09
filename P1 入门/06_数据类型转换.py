# 常见转换语句
# int(x)    将x转换为一个整数
# float(x)  将x转换为一个浮点数
# str(x)    将x转换为字符串
# 这三个语句有返回结果

num_str = str(666) # 将数字转换为字符串
print(type(num_str), num_str)

float_str = str(12.34)
print(type(float_str), float_str)

string_int = int("666") # 将字符串转换为整数
print(type(string_int), string_int)

string_float = float("666.55") # 将字符串转换为浮点数
print(type(string_float), string_float)

# “万物皆可转成字符串”
# 不是所有的字符串都能转换成数字

# 整数转浮点数
f_num = float(12)
print(type(f_num), f_num)

# 浮点数转整数
int_num = int(12.99999999999)
print(type(int_num), int_num) # 12

int_num = int(-12.9999999999)
print(type(int_num), int_num) # -12