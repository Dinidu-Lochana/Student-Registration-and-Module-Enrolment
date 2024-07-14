create database FfOE_23;

use FOE_23;

create table DEPARTMENT(
	Dept_ID varchar(30) NOT NULL,
    Dept_Head varchar(200) not NULL,
    Primary key (Dept_ID)
);

create table EMPLOYEE(
	Employee_ID varchar(30) not null,
    Dept_ID varchar(30),
    Area varchar(50),
    Designation varchar(75),
    
    primary key(Employee_ID)
);

insert into DEPARTMENT(Dept_ID,Dept_Head)
values('EIE','Menuka');



insert into department values('CEE','Shantha');
insert into department values('MME','Sanath');

insert into employee values('EE001','Amal','Galle','Lecturer');
insert into employee values('CEE001','Bimal','Galle','Lecturer');

insert into employee values('MME001','Kamal','Galle','Lecturer');
insert into employee values('CEE002','Kana','Galle','Student');


Alter table EMPLOYEE add constraint Fk_DeptID foreign key(Dept_ID) references DEPARTMENT(Dept_ID)
on delete set null on update cascade;
data
update department
set Dept_ID = 'DEIE' where Dept_Head='Menuka';



