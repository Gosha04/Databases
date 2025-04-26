/*
 Vaysman, Joshua
 CPSC 408-02
 L20 In-Class Assignment
 */

ALTER TABLE film -- 1
ADD CONSTRAINT uniqueTitle UNIQUE (title) ;

ALTER TABLE film -- 2
DROP CONSTRAINT uniqueTitle;

CREATE VIEW chosenFilms AS -- 3
    SELECT *
    FROM film
    WHERE SUBSTRING(TITLE, 1, 1) = 'A' AND release_year = 2006;

SELECT * FROM chosenFilms; -- 4

DELIMITER $$ -- 5
CREATE TRIGGER checkRating AFTER INSERT ON film
    FOR EACH ROW
    BEGIN
        IF NEW.rating = 'R' THEN
            INSERT INTO rating_log VALUES
            (USER(), CONCAT('User attempted to input an R-rated film: ', NEW.title, '!'));
        END IF;
END $$
DELIMITER ;

INSERT INTO film (title, rating, language_id) VALUES ('Random R-Rated Film', 'R', 1); -- 6A
-- 6B: root@local | User attempted to input an R-rated film: Random R-Rated Film!

DELIMITER $$ -- 7
CREATE PROCEDURE yearReleased (
    IN movieTitle VARCHAR(50),
    OUT releaseYear INT)
BEGIN
    SELECT release_year INTO releaseYear
    FROM film
    WHERE title = movieTitle;
END $$
DELIMITER ;

CALL yearReleased('Ace Goldfinger', @yearReleased); -- 8
SELECT @yearReleased;


