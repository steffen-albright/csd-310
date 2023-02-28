import mysql.connector
from mysql.connector import errorcode

CREATE DATABASE whatabook;

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

USE whatabook; 


ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('12220 K Plaza, Omaha, NE 68137');


INSERT INTO book(book_name, author, details)
    VALUES('Don Quixote', 'Miguel de Cervantes', 'The best selling book of all time');

INSERT INTO book(book_name, author, details)
    VALUES('A Tale of Two Cities', 'Charles Dickens', 'The second best selling book of all time');

INSERT INTO book(book_name, author, details)
    VALUES('The Little Prince', 'Antoine de Saint-Exupery', "Over 142 million copies sold");

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Sorcercers Stone', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('And Then There Were None', 'Agatha Christie');

INSERT INTO book(book_name, author)
    VALUES('The Dream of Red Chamber', 'Cao Xueqin');

INSERT INTO book(book_name, author)
    VALUES('She: A History of Adventure', 'H. Rider Haggard');

INSERT INTO book(book_name, author)
    VALUES('The Da Vinci Code', 'Dan Brown');

INSERT INTO book(book_name, author)
    VALUES('Think and Grow Rich', 'Napolean Hill');



INSERT INTO user(first_name, last_name) 
    VALUES('Henry', 'Le');

INSERT INTO user(first_name, last_name)
    VALUES('Anthony', 'Geron');

INSERT INTO user(first_name, last_name)
    VALUES('Steffen', 'Albright');



INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Henry'), 
        (SELECT book_id FROM book WHERE book_name = 'Don Quixote')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Anthony'),
        (SELECT book_id FROM book WHERE book_name = 'A Tale of Two Cities')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Steffen'),
        (SELECT book_id FROM book WHERE book_name = 'Think and Grow Rich')
    );
