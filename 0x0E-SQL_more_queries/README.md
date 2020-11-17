# 0x0E. SQL - More queries

## Foundations - Higher-level programming ― Databases

by Guillaume, CTO at Holberton School

![holberton image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## Resources

### Read or watch:

[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)

[How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)

[MySQL constraints](http://zetcode.com/mysql/constraints/)

[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

[Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)

[SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)

[SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)

[SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)

[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)

[The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)

[MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)

[SQL Style Guide](https://www.sqlstyle.guide/)

[MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)

### Extra resources around relational database model design:

[Design](https://www.guru99.com/database-design.html)

[Normalization](https://www.guru99.com/database-normalization.html)

[ER Modeling](https://www.guru99.com/er-modeling.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What’s a PRIMARY KEY
    What’s a FOREIGN KEY
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What are subqueries
    What are JOIN and UNION

## Requirements
### General

    Allowed editors: vi, vim, emacs
    All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

## More Info
### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
![Holberton image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201117T183646Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b418b8ad3a3f2e807518b06aac5733b6603a32b3d587ec6c1214ab62eea5d69)
