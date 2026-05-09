# 局部变量 全局变量

def test_a():
    num_1 = 100 # 局部变量：定义在函数内部，函数外部无法使用
    print(f"test_a: num_1 = {num_1}是函数内部的变量，属于局部变量")

test_a()
# print(num) # 直接运行这条语句会报错

num_2 = 300 # 全局变量：定义在函数外面，函数内外均可使用

def test_b():
    print(f"test_b: num_2 = {num_2}")

def test_c():
    num_2 = 600 # 此时num_2是局部变量，只在函数内部生效
    print(f"test_c: num_2 = {num_2}")

# 使用global关键字，在函数内部声明全局变量

def test_d():
    global num_2 # 声明num_2是全局变量
    num_2 = 600 # 此时num_2是全局变量
    print(f"test_d: num_2 = {num_2}")

print(num_2) # 300
test_b() # 300
test_c() # 600
test_d() # 600
print(num_2) # 600