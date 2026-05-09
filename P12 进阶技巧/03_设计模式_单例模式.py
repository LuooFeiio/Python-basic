# 某些场景下，我们只需要一个实例对象就够了
# 对一个类，只获取其唯一的实例对象，持续复用它

from module_SingletonPattern import stl
# 引入的stl是一个实例
s1 = stl
s2 = stl

print(id(s1)) # s1与s2的id是一样的
print(id(s2))
print(s1) # s1与s2的地址相同
print(s2)