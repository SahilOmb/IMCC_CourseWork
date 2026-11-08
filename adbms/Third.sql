/* filtering data from the table*/
/* where, select DISTNICT, and, or, not, in , between,,like,limit,is null*/
create database organization;
use organization;
create table employee(empid int not null primary key,
first_name varchar(15),last_name varchar(15),
gender char, role varchar(15), dept varchar(15), Manager_id varchar(10));
desc employee;
insert into employee values(1,'john','allen','M','Team leader','Retail','M11');
insert into employee values(2,'kim','hen','f','Team leader','finance','M12');
insert into employee values(3,'aryan','patekar','M','Manager','Retail','M13');
insert into employee values(4,'Mahi','bhai','M','Manager','finace','M14');
insert into employee values(5,'jos','buttler','M','president','HR','M15');
insert into employee values(6,'mansi','patil','f','president','HR','M16');
select * from Employee;
/* select Distinct keyword*/
/* the distinct clause in the select statement is use to eliminate
duplicate rows from the result set that may be produced while querying data from a table.
when using the distinct clause to provide*/
select distinct dept from employee order by dept;
select distinct role from employee;
select distinct role from employee order by Role;
select * from employee where role='president' and dept='HR';
select * from employee where role='president' and dept='retail';
select * from employee where role='manager' and dept='finace';
select * from employee where role='Manager' and role='Team Leader';
select * from employee where role in ('ceo','manager');
select * from employee where role in('President','Manager');
select * from employee where role not in('President','Manager');
alter table employee add column Experience int;
update employee set Experience=8 where empid=1;
update employee set Experience=4 where empid=4;
update employee set Experience=6 where empid=3;
select * from Employee;
alter table Employee drop column expeinece;
select * from employee where Experience between 6 and 10;/* Between operator*/
select * from employee where experience=5 or experience=10;
select * from employee where last_name like 'A%';	
/*limit operator*/
select * from employee order by experience limit 5;
select * from employee where manager_id is null;
select * from employee where experience is null;
select * from employee where experience is not null;
/* aggregate functions */
/* count, sum, avg, min, max */
select count(empid) from employee where dept = 'finance';
select min(experience) from employee;
select max(experience) from employee;
select sum(experience) from employee;
select avg(experience) as emp_exr from employee;
select * from employee;
select dept, count(*) as employee_count from employee group by dept;
select role,count(*) as employee_count from employee group by role;
select gender, count(*) as employee_count from employee group by gender;
select dept, sum(experience) as total_experience from employee group by dept having total_experience >= 10 and total_experience <=20;
select role, sum(experience) as total_experience from employee group by role having total_experience >= 10 and total_experience <=20;
select dept, count(empid) from employee group by dept having count(empid) > 1 order by count(empid) desc;