create database companydb2;
use companydb2;
create table emp(empid int primary key, ename varchar(50),salary int, joindate date);
create table departments(deptid int primary key, dname varchar(50));

alter table emp add column age int;
alter table departments add column dept_loc varchar(50);
alter table emp add column phone int not null;
alter table emp modify column email varchar(100);
alter table departments drop primary key;
alter table departments modify deptid int primary key;
alter table emp add deptid int;
alter table emp add constraint fk_dept foreign key(deptid) references departments(deptid);
alter table emp rename column ename to empname;
alter table emp add constraint ck_salary check(salary>12000);
alter table emp add constraint ck_age check(age>18);
alter table emp drop column phone;
alter table emp drop  constraint ck_salary;
alter table emp rename to empdetails;