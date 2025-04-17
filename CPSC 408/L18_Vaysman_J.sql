/*
 Vaysman, Joshua
 CPSC 408-02
 L18 In-Class Assignment
 */

#1
SELECT address.address_id
FROM address LEFT JOIN store ON store.address_id = address.address_id
WHERE address.district = 'California' AND store_id is NULL;

#2
SELECT film.title, COUNT(*) AS numStoresHave
FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id
GROUP BY film.title;

#3
SELECT film.title, CONCAT(actor.first_name, ' ', actor.last_name) AS actors
FROM film INNER JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id;

#4
SELECT film.film_id, actor.actor_id
FROM film LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
UNION -- Added Correction Here
SELECT NULL AS film_id, actor.actor_id
FROM actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
WHERE film_actor.film_id IS NULL;
