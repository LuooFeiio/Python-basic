from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# csv格式文件可以由 记事本 Excel notepad++ 软件打开
f = open("./动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding = "GB2312")
data_lines = f.readlines() # 返回一个列表
f.close()
# print(data_lines)

# 删除第一条数据：'year,GDP,rate\n'
data_lines.pop(0)

# 将数据转化为字典格式：
# {年份: [[国家, GDP], [国家, GDP], [国家, GDP] ...], 年份: [[国家, GDP], [国家, GDP], [国家, GDP] ...], ...}
# {1960: [[中国, GDP], [美国, GDP], [英国, GDP] ...], 1961: [[中国, GDP], [美国, GDP], [英国, GDP] ...], ...}

# 先定义一个字典对象
data_dict = {}

for line in data_lines:
    year = int(line.split(',')[0]) # 年份
    country = line.split(',')[1] # 国家
    gdp = float(line.split(',')[2]) # GDP（有些数据由科学计数法表示，使用float()方法转换）（float()方法顺便去掉了'\n'）

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = [] # year对应的value创建空列表
        data_dict[year].append([country, gdp]) # 再追加数据
# print(data_dict)

# 创建时间线对象
timeline = Timeline({'theme': ThemeType.LIGHT})

# print(data_dict.keys())
sorted_year_list = sorted(data_dict.keys()) # 获取升序的年份：1960，1961，...，2019
# print(sorted_year_list)
for year in sorted_year_list:
    # 对每一年的数据降序排序
    data_dict[year].sort(key = lambda element: element[1], reverse = True)

    # 取出本年份前8名
    year_data = data_dict[year][0: 8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # x轴添加国家
        y_data.append(country_gdp[1] / 100000000) # y轴添加本年对应国家的GDP，以亿为单位

    # for循环每一年的数据，基于每年的数据，创建每一年的Bar对象
    bar = Bar()
    x_data.reverse() # 微调
    y_data.reverse() # 微调
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts = LabelOpts(position = 'right'))
    bar.reversal_axis() # 反转x y轴
    bar.set_global_opts( # 微调
        title_opts = TitleOpts(title = f'{year}年全球前八GDP数据', pos_left = "left", pos_top = "top"), # 标题
        legend_opts = LegendOpts(is_show = True, pos_left = 'center', pos_top = 'top') # 图例
    )

    # for循环中将每一年的Bar对象添加到时间线对象中
    timeline.add(bar, str(year))

# 时间线对象的设置
timeline.add_schema(
    play_interval = 1000, # 1秒种的播放间隔
    is_timeline_show = True, # 显示时间线
    is_auto_play = True, # 自动播放
    is_loop_play = False # 不循环
)

# 绘图
timeline.render('1960-2019全球GDP前八国家.html')