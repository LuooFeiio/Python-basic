-- DML

# use 库名;
-- 数据插入，基本语法：
-- INSERT INTO 表[(列1, 列2, ..., 列N)] values(值1, 值2, ..., 值N)[, (值1, 值2, ..., 值N), ..., (值1, 值2, ..., 值N)];
create TABLE student(
	id INT,
	name VARCHAR(20),
	age INT
);

# 仅插入id列数据
insert INTO student(id) VALUES(10001), (10002), (10003);
insert INTO student(id) VALUES(10004);
insert INTO student(id) VALUES(10005);

# 所有列插入数据
# SQL仅支持单引号，字符串需要被单引号包起来
insert into student(id, name, age) values(10006, 'fee', 18), (10007, 'zhao', 19);
insert into student(id, name, age) values(10007, '刘', 30);

-- 数据删除，基本语法：
-- DELETE FROM 表名称 [WHERE 条件判断];
-- 条件判断：列 操作符 值
-- 操作符：=、<、>、<=、>=、!=等
-- 如：id = 5、id < 3、id >= 6、id != 5
DROP table if EXISTS student;
create TABLE student(
	id INT,
	name VARCHAR(20),
	age INT
);
insert into student(id, name, age) values(10001, 'fee', 18), (10002, 'zhao', 19), 
(10003, '王', 20), (10004, '刘', 21), (10005, '李', 22);

DELETE FROM student WHERE id = 10001;
DELETE FROM student WHERE id <= 10003;
DELETE FROM student WHERE age = 21;

# 删除整张表的数据
DELETE FROM student;

-- 数据更新，基本语法：
-- UPDATE 表名 SET 列 = 值 [WHERE 条件判断];
insert into student(id, name, age) values(10001, 'fee', 18), (10002, 'zhao', 19), 
(10003, '王', 20), (10004, '刘', 21), (10005, '李', 22);

UPDATE student set name = 'luofei' where id = 10001;

# 将表的某一列全部修改为同一个值
UPDATE student set name = 'UnKnown';