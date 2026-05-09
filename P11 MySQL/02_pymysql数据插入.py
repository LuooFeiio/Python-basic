from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host = "localhost", # 主机名
    port = 3306, # 端口
    user = "root", # 账户
    password = "134617", # 密码
    autocommit = True # 设置自动提交后，无需再手动调用commit方法
)
# print(conn.get_server_info())

#  执行SQL数据插入

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("drop table if exists test_pymysql;") # “;”号可以不写

# 数据插入，需要确认
cursor.execute("insert into student values(20002, '华为遥遥领先', 55, '男');")
# 需要通过commit确认
# conn.commit() # 设置自动提交后，无需再手动调用commit方法

# 关闭链接
conn.close()