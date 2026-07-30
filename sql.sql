CREATE DATABASE dishaji;
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS dishaji;
CREATE DATABASE py2;
SHOW DATABASES;
USE dishaji;
CREATE TABLE student (
    id INT PRIMARY KEY,
    FullName VARCHAR(50) NOT NULL,
    Course VARCHAR(50) DEFAULT 'B.Tech',
    Email VARCHAR(70),
    Phone VARCHAR(12),
    Marks FLOAT CHECK (Marks >= 0)
);
DESC student;
INSERT INTO student (id, FullName,Email, Phone, Marks)
VALUES
(181,'Sambhav Jain','sambhav1@gmail.com', '9890082314', 95.6);
SELECT * FROM student;
INSERT INTO student
VALUES
(333, 'Prince Soni', 'B.Tech', 'prince@gmail.com', '9984908383', 60.3);
INSERT INTO student
VALUES
(103, 'Yashraj Deshpande', 'B.Sc.', 'rohan012@gmail.com', '9179606679', 80.3),
(105, 'Disha Malviya', 'btech', 'disham@gmail.com', '9425790331', 85.6);

alter table student
change Email Mail_id varchar(70);

alter table student 
modify gender char(7);
alter table student
drop gender;
alter table student
add unique key(phone);
truncate table student;
-- select queries
select*from student;
select FullName from student;
select id,FullName from student;


select*from student
where FullName Like "P%";
select FullName from student order by FullName
desc;
select count(*) from student group by course;
having course= "B.tech";

create table customer(
c_id varchar(10),
c_name varchar(50),
c_phone varchar(12),
address varchar(200)
);
 insert into customer values
 ("c101","Shruti","7518384867","Indore MP"),
 ("c102","Yashraj","9179606679","Shajapur MP"),
 ("c103","Disha","9425790331","Gorkhpur UP");
 
 insert into orders values
 (1,"cheese","c101"),(1,"nepali momo","c102"),CREATE DATABASE dishaji;
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS dishaji;
CREATE DATABASE py2;
SHOW DATABASES;
USE dishaji;
CREATE TABLE student (
    id INT PRIMARY KEY,
    FullName VARCHAR(50) NOT NULL,
    Course VARCHAR(50) DEFAULT 'B.Tech',
    Email VARCHAR(70),
    Phone VARCHAR(12),
    Marks FLOAT CHECK (Marks >= 0)
);
DESC student;
INSERT INTO student (id, FullName,Email, Phone, Marks)
VALUES
(181,'Sambhav Jain','sambhav1@gmail.com', '9890082314', 95.6);
SELECT * FROM student;
INSERT INTO student
VALUES
(333, 'Prince Soni', 'B.Tech', 'prince@gmail.com', '9984908383', 60.3);
INSERT INTO student
VALUES
(103, 'Yashraj Deshpande', 'B.Sc.', 'rohan012@gmail.com', '9179606679', 80.3),
(105, 'Disha Malviya', 'btech', 'disham@gmail.com', '9425790331', 85.6);

alter table student
change Email Mail_id varchar(70);

alter table student 
modify gender char(7);
alter table student
drop gender;
alter table student
add unique key(phone);
truncate table student;
-- select queries
select*from student;
select FullName from student;
select id,FullName from student;


select*from student
where FullName Like "P%";
select FullName from student order by FullName
desc;
select count(*) from student group by course;
having course= "B.tech";

create table orders(
i_id varchar(10),
p_name varchar(50),
c_id varchar(10)
);

create table customer(
c_id varchar(10),
c_name varchar(50),
c_phone varchar(12),
address varchar(200)
);
 insert into customer values
 ("c101","Shruti","7518384867","Indore MP"),
 ("c102","Yashraj","9179606679","Shajapur MP"),
 ("c103","Disha","9425790331","Gorkhpur MP");
 
 insert into orders values
 (1,"cheese","c101"),(2,"nepali momo","c102"),(3,"pav bhaji","c103"),(4,"idli","c102"),(5,"pizza","c101");

select*from orders;
select*from customer;

select i_id,p_name,c_name,c_phone,address
from orders
Left JOIN customer
on orders.c_id=customer.c_id
union 
select i_id,p_name,c_name,c_phone,address
from orders
right JOIN customer
on orders.c_id=customer.c_id; 
