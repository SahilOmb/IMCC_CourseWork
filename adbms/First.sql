create database tcl;
use tcl;
create table orders(order_id int primary key, cust_name varchar(100), status varchar(50));

desc orders;
set autocommit=0;
begin;
insert into orders values (101,"Mahess","pending");
insert into orders values (102,"Vedant","pending");

select * from orders;
rollback;
commit;

update orders set cust_name="Vedang" where order_id=102;

-- for commit
insert into orders values (103,"Atharva","pending");
insert into orders values (104,"prathamesh","pending");
select * from orders;
savepoint sp1;
update orders set status = 'shipped' where order_id=103;
savepoint sp2;
rollback to savepoint sp1;
delete from orders where order_id=102;
savepoint sp3;
rollback;
commit;
