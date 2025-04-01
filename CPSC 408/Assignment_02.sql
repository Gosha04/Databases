/*
 Vaysman, Joshua
 CPSC 408-02
 Assignment 2
 */

CREATE table Patient( --1
    patientID INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    dob DATE,
    phone INTEGER
);

ALTER TABLE Patient --2
ADD address TEXT;

DROP TABLE Patient; --3

SELECT FirstName, LastName, Email --4
FROM employees;

SELECT EmployeeId --5
FROM employees WHERE HireDate BETWEEN '2004-01-01' AND '2004-12-31';

SELECT * --6
FROM employees WHERE Title LIKE '%Manager';

SELECT DISTINCT BillingCity --7
FROM invoices;

SELECT DISTINCT BillingCountry --8
FROM invoices WHERE Total > 10 AND InvoiceDate BETWEEN '2013-01-01' AND '2013-12-31';

SELECT customers.State --9
FROM customers EXCEPT SELECT employees.State FROM employees;

SELECT employees.Phone FROM employees --10
UNION SELECT customers.Phone FROM customers;

SELECT customers.FirstName FROM customers --11
UNION SELECT employees.FirstName FROM employees;