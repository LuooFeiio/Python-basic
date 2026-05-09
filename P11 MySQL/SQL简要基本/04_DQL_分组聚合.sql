-- DQL

# 分组聚合，基础语法：
-- SELECT 字段|聚合函数 FROM 表 [WHERE 条件] GROUP BY 列;
# 聚合函数有：
# SUM(列) 求和
# AVG(列) 求平均值
# MIN(列) 求最小值
# MAX(列) 求最大值
# COUNT(列|*) 求数量

# 注意前后的gender是对应的
select gender, avg(age) from student group by gender;

# 可有多个聚合统计
select gender, avg(age), min(age), max(age), sum(age), count(name) from student group by gender;
select gender, avg(age), min(age), max(age), sum(age), count(*) from student group by gender;
# count(*)，*表示任意列字段

# 下面这样执行会报错
select gender, name, avg(age) from student group by gender;