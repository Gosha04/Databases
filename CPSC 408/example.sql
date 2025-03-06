SELECT 'Sierra';

SELECT *
FROM employees;

SELECT *
FROM albums;

SELECT Title AS albumTitle,
    ArtistId, 5 AS number
FROM albums;

SELECT DISTINCT Composer AS Artist
FROM tracks;

SELECT Total, Total/2
FROM invoices;

SELECT albums.Title, artists.Name
FROM albums CROSS JOIN artists;

SELECT albums.Title, artists.Name
FROM albums NATURAL JOIN artists;

SELECT albums.Title, artists.Name
FROM albums INNER JOIN artists ON albums.ArtistID = artists.ArtistID;

SELECT al.Title, ar.Name
FROM albums AS al INNER JOIN artists AS ar ON al.ArtistID = ar.ArtistID;

SELECT al.Title AS trackName, tracks.Name AS albumName
FROM albums AS al INNER JOIN tracks ON al.AlbumId = tracks.AlbumId;

SELECT *
FROM invoices WHERE BillingCountry = 'USA';

SELECT DISTINCT BillingCity
FROM invoices WHERE BillingCountry = 'Canada' AND Total > 10;

SELECT DISTINCT BillingCity
FROM invoices WHERE BillingCountry IN ('Canada', 'USA') AND Total > 10;

SELECT DISTINCT Address
FROM customers WHERE customers.Country IN ('Brazil', 'Germany', 'Norway') AND
                    CustomerId BETWEEN 2 AND 30;

/*
 Lesson 9
 */

 SELECT *
 FROM customers
 WHERE FirstName LIKe 'S%'
 OR FirstName Like 'H___';

SELECT CustomerId
FROM customers WHERE FirstName LIKE 'F%' AND LastName LIKE '%s';

SELECT Name
FROM tracks WHERE GenreId = '24' ORDER BY Milliseconds ASC LIMIT 10;

/*
 Lesson 10
 */

SELECT COUNT (*) AS OsloInvoices
FROM invoices
WHERE BillingCity = 'Oslo';

SELECT COUNT (BillingState) AS totalInvoices
FROM invoices;

SELECT COUNT(*) AS numRecords,
    ROUND(AVG(Total),2) as avgTotalInvoice
FROM invoices;

SELECT COUNT(*) AS numRecords,
    ROUND(AVG(Total),2) as avgTotalInvoice
FROM invoices WHERE BillingCountry IN ('USA', 'Canada');

SELECT BillingCity, COUNT(*) as numRecords
FROM invoices
GROUP BY BillingCity;

SELECT albums.ArtistId,artists.Name,
       COUNT(albums.AlbumID)
FROM artists
INNER JOIN albums ON artists.ArtistId = albums.ArtistId
GROUP BY artists.ArtistId;

SELECT SupportRepId, Country, COUNT(*) AS numCustomers
FROM customers
GROUP BY SupportRepId, Country;

SELECT BillingCity, COUNT(*) as numRecords
FROM invoices
GROUP BY BillingCity
HAVING numRecords > 10;