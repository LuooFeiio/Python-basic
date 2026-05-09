# SQL脚本：
"""
create database py_sql charset utf8;

use py_sql;

create table orders(
	order_date date,
	order_id varchar(255),
	money int,
	province varchar(10)
);
"""

from my_utils.data_define import Record
from my_utils.file_define import FileReader, TextFileReader, JsonFileReader

tfr = TextFileReader('./my_utils/2011年1月销售数据.txt')
jfr = JsonFileReader('./my_utils/2011年2月销售数据JSON.txt')

jan_data = tfr.read_date() # type: list[Record]
feb_data = jfr.read_date() # type: list[Record]

# 将上面两个list合并
all_data = jan_data + feb_data  # type: list[Record]

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host = "localhost", # 主机名
    port = 3306, # 端口
    user = "root", # 账户
    password = "134617", # 密码
    autocommit = True # 设置自动提交后，无需再手动调用commit方法
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) values('{record.date}', '{record.order_id}', {record.money}, '{record.province}');"
    # print(sql)

    # 执行sql语句
    cursor.execute(sql)

# 关闭链接
conn.close()