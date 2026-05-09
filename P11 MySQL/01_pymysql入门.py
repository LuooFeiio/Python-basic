# windows命令提示符：“pip install pymysql”

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host = "localhost", # 主机名
    port = 3306, # 端口
    user = "root", # 账户
    password = "134617" # 密码
)
print(conn.get_server_info())

# 1 执行非查询性质SQL

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql
# cursor.execute("create table test_pymysql(id int);") # “;”号可以不写

# 2 执行查询性质SQL

# 构建到MySQL数据库的链接
# 获取游标对象
# 选择数据库
# 通过游标对象，执行sql语句
cursor.execute("select * from student")
# 获取查询结果
results: tuple = cursor.fetchall() # 类型注解
for r in results:
    print(r) # 大元组中小元组

# 关闭链接
conn.close()