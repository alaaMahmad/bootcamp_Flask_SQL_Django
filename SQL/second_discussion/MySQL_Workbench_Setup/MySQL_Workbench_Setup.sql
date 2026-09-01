CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);


INSERT INTO users (user_name, email) 
VALUES 
    ('alaa', 'alaa@gmail.com'),
    ('ahmad', 'ahmad@gmail.com'),
    ('bara', 'bara@gmail.com'),
    ('maryan', 'maryan@gmail.com');

SELECT * FROM users;

UPDATE users 
SET email = 'alaa_2@gmail.com' 
WHERE id = 1;

DELETE FROM users 
WHERE id = 4;
