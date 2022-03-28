CREATE DATABASE private_school;  -- CREATE THE DATABASE
USE private_school;

-- CREATE THE TABLES

CREATE TABLE IF NOT EXISTS Students(
studentid int not null,
firstname varchar(45),
lastname varchar(45),
dateOfBirth date,
tuitionFees int,
primary key (studentid)

);
CREATE TABLE IF NOT EXISTS Courses(
courseid int not null,
title varchar(45),
stream varchar(45),
type varchar(45),
startDate date,
endDate date,
primary key(courseid)
);
CREATE TABLE IF NOT EXISTS Trainers(
trainerid int not null,
firstname varchar(45),
lastname varchar(45),
subject varchar(45),
primary key(trainerid)

);
CREATE TABLE IF NOT EXISTS Assignments(
assignmentid int not null,
title varchar(45),
description varchar(45),
subDateTime date,
oralMark int,
totalMark int,
primary key(assignmentid)
);
CREATE TABLE IF NOT EXISTS Trainers_per_course(
tpcid int not null,
trainerid int,
courseid int,
primary key(tpcid),
foreign key(trainerid) references Trainers(trainerid),
foreign key(courseid) references Courses(courseid)

);
CREATE TABLE IF NOT EXISTS Students_per_course(
spcid int not null,
studentid int,
courseid int,
primary key(spcid),
foreign key(studentid) references Students(studentid),
foreign key (courseid) references Courses(courseid)
);
CREATE TABLE IF NOT EXISTS Assignments_per_course(
apcid int not null,
assignmentid int,
courseid int,
primary key(apcid),
foreign key(assignmentid) references Assignments(assignmentid),
foreign key(courseid) references Courses(courseid)
);
CREATE TABLE IF NOT EXISTS Assignments_per_student_per_course(
apspcid int not null,
assignmentid int,
studentid int,
courseid int,
primary key(apspcid),
foreign key(assignmentid) references Assignments(assignmentid),
foreign key(studentid) references Students(studentid),
foreign key(courseid) references Courses(courseid)
);

                        -- INSERT DATA INSIDE THE TABLES

-- INSERT DATA IN STUDENTS TABLE
INSERT INTO Students VALUES (1,'Miltos','Papagergiou','1991-09-12',2000);
INSERT INTO Students VALUES (2,'Maria','Papadopoulou','1996-03-20',2000);
INSERT INTO Students VALUES (3,'Nikos','Nikolaidis','1998-06-10',2000);
INSERT INTO Students VALUES (4,'Alexia','Dimitriou','1987-11-23',2000);
INSERT INTO Students VALUES (5,'Giorgos','Nikou','1994-07-03',2000);

-- INSERT DATA IN COURSES TABLE

INSERT INTO Courses VALUES (1,'BC8','Python','Part Time','2020-02-08','2020-08-10');
INSERT INTO Courses VALUES (2,'BC8','Java','Full Time','2020-02-14','2020-05-14');
INSERT INTO Courses VALUES (3,'BC9','Javascript','Part Time','2020-03-10','2020-09-11');
INSERT INTO Courses VALUES (4,'BC9','C#','Full Time','2020-04-05','2020-07-07');
INSERT INTO Courses VALUES (5,'BC8','C++','Part Time','2020-05-12','2020-11-06');

-- INSERT DATA IN TRAINERS TABLE
INSERT INTO Trainers VALUES (1,'Marios','Antoniou','Python');
INSERT INTO Trainers VALUES (2,'Georgia','Patouli','Java');
INSERT INTO Trainers VALUES (3,'Dimitris','Papaioanou','Javascript');
INSERT INTO Trainers VALUES (4,'Nikos','Mitsotakis','C#');
INSERT INTO Trainers VALUES (5,'Pinelopi','Tsaka','C++');

-- INSERT DATA IN ASSIGNMENTS TABLE

INSERT INTO Assignments VALUES (1,'Assignment_1','Assignment_1','2020-03-15',90,95);
INSERT INTO Assignments VALUES (2,'Assignment_2','Assignment_2','2020-04-23',95,85);
INSERT INTO Assignments VALUES (3,'Assignment_3','Assignment_3','2020-05-07',90,95);
INSERT INTO Assignments VALUES (4,'Assignment_4','Assignment_4','2020-06-05',85,97);
INSERT INTO Assignments VALUES (5,'Assignment_5','Assignment_5','2020-08-15',90,95);

-- INSERT DATA IN TRAINERS PER COURSE TABLE

INSERT INTO Trainers_per_course VALUES (1,1,1);
INSERT INTO Trainers_per_course VALUES (2,2,2);
INSERT INTO Trainers_per_course VALUES (3,3,3);
INSERT INTO Trainers_per_course VALUES (4,4,4);
INSERT INTO Trainers_per_course VALUES (5,5,5);

-- INSERT DATA IN STUDENTS PER COURSE TABLE

INSERT INTO Students_per_course VALUES (1,1,1);
INSERT INTO Students_per_course VALUES (2,2,2);
INSERT INTO Students_per_course VALUES (3,3,3);
INSERT INTO Students_per_course VALUES (4,4,4);
INSERT INTO Students_per_course VALUES (5,4,2);

-- INSERT DATA ASSIGNMENTS PER COURSE TABLE

INSERT INTO Assignments_per_course VALUES (1,1,1);
INSERT INTO Assignments_per_course VALUES (2,1,2);
INSERT INTO Assignments_per_course VALUES (3,3,1);
INSERT INTO Assignments_per_course VALUES (4,4,4);
INSERT INTO Assignments_per_course VALUES (5,5,5);

-- INSERT DATA IN ASSIGNMENTS PER STUDENT PER COURSE TABLE

INSERT INTO Assignments_per_student_per_course VALUES (1,1,1,1);
INSERT INTO Assignments_per_student_per_course VALUES (2,2,2,2);
INSERT INTO Assignments_per_student_per_course VALUES (3,3,3,3);
INSERT INTO Assignments_per_student_per_course VALUES (4,4,3,4);
INSERT INTO Assignments_per_student_per_course VALUES (5,5,1,1);












--  CREATE THE QUERYS

-- SELECT ALL STUDENTS
SELECT * FROM Students;

-- SELECT ALL COURSES
SELECT * FROM Courses;

-- SELECT ALL ASSIGNMENTS
SELECT * FROM Assignments;

-- SELECT ALL TRAINERS
SELECT * FROM Trainers;


-- Students per course query
SELECT s.studentid,courseid,s.firstname,s.lastname,s.dateOfBirth,s.tuitionFees
FROM Students as s
INNER JOIN Students_per_course on s.studentid=Students_per_course.courseid;


-- Trainers per course query 
SELECT t.trainerid,courseid ,t.firstname,t.lastname,t.subject
FROM Trainers as t 
INNER JOIN Trainers_per_course on t.trainerid=Trainers_per_course.courseid;


-- Assignments per course query
SELECT a.assignmentid,courseid,a.title,a.description,a.subDateTime,a.oralMark,a.totalMark
FROM Assignments as a 
INNER JOIN Assignments_per_course on a.assignmentid=Assignments_per_course.courseid;


-- Assignment per student per course query
SELECT a.assignmentid,Assignments_per_student_per_course.studentid,Assignments_per_student_per_course.courseid,a.title,a.description,a.subDateTime,a.oralMark,a.totalMark
FROM Assignments as a
INNER JOIN  Assignments_per_student_per_course on Assignments_per_student_per_course.assignmentid=a.assignmentid 
INNER JOIN Students on students.studentid=Assignments_per_student_per_course.studentid
INNER JOIN Courses on courses.courseid=Assignments_per_student_per_course.courseid;

--  students that belong to more than one courses
SELECT s.studentid,s.firstname,s.lastname,s.dateOfBirth,s.tuitionFees,count(sc.studentid) FROM students as s
INNER JOIN students_per_course as sc on s.studentid=sc.studentid GROUP BY sc.studentid HAVING count(sc.studentid)>1;


