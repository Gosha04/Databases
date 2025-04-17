/*
 Vaysman, Joshua
 CPSC 408-02
 L17 In-Class Assignment
 */

USE sakila;

# 1
SELECT rental_duration , (
       SELECT AVG(rental_duration) FROM film
       ) AS avgRentalDuration
FROM film;

# 2
SELECT COUNT(*) AS categoriesW60Film
FROM (
    SELECT category_id, COUNT(film_id) AS totalFilms
    FROM film_category
    GROUP BY category_id
    HAVING totalFilms > 60
     ) AS temp;

# 3
SELECT AVG(p.amount) AS avgMexPayment
FROM payment AS p
WHERE p.customer_id IN (
    SELECT customer_id
    FROM customer AS cust
    WHERE cust.address_id IN (
        SELECT address_id
        FROM address AS ad
        WHERE ad.city_id IN (
        SELECT c.city_id
        FROM city AS c
        WHERE c.country_id IN (
            SELECT nat.country_id
            FROM country AS nat
            WHERE nat.country = 'Mexico'))));

# 4
SELECT AVG(p.amount) AS avgMexPayment
FROM payment AS p
INNER JOIN customer AS cust ON cust.customer_id = p.customer_id
INNER JOIN address AS ad ON ad.address_id = cust.address_id
INNER JOIN city AS c ON c.city_id = ad.city_id
INNER JOIN country AS nat ON nat.country_id = c.country_id
WHERE nat.country = 'Mexico';