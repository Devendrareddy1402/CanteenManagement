CREATE SCHEMA `CANTEEN`;
USE `CANTEEN`;
DROP TABLE IF EXISTS `Customers`;
CREATE TABLE Customers(
	Name varchar (100) NOT NULL,
	Gender char NOT NULL,
	ID int NOT NULL,
	EmailID varchar (100) NOT NULL,
	Role varchar (100) NOT NULL,
	Amount int NOT NULL);
ALTER TABLE Customers ADD PRIMARY KEY (ID);
DROP TABLE IF EXISTS `Stall`;
CREATE TABLE Stall(
	Stallname varchar (100) NOT NULL,
	ID int NOT NULL,
	Openingtime TIME NOT NULL,
	Closingtime TIME NOT NULL,
	Duration TIME NOT NULL);
ALTER TABLE Stall ADD PRIMARY KEY (ID);
DROP TABLE IF EXISTS `Dependents`;
CREATE TABLE Dependents(
	CustomerID int NOT NULL,
    Dependentname varchar (50) NOT NULL,
    DependentGender char NOT NULL);
DROP TABLE IF EXISTS `CustomerNumber`;
CREATE TABLE CustomerNumber(
	CustomerID int NOT NULL,
    CustomerName varchar (100) NOT NULL,
    PhoneNumber varchar(100) NOT NULL);
ALTER TABLE CustomerNumber ADD PRIMARY KEY (PhoneNumber);
DROP TABLE IF EXISTS `Breakfast`;
CREATE TABLE Breakfast(
	SID int NOT NULL,
	Item varchar(100) NOT NULL,
	Price int NOT NULL);
DROP TABLE IF EXISTS `Lunch`;
CREATE TABLE Lunch(
	SID int NOT NULL,
    Item varchar (100) NOT NULL,
    Price int NOT NULL);
DROP TABLE IF EXISTS `Dinner`;
CREATE TABLE Dinner(
	SID int NOT NULL,
    Item varchar(100) NOT NULL,
    Price int NOT NULL);
DROP TABLE IF EXISTS `ExpenditureCalculation`;
CREATE TABLE ExpenditureCalculation(
	StallID int NOT NULL,
	Edate DATE NOT NULL,
	BorderNumber varchar(100) NOT NULL,
	EmployeeID int NOT NULL);
DROP TABLE IF EXISTS `Bill`;
CREATE TABLE Bill(
	CustomerID int NOT NULL,
    Name varchar(100) NOT NULL,
    StallID int NOT NULL,
    Amount int NOT NULL,
    DateandTime TIMESTAMP NOT NULL,
    Ordernumber varchar(100) NOT NULL);
ALTER TABLE BILL ADD PRIMARY KEY (Ordernumber);
DROP TABLE IF EXISTS `StallMaintenance`;
CREATE TABLE StallMaintenance(
	StallID int NOT NULL,
    Sdate DATE NOT NULL,
    Income int NOT NULL,
    Expenditure int NOT NULL);
ALTER TABLE StallMaintenance ADD PRIMARY KEY (Sdate, StallID);
DROP TABLE IF EXISTS `Employee`;
CREATE TABLE Employee(
	Name varchar(100) NOT NULL,
    Gender char NOT NULL,
	ID int NOT NULL,
    StallID int NOT NULL,
    Role varchar (100) NOT NULL,
    Salary int NOT NULL,
    Workingdays int NOT NULL,
    ManagerID int NOT NULL);
ALTER TABLE Employee ADD PRIMARY KEY (ID);

ALTER TABLE Breakfast ADD FOREIGN KEY (SID) REFERENCES Stall(ID);
ALTER TABLE Lunch ADD FOREIGN KEY (SID) REFERENCES Stall(ID);
ALTER TABLE Dinner ADD FOREIGN KEY (SID) REFERENCES Stall(ID);

ALTER TABLE Dependents ADD FOREIGN KEY (CustomerID) REFERENCES Customers(ID);
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (Edate, StallID) REFERENCES StallMaintenance(Sdate, StallID);
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);

ALTER TABLE StallMaintenance ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);
ALTER TABLE Employee ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (BorderNUmber) REFERENCES Bill (OrderNumber);

ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (EmployeeID) REFERENCES Employee(ID);

ALTER TABLE Employee ADD FOREIGN KEY (ManagerID) REFERENCES Employee(ID);

LOCK TABLES `Customers` WRITE;
INSERT INTO Customers VALUES('AbhiRam', 'M', 88, 'u21ec088@eced.svnit.ac.in', 'Student',200);
INSERT INTO Customers VALUES('Melky', 'M', 76, 'u21ec076@eced.svnit.ac.in', 'Student', 190);
INSERT INTO Customers VALUES('Sekhar', 'M', 099,'u21ec099@eced.svnit.ac.in', 'Student', 180);

UNLOCK TABLES;

INSERT INTO Stall VALUES('Night Station', 1,'18:00:00','03:00:00' ,'09:00:00');
INSERT INTO Stall VALUES('Tantra Food', 2, '13:00:00', '23:00:00','10:00:00');
INSERT INTO Stall VALUES('Juice', 3, '14:00:00', '2:00:00','12:00:00');
INSERT INTO Stall VALUES('Yellow', 4, '08:00:00', '21:00:00', '13:00:00');

INSERT INTO Breakfast VALUES(4, 'Idly', 20);
INSERT INTO Breakfast VALUES(4, 'Dosa', 25);
INSERT INTO Breakfast VALUES(4, 'Upma', 20);

INSERT INTO Lunch VALUES(2, 'Veg Fried Rice', 50);
INSERT INTO Lunch VALUES(2, 'Egg Pulavu', 65);
INSERT INTO Lunch VALUES(2, 'Biryani', 80);


INSERT INTO Dinner VALUES(2, 'Punjabi Thali', 120);
INSERT INTO Dinner VALUES(3, 'Andhra Meals', 100);
INSERT INTO Dinner VALUES(3, 'Gujarati Thali', 150);


SELECT * FROM Customers;
SELECT * FROM CustomerNumber;
SELECT * FROM Bill;
SELECT * FROM Dependents;
SELECT * FROM Stall 










