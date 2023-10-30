-- Init database
CREATE DATABASE BookReviews;

-- Create tables
CREATE TABLE reviews(
  book_id SERIAL PRIMARY KEY,
  book_name VARCHAR(255) NOT NULL,
  book_author VARCHAR(255) NOT NULL,
  book_review VARCHAR(2000) NOT NULL
);

CREATE TABLE genres(
  genre_id SERIAL PRIMARY KEY,
  genre_name VARCHAR(50)
);

CREATE TABLE bookgenres(
  bg_id SERIAL PRIMARY KEY,
  book_id INT,
  genre_name VARCHAR(50)
);

-- Create genres
INSERT INTO genres (genre_name) VALUES ('Fiction');
INSERT INTO genres (genre_name) VALUES ('Non-Fiction');
INSERT INTO genres (genre_name) VALUES ('Science');
INSERT INTO genres (genre_name) VALUES ('Romance');
INSERT INTO genres (genre_name) VALUES ('Comedy');
INSERT INTO genres (genre_name) VALUES ('Thriller');
INSERT INTO genres (genre_name) VALUES ('Fantasy');
INSERT INTO genres (genre_name) VALUES ('Motivational');
INSERT INTO genres (genre_name) VALUES ('History');
INSERT INTO genres (genre_name) VALUES ('Biography');
INSERT INTO genres (genre_name) VALUES ('Auto-Biography');
INSERT INTO genres (genre_name) VALUES ('Poetry');
INSERT INTO genres (genre_name) VALUES ('Dystopia');
INSERT INTO genres (genre_name) VALUES ('Mystery');
INSERT INTO genres (genre_name) VALUES ('Crime');
INSERT INTO genres (genre_name) VALUES ('Drama');
INSERT INTO genres (genre_name) VALUES ('Novel');