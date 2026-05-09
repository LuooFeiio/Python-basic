-- DQL

-- 结果排序，order by关键字
-- SELECT 列|聚合函数|* FROM 表 [WHERE 条件] [GROUP BY 列] ORDER BY ... [ASC|DESC];

DROP table if EXISTS student;
# 建表
CREATE TABLE student(
	id INT,
	name VARCHAR(20),
	age INT,
	gender VARCHAR(10)
);
# 插入数据
INSERT INTO student VALUES(10001, '周杰轮', 31, '男'), (10002, '王力鸿', 33, '男'), (10003, '蔡依琳', 35, '女'), (10004, '林志灵', 36, '女'), 
(10005, '刘德滑', 33, '男'), (10006, '张大山', 10, '男'), (10007, '刘志龙', 11, '男'), (10008, '王潇潇', 33, '女'), 
(10009, '张一梅', 20, '女'), (10010, '王一倩', 13, '女'), (10011, '陈一迅', 31, '男'), (10012, '张晓光', 33, '男'), 
(10013, '李大晓', 15, '男'), (10014, '吕甜甜', 36, '女'), (10015, '曾悦悦', 31, '女'), (10016, '刘佳慧', 21, '女'), 
(10017, '项羽凡', 23, '男'), (10018, '刘德强', 26, '男'), (10019, '王强强', 11, '男'), (10020, '林志慧', 25, '女');

# 按年龄降序排列
select * from student ORDER by age DESC;

# 按id升序排列
select * from student where age >= 31 ORDER by id ASC;

# 升序是默认的
select * from student where age >= 31 ORDER by id;

-- 结果分页限制，limit关键字
-- SELECT 列|聚合函数|* FROM 表 [WHERE ...] [GROUP BY ...] [ORDER BY ... [ASC|DESC]] LIMIT n[, m];

# 只看5条数据
select * from student limit 5;

# 跳过10条记录后，看接下来的5条数据
select * from student limit 10, 5;

select age, count(*) from student where age >=26
group by age order by age ASC
limit 3;

-- 关键字的顺序按上述排序！
-- select与from关键字是必须的！
-- WHERE、GROUP BY、ORDER BY、LIMIT关键字是可选的.