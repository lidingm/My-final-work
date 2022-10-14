# MySQL

## SQL

### 通用语法

1、SQL语句可以单行或多行书写，以分号结尾。

2、可以用空格来增强语句的可读性

3、SQL语句不区分大小写

4、--或者#注释内容（单行注释）

5、多行注释/* 注释内容  */ 

### SQL分类

#### 启动与停止

- 启动 `net start mysql80`
- 停止 `net stop mysql80`

#### 客户端连接

- MySQL提供的客户端命令工具 输入密码连接
- 用cmd连接，不过需要配置环境变量

#### DDL

*定义语言，用来定义数据库对象（数据库、表、字段）*

##### 数据库操作

- 查询 查询所有数据库： `show databases`

  ​         查询当前数据库： `select databases()`

- 创建 ([]可选)

   `create database[if not exits]数据库名[defaul charset 字符集][collate 排序规则]`

- 删除 `drop database[if exits]数据库名`

- 使用 `USE 数据库名`

##### 表操作

查询当前数据库所有表：
`show tables;`
查询表结构：
`desc 表名;`
查询指定表的建表语句：
`show create table 表名;`

创建表：

```mysql
create table 表名（
   字段1 类型 [comment 注释]   下同
   ）[comment 表注释]
```

*最后一个字段后面没有逗号*

- 添加字段：

  `alter table 表名 add 字段名 类型(长度)[约束] [comment 注释];`

  例：`alter table emp add nickname varchar(20) comment '昵称';`

- 修改数据类型：

  `alter table 表名 modify 字段名 新数据类型(长度);`

- 修改字段名和字段类型：

  `alter table 表名 change 旧字段名 新字段名 类型(长度) [comment 注释] [约束];`

  例：将emp表的nickname字段修改为username，类型为varchar(30)

  `alter table emp change nickname username varchar(30) comment '昵称';`

- 删除字段：

  `alter table 表名 drop 字段名;`

- 修改表名：

  `alter table 表名 rename to 新表名`

- 删除表：

  `drop table [if exits] 表名;`

- 删除表，并重新创建该表：

  `truncate table 表名;`

#### DML

*操作语言，对数据进行增删改*

##### 添加数据

- 指定字段：

  `insert into 表名 (字段名1) values (值);`

- 全部字段：

  `insert into 表名 values (值1);`

- 批量添加数据：

  `insert into 表名 (字段名) values (值);`

  `insert into 表名 values (值1)`

##### 更新和删除数据

- 修改数据：

  `update 表名 set 字段名1 [ WHERE 条件 ];`

  例：

  `update emp set name = 'Jack' where id = 1;`

- 删除数据：

  `delete 表名 [ where 条件 ];`

#### DQL

查询语言，查询记录

语法：

```Mqsql
select 字段列表
from  表名字段
where 条件列表
group by 分组后的条件列表
order by 排序（asc||desc）
limit 分页参数
```

查询多个字段：

`select 字段一...from 表名；`

`select * from 表名`展示全部字段

去除重复记录：
`select distinct 字段列表 from 表名;`

##### 条件查询

语法：

`select 字段列表 from 表名 where 条件`

条件：

比较运算符 

举例不熟悉的：

 `between  . and .`在某个范围内

 `in（）`在in之后的列表中的值，多选一

link 占位符 模糊匹配   _  匹配一个字符，%匹配任意字符

`is null `  指空值

##### 聚合查询

```
count   统计数量
max     最大值
min     最小值
avg     平均值
sum     求和
```

如：

`select count（id） from employee workaddress='广东省'`

##### 分组查询

语法：

`select 字段列表 from 表名 where 条件 group by 分组字段名 having 分组后的过滤条件` 

where 和 having 的区别：

- 执行时机不同：where是分组之前进行过滤，不满足where条件不参与分组；having是分组后对结果进行过滤。
- 判断条件不同：where不能对聚合函数进行判断，而having可以。

另外

- 执行顺序：where > 聚合函数 > having
- 分组之后，查询的字段一般为聚合函数和分组字段，查询其他字段无任何意义

##### 排序查询

语法：
`select 字段列表 from 表名 order by 字段1 排序方式1, 字段2 排序方式2;`

排序方式：

- ASC: 升序
- DESC: 降序

如：

`select * from employee order by age asc`

##### 注意事项

如果是多字段排序，当第一个字段值相同时，才会根据第二个字段进行排序

##### 分页查询

语法：
`SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;`

例子：

```
-- 查询第一页数据，展示10条
 select * from employee limit 0，10（10，10）--第二页
```

注意事项

- 起始索引从0开始，起始索引 = （查询页码 - 1） * 每页显示记录数
- 分页查询是数据库的方言，不同数据库有不同实现，MySQL是LIMIT
- 如果查询的是第一页数据，起始索引可以省略，直接简写limit 10

##### DQL执行顺序

`from >where > group by> select> order by>limit`

#### DCL

控制语言，用来创建数据库用户、控制数据库的访问权限

#### 约束

分类：

```
非空约束 限制该字段的数据不能为null            not null   
唯一约束 保证该字段的所有数据都是不重复的        unique    
主键约束 主键是一行数据的唯一标识，要求非空且唯一 primary key
默认约束 如果未指定该字段的值，则采用默认值      default  
检查约束 保证字段值满足某一个条件              check    
外键约束 保证两张表数据的一致性和完整性         foreign key 
```

常用约束：

```
主键       primary key
自动增长   auto_incrementT 
不为空     not null     
唯一       unique
逻辑条件   check   
默认值     default
```

外键约束

```
create table 表名（
   字段名 类型 [constraint][外键名称] foreign key （外键字段名） references 主表（主表列名）；
   
alter table 表名 add constraint 外键名称 foreign key（外键字段名） references 主表（主表列名）
```

删除外键：

`alter table 表名 drop foreign key 外键名`

#### 查询

###### 合并查询

笛卡尔积，会展示所有组合结果：
`select * from employee, dept;`

消除无效笛卡尔积：
`select * from employee, dept where employee.dept = dept.id;`

###### 内连接查询

内连接查询的是两张表交集的部分

隐式内连接：
`select 字段列表 drom 表1, 表2 WHERE 条件 ...;`

显式内连接：
`select 字段列表 from 表1 [ inner ] join 表2 on 连接条件 ...;`

###### 外连接查询

左外连接：
查询左表所有数据，以及两张表交集部分数据
`select 字段列表 from 表1 left [ outer ] join 表2 on 条件 ...;`
相当于查询表1的所有数据，包含表1和表2交集部分数据

右外连接：
查询右表所有数据，以及两张表交集部分数据
`select 字段列表 from 表1 right [ outer ] join 表2 on 条件 ...;`

###### 自连接查询

当前表与自身的连接查询，自连接必须使用表别名

语法：
`select 字段列表 from 表A 别名A join 表A 别名B ON 条件 ...;`

自连接查询，可以是内连接查询，也可以是外连接查询

###### 联合查询

把多次查询的结果合并，形成一个新的查询集

语法：

```
select 字段列表 from 表A ...
union [all]
select 字段列表 from 表B ...
```

注意事项

- UNION ALL 会有重复结果，UNION 不会
- 联合查询比使用or效率高，不会使索引失效

###### 子查询

SQL语句中嵌套SELECT语句，称谓嵌套查询，又称子查询。

`select * from t1 where column1 = ( select column1 from t2);`
子查询外部的语句可以是insert/ update / delete / select 的任何一个

##### 视图

创建：

`create [or replace] view 视图名称[列名列表] as select语句 [with[cascaded`|local`]check option]`

查询：

`查看创建视图语句：show create view 视图名称；`

`查看试图数据：select * from 视图名称；`

修改：

`方式一：create [or replace] view 视图名称[列名列表] as select [with[cascaded`|local`]check option]`

`方式二：alter view 视图名称[列名列表] as select语句[with[cascaded`|local`]check option] `

删除

`drop view [if exits] 视图名称`