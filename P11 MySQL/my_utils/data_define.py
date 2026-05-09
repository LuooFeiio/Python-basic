# 数据定义的类——可以放在“data_define.py”文件
class Record:
    date = None # 日期
    order_id = None # 订单号
    money = None # 销售额
    province = None # 销售省份

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self): # 魔术方法
        return f'{self.date}, {self.order_id}, {self.money}, {self.province}'