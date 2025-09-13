create database ayush;
use ayush;

# ASSESSMENT 1
drop table if exists worker;
create table worker(
worker_id int,
first_name varchar(50),
last_name varchar(40),
salary int,
joining_date date,
department varchar(50)
);
ALTER TABLE WORKER
MODIFY COLUMN JOINING_DATE DATETIME;
INSERT INTO Worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
(1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
(2, 'Niharika', 'Vema', 80000, '2014-06-11 09:00:00', 'Admin'),
(3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
(4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'),
(5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
(6, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
(7, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
(8, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');
SELECT*FROM WORKER;

select distinct * from worker;

/* 1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.*/
select * from worker
order by FIRST_NAME ASC, DEPARTMENT DESC;

/*2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish”
from the Worker table. */
select*from worker
where first_name in ("Vipul","satish");

/*3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and
contains six alphabets. */
select*from worker
where first_name like '_____h';

/*4. Write an SQL query to print details of the Workers whose SALARY lies between 1. */
SELECT * FROM worker
WHERE salary between 100000 and 300000;
/*5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. */
SELECT first_name, last_name, department,
COUNT(*) as duplicate_count
FROM worker
GROUP BY first_name,last_name, department
HAVING COUNT(*) >= 1;

/*6. Write an SQL query to show the top 6 records of a table. */
select*from worker
limit 6 ;

/*7. Write an SQL query to fetch the departments that have less than five people in them.*/
select department from worker
group by department
having department<5;

/*8. Write an SQL query to show all departments along with the number of people in there.*/
select department,
count(first_name) as people
from worker
group by department;

/*9. Write an SQL query to print the name of employees having the highest salary in each
department. */
select first_name as employee,
department,
salary
from worker w 
where salary=(
select max(salary)
from worker
where department= w.department)
order by salary desc;

# Question 2. Open schol database, then select student table and use fallowing SQL statements.alter.TYPE THE STATEMENT, PRESS ENTER AND NOT THE OUTPUT
use ayush;
drop table if exists student;
CREATE TABLE student (
    StdID INT PRIMARY KEY,
    StdName VARCHAR(100),
    Sex VARCHAR(10),
    Percentage INT,
    Class INT,
    Sec CHAR(1),
    Stream VARCHAR(20),
    DOB DATE
);
select*from student;
INSERT INTO student (StdID, StdName, Sex, Percentage, Class, Sec, Stream, DOB)
VALUES
(1001, 'Surekha Joshi', 'Female', 82, 12, 'A', 'Science', '1998-08-03'),
(1002, 'Maahi Agarawal', 'Female', 56, 11, 'C', 'Commerce', '2008-11-23'),
(1003, 'Sonam Verma', 'Male', 59, 11, 'C', 'Commerce', '2006-06-29'),
(1004, 'Rohit Kumar', 'Male', 63, 11, 'C', 'Commerce', '1997-11-05'),
(1005, 'Dipesh Pulkit', 'Male', 78, 11, 'B', 'Science', '2003-09-14'),
(1006, 'Jahanvi Puri', 'Female', 60, 11, 'B', 'Commerce', '2008-11-07'),
(1007, 'Suman Kumar', 'Male', 23, 12, 'F', 'Commerce', '1998-08-03'),
(1008, 'Sahil Saras', 'Male', 56, 11, 'C', 'Commerce', '2008-11-07'),
(1009, 'Akshra Agarawal', 'Female', 72, 12, 'B', 'Commerce', '1996-10-01'),
(1010, 'Stuti Mishra', 'Female', 39, 11, 'F', 'Science', '2008-11-23'),
(1011, 'Harsh Agarawal', 'Male', 42, 11, 'C', 'Science', '1998-08-03'),
(1012, 'Nikunj Agarawal', 'Male', 49, 12, 'C', 'Commerce', '1998-06-28'),
(1013, 'Akriti Saxena', 'Female', 89, 12, 'A', 'Science', '2008-11-23'),
(1014, 'Tani Rastogi', 'Female', 82, 12, 'A', 'Science', '2008-11-23');

/* 1 To display all the records form STUDENT table. SELECT * FROM student ; */
select * from student;

/* 2. To display any name and date of birth from the table STUDENT. SELECT StdName, DOB
FROM student ; */
select stdName,DOB 
from student;

/* 3. To display all students record where percentage is greater of equal to 80 FROM student table.
SELECT * FROM student WHERE percentage >= 80; */
select*from student
where percentage >= 80;

/*4. To display student name, stream and percentage where percentage of student is more than 80
SELECT StdName, Stream, Percentage WHERE percentage > 80; */
select stdName,stream,percentage
from student
where percentage>80;

/*5. To display all records of science students whose percentage is more than 75 form student table.
SELECT * FORM student WHERE stream = ‘Science’ AND percentage > 75; */
select*from student
where stream = 'science' and percentage >75;

