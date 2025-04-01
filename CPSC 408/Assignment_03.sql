/*
 Vaysman, Joshua
 CPSC 408-02
 Assignment 3
 */

 /*
  Set 1
  */

SELECT Composer, AVG(Milliseconds) AS avgTime --1
FROM tracks
GROUP BY Composer;

SELECT COUNT(*) AS numCustomers --2
FROM customers;

SELECT GenreId, MediaTypeId, COUNT(*) AS numRecords, --3
       MAX(UnitPrice) AS maxCost
FROM tracks
GROUP BY GenreId, MediaTypeId
ORDER BY GenreId;

SELECT genres.Name as genreName, AVG(tracks.Milliseconds) AS avgTime --4
FROM tracks, genres
GROUP BY tracks.GenreId, genreName;

SELECT artists.Name AS artistName, COUNT(*) AS numAlbums --5
FROM albums, artists
GROUP BY albums.ArtistId, artists.Name;

SELECT BillingCity, COUNT(*) AS numInvoices --6
FROM invoices
WHERE BillingCountry = 'USA'
GROUP BY BillingCity;

/*
 Set 2
 */



SELECT Composer, AVG(Milliseconds) as avgTrackLength --1
FROM tracks
WHERE Milliseconds < 375000
GROUP BY Composer;

SELECT Composer, AVG(Milliseconds) as avgTrackLength --2
FROM tracks
GROUP BY Composer
HAVING avgTrackLength < 375000;

SELECT BillingCountry, COUNT(*) AS totalInvoices --3
FROM invoices
GROUP BY BillingCountry
HAVING totalInvoices < 10;

SELECT BillingCountry --4
FROM invoices
GROUP BY BillingCountry
HAVING COUNT(DISTINCT BillingCity) = 8;

SELECT BillingCountry, SUM(Total) AS sumTotals --5
FROM invoices
WHERE InvoiceDate BETWEEN '2010-01-01' AND '2010-12-31'
GROUP BY BillingCountry
HAVING COUNT(*) > 5;

/*
 Set 3
 https://docs.google.com/document/d/1B5CJlNJK79aRgcKk5qXfry7lemZLB8eTWgie7Bh5A0Q/edit?usp=sharing
 */




