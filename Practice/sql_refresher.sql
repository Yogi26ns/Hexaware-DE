#DDL Commands
Create database sql_practice;
use sql_practice;
create table department(deptno int auto_increment primary key,deptname varchar(100),managername varchar(100));
Create table empl(empno int auto_increment Primary key,empName varchar(100),deptname varchar(100),deptno int,foreign key (deptno) references department(deptno),role varchar(100));
desc department;
desc empl;
alter table empl drop column deptname;
alter table empl
add email varchar(100);
#DML Commands
INSERT INTO department (deptname, managername) VALUES
('HR', 'Ravi Kumar'),
('Finance', 'Priya Sharma'),
('IT', 'Ankit Mehta'),
('Marketing', 'Sneha Reddy');

INSERT INTO empl (empName, deptno, role) VALUES
('Ravi Kumar', 1, 'Manager'),      
('Priya Sharma', 2, 'Manager'),    
('Ankit Mehta', 3, 'Manager'),     
('Sneha Reddy', 4, 'Manager'),     
('Akhil Raj', 1, 'HR Executive'),
('Meera Das', 1, 'Recruiter'),
('Nikhil Dev', 2, 'Accountant'),
('Deepa Singh', 3, 'Software Engineer'),
('Harish K', 3, 'Data Engineer'),
('Radhika Iyer', 4, 'Marketing Executive');

set SQL_SAFE_UPDATES = 0;
update empl
set role = 'senior software engineer'
where empName = 'Deepa Singh';

delete from empl
where role = 'Marketing executive';

select * from empl;
select empName, role from empl;
select * from empl
where role = 'data engineer';
select * from empl
where role = 'software engineer' and deptno = 3;
select * from empl
where deptno = 1 OR deptno = 2;
select * from empl
where not role = 'Manager';
select * from empl
WHERE role IN ('Manager', 'Accountant');
select * from empl
where empName LIKE 'R%';  -- Names starting with R

select empName, role from empl
order by empName asc;

select distinct role from empl;

select * from empl
where email is null;

select * from empl
limit 5;

select deptno, COUNT(*) as emp_count
from empl
group by deptno
having count(*) > 2;

#Joins
select e.empName, e.role, d.deptname, d.managername
from empl e
inner join department d on e.deptno = d.deptno;

select e.empName, e.role, d.deptname, d.managername
from empl e
left join department d on e.deptno = d.deptno;

select e.empName, e.role, d.deptname, d.managername
from empl e
right join department d on e.deptno = d.deptno;

select e.empName, e.role, d.deptname, d.managername
from empl e
left join department d on e.deptno = d.deptno
union
select e.empName, e.role, d.deptname, d.managername
from empl e
right join department d on e.deptno = d.deptno;

#Sub Queries
-- Types of SubQueries
-- 1.Scalar
select empname
from empl
where salary = (select max(salary) from empl);
-- 2.Row
select *
from department
where (deptname, managername) = 
      (select deptname, managername from department where deptno = 2);
-- 3.Column
select empName
from empl
where deptno IN (
select deptno from department where managername = 'John');

-- 4.Table
-- always has an alias name when using table subquery
select avg_salary.deptno, avg_salary.avg_sal
from (
    select deptno, avg(salary) as avg_sal
    from empl
    group by deptno
) as avg_salary; 
-- correleated subquer
select empname
from empl e
where salary > (select avg(salary) from empl where deptno = e.deptno);

-- string functions
select lower(empname) from empl;
select upper(managername) from department;
select length(empname) from empl;
select concat(empname, ' - ', role) from empl;

-- date functions
select curdate();
select now();
select year(curdate());
select datediff(curdate(), '2022-01-01') as days_since;

-- join,aggregate and groupby in a query
select d.deptname, count(e.empno) as total_employees
from department d
join empl e on d.deptno = e.deptno
group by d.deptname
having count(e.empno) > 1;

