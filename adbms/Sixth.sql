use companydb2;
CREATE TABLE EMPLOYEE (
    Emp_no INT PRIMARY KEY,
    E_name VARCHAR(50),
    E_address VARCHAR(100),
    E_ph_no VARCHAR(15),
    Dept_no INT,
    Dept_name VARCHAR(50),
    Job_id VARCHAR(10),
    Designation VARCHAR(50),
    Salary DECIMAL(10,2),
    Join_date DATE 
);

INSERT INTO EMPLOYEE (Emp_no, E_name, E_address, E_ph_no, Dept_no, Dept_name, Job_id, Designation, Salary, Join_date)
VALUES 
(101, 'SMITH', '123 Main St, Pune', '9876543210', 10, 'IT', 'J01', 'CLERK', 9500.00, '1980-01-19'),
(102, 'HARRY', '456 Elm St, Mumbai', '9876543211', 20, 'IT', 'J02', 'ANALYST', 12000.00, '1981-05-01'),
(103, 'SCOTT', '789 Oak St, Pune', '9876543212', 10, 'HR', 'J03', 'MANAGER', 25000.00, '1981-12-03'),
(104, 'HELEN', '321 Pine St, Bangalore', '9876543213', 30, 'Sales', 'J04', 'ANALYST', 15000.00, '1982-06-15'),
(105, 'ADAMS', '654 Maple St, Pune', '9876543214', 20, 'Finance', 'J05', 'PRESIDENT', 45000.00, '1981-11-17');

alter table Employee rename to emp;
select * from emp;
select emp_no, e_name, salary from emp where designation = "manager";
select * from emp where salary > 10000;
select * from emp where join_date > '1981-12-31' order by designation asc;
select e_name, year(curdate())-year(join_date) as exp, salary/30 dailysal from emp;
select * from emp where designation in('clerk','analyst') ;
select * from emp where join_date in('1981-05-01', '1981-12-03', '1981-12-17', '1980-01-19');
select * from emp where e_name like 's%';
select max(salary)as maxsalary from emp limit 1;
select sum(salary) as totsalary from emp;
select avg(salary) as avgsalary from emp where dept_name = 'it';
select distinct salary from emp;


