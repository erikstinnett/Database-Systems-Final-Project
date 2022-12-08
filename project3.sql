DROP TABLE Film;
DROP TABLE Employee;
DROP TABLE Awards;
DROP TABLE Reviews;
DROP TABLE Production_Company;
DROP TABLE Directors;
DROP TABLE Writers;
DROP TABLE Actors;


CREATE TABLE Film
(
Title			VARCHAR2(30),
Runtime		NUMBER(5,2),
Genre			VARCHAR2(12),
Release_Date	DATE,
User_Rating		NUMBER(3,2),
Metascore_rating	NUMBER(3,2),
Film_Award		VARCHAR2(15),
Produced_By		VARCHAR2(20),
CONSTRAINT		Film_Title_Release_Date_PK PRIMARY KEY(Title, Release_Date)
);

CREATE TABLE Employee
(
Fname			VARCHAR2(15),
Mname			VARCHAR2(15),
Lname			VARCHAR2(15),
Pay			NUMBER(8,2),
Age			NUMBER(2),
CONSTRAINT		Emp_Name_PK PRIMARY KEY(Fname, Lname)
);

CREATE TABLE Actors
(
Fname			VARCHAR2(15),
Mname			VARCHAR2(15),
Lname			VARCHAR2(15),
Acts_In		VARCHAR2(30),
Awards_Num	NUMBER(3),
CONSTRAINT		Actor_Name_FK FOREIGN KEY(Fname, Lname)
REFERENCES Employee(Fname, Lname)
);

CREATE TABLE Writers
(
Fname			VARCHAR2(15),
Lname			VARCHAR2(15),
Writes_For		VARCHAR2(30),
Writing_Award	VARCHAR2(15),
CONSTRAINT		Writer_Name_FK FOREIGN KEY(Fname, Lname)
REFERENCES Employee(Fname, Lname)
);

CREATE TABLE Directors
(
Fname			VARCHAR2(15),
Lname			VARCHAR2(15),
Directs		VARCHAR2(30),
Director_Award	VARCHAR2(15),
CONSTRAINT		Direcot_Name_FK FOREIGN KEY(Fname, Lname)
REFERENCES Employee(Fname, Lname)
);

CREATE TABLE Awards
(
Award_Name		VARCHAR2(15),
Category		VARCHAR2(12),
Award_Date		DATE,
CONSTRAINT		Award_Name_Category_PK PRIMARY KEY(Award_Name, Category)
);

CREATE TABLE Reviews
(
Journal		VARCHAR2(20),
Reviewer_Fname	VARCHAR2(15),
Reviewer_Lname	VARCHAR2(15),
Reviewer_Rating	NUMBER(3,2),
CONSTRAINT		Reviewer_name_PK PRIMARY KEY(Reviewer_Fname, Reviewer_Lname)
);

CREATE TABLE Production_Company
(
Company_Name	VARCHAR2(20),
City_Location	VARCHAR2(15),
State_Location	CHAR(2),
Country_Location	VARCHAR2(20),
CONSTRAINT		Comp_Name_PK PRIMARY KEY(Company_Name)
);