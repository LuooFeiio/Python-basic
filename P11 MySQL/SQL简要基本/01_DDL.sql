-- 单行注释(--后面一定要有空格)
# 这也是注释(#后面推荐加上空格)

/*
多行
注释
*/

# 库 -> 表 -> 数据
-- SQL大小写不敏感，语句的结束以;为标志

# 查看数据库，语法：show databases;
-- show databases;

# 使用数据库，语法：use 数据库名称;
-- use sakila;

# 查看当前使用的数据库，语法：SELECT DATABASE();
-- select database();

# 创建数据库，语法：create database 数据库名称 [CHARSET UTF8];
-- create database test charset utf8;

# 删除数据库，语法：DROP database 数据库名称;
-- drop database test;

# 查看有哪些表，语法：show tables;
use world; # 需要先选择库
show TABLES;

# 创建表
create table student(
	# 列名称 列类型
	id int, # id列数据的类型为整数
	name varchar(10), # name列的数据为文本类型，长度为10，最大长度可填255
	age int
	# float-浮点数，date-日期类型，timestamp-时间戳类型
);

# 删除表，语法：drop table 表名称;
# 删除表，语法：drop table IF EXISTS 表名称;
drop table student;

# SQL：结构化查询语言
# SQL语言的分类
-- DDL数据定义 data define language
-- DML数据操作 data manipulate language
-- DCL数据控制 data control language
-- DQL数据查询 data query language