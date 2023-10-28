CREATE DATABASE BookReviews;

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
  genre_id INT, 
  genre_name VARCHAR(50)
);