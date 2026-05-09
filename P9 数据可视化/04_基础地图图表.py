"""
演示地图可视化的基本使用
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
# 添加数据
map.add("测试地图-各省数据", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts = VisualMapOpts( # 视觉映射
        is_show = True,
        is_piecewise = True,
        pieces = [
            {"min": 1, "max": 100, "label": "1-100", "color": "#99FF99"}, # RGB颜色对照表
            {"min": 101, "max": 200, "label": "101-200", "color": "#FFFF77"},
            {"min": 201, "max": 300, "label": "201-300", "color": "#FF8800"},
            {"min": 301, "max": 400, "label": "301-400", "color": "#FF3EFF"},
            {"min": 401, "max": 500, "label": "401-500", "color": "#FF0000"}
        ]
    )
)

# 绘图
map.render('基础地图图表.html')