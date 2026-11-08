CREATE DATABASE FinanceDB;

-- Select/use the database before creating tables
USE FinanceDB;

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    City VARCHAR(50),
    bdate DATE
);

CREATE TABLE Investor (
    inv_no INT PRIMARY KEY,
    inv_name VARCHAR(50),
    inv_date DATE,
    inv_amt DECIMAL(12,2),
    emp_id INT
);
-- Inserting 5 rows into Employee
INSERT INTO Employee (emp_id, emp_name, City, bdate) VALUES
(1, 'Amit Sharma', 'Pune', '1985-04-12'),
(2, 'Rahul Verma', 'Mumbai', '1990-08-23'),
(3, 'Sneha Patil', 'Pune', '1992-11-05'),
(4, 'John Doe', 'Delhi', '1988-01-30'),
(5, 'Pooja Joshi', 'Bangalore', '1995-07-19');

-- Inserting 5 rows into Investor
INSERT INTO Investor (inv_no, inv_name, inv_date, inv_amt, emp_id) VALUES
(101, 'Karan Malhotra', '2023-01-15', 50000.00, 1),
(102, 'Riya Sen', '2023-03-22', 120000.00, 2),
(103, 'Vijay Mallya', '2022-11-11', 75000.00, 1),
(104, 'Ananya Birla', '2024-05-09', 200000.00, 4),
(105, 'Sameer Khan', '2023-08-18', 35000.00, 5);

alter table investor rename to inv;
select * from employee;
alter table emp add column age int ,add column salary int ;
alter table emp add constraint ck_age check(age>18) ,add constraint ck_salary check(salary>10000) ;
alter table inv add column age int;
alter table inv modify inv_name text;
alter table emp rename column emp_id to eid;
update emp set city = 'nagpur' where eid= 4;