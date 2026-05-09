# 什么是面向对象编程：
# 1 设计类 2 基于类创建对象 3 由具体的对象做具体工作
# 开发效率

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

clock1 = Clock()

clock1.ring() # 电脑响铃