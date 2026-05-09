import json

from 综合案例数据文件.data_define import Record

# 文件相关的类——可以放在“file_define.py”文件
# 先定义抽象类
class FileReader:
    def read_date(self) -> list[Record]:
        """读取文件中的数据，读到的每一条数据都转换为Record类对象，将他们封装到list返回"""
        pass

# 读取文本文件的类
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path # 定义成员变量记录文件的路径

    # 复写父类的抽象方法
    def read_date(self) -> list[Record]:
        f = open(self.path, 'r', encoding = 'UTF-8')

        record_list: list[Record] = [] # 类型注解

        for line in f.readlines():
            # print(line)
            line = line.strip() # 去掉'\n'
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

# 读取json文件的类
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件的路径

    # 复写父类的抽象方法
    def read_date(self) -> list[Record]:
        f = open(self.path, 'r', encoding = 'UTF-8')

        record_list: list[Record] = []  # 类型注解

        for line in f.readlines():
            data_dict = json.loads(line) # 将json格式的字符串转换为python字典格式的数据容器
            record = Record(data_dict['date'], data_dict['order_id'], data_dict['money'], data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':
    tfr = TextFileReader('./2011年1月销售数据.txt')
    list1 = tfr.read_date() # list1是列表，其中的元素是类对象

    jfr = JsonFileReader('./2011年2月销售数据JSON.txt')
    list2 = jfr.read_date()

    for l in list1:
        # l是Record类对象，该类已定义了__str__魔术方法
        print(l)

    for l in list2:
        print(l)