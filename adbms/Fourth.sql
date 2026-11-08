create database basicjoin;
use basicjoin;
create table emp(empid int primary key, ename varchar(50));
desc emp;

insert into emp values (101,"sahil");
insert into emp values (102,'vaibhax');
insert into emp values (103,"atharva");
insert into emp values (104,"kshipra");
insert into emp values (109,"rashmika");
insert into emp values (110,"alia");

create table project(proid int primary key, pname varchar(50),empid int ,
 foreign key(empid) references emp(empid));

insert into project values (5,"pro1",103);
insert into project values (6,'pro2',null);
insert into project values (7,"pro7");
insert into project values (4,"pro4",104);

select * from emp;
select * from project;

select * from emp join project on emp.empid=project.empid;

select e.ename, p.pname from project p inner join emp e on e.empid = p.empid;

select e.ename, p.pname from emp e left join project p on e.empid = p.empid;
select e.ename, p.pname from project p right join emp e on e.empid = p.empid;

insert into project(proid, pname) values (8,'proji');

select * from emp left join project on emp.empid = project.empid
UNION
select * from emp right join project on emp.empid = project.empid;


select emp.ename,project.pn ame from emp left join project on emp.empid=project.empid
where project.empid is not null;