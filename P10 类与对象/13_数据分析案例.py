# 1 设计一个类，可以完成数据的封装 ✓
# 2 设计一个抽象类，定义文件读取的相关功能，用子类实现具体的功能 ✓
# 3 读取文件，产生数据对象
# 4 计算每天的销售额
# 5 用pyecharts绘图

from 综合案例数据文件.data_define import Record
from 综合案例数据文件.file_define import FileReader, TextFileReader, JsonFileReader

from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

tfr = TextFileReader('./综合案例数据文件/2011年1月销售数据.txt')
jfr = JsonFileReader('./综合案例数据文件/2011年2月销售数据JSON.txt')

jan_data = tfr.read_date() # type: list[Record]
feb_data = jfr.read_date() # type: list[Record]

# 将上面两个list合并
all_data = jan_data + feb_data  # type: list[Record]

# 数据计算——每天的销售额
# 字典{key: value}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys(): # 这个写法头回见——in: Python的成员运算符，用于检查左边的值是否存在于右边的集合中，返回布尔值
        # 问AI——“if record.date in data_dict:”这个写法更优雅
        data_dict[record.date] += record.money
        # 如果字典的key中有当前日期的记录了，将当前记录的money累加到字典key对应的value中去
    else:
        data_dict[record.date] = record.money
# 数据准备完毕
# print(data_dict)

# 可视化开发
bar = Bar(init_opts = InitOpts(theme = ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额', list(data_dict.values()), label_opts = LabelOpts(is_show = False))
# data_dict.values()第一次见这个写法
bar.set_global_opts(
    title_opts = TitleOpts(is_show = True, title = '每日销售额', pos_top = 'top')
)

bar.render('每日销售额柱状图.html')