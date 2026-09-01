#1
CREATE DATABASE friendships_schema;
USE friendships_schema;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);
CREATE TABLE friendships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    friend_id INT,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

#2
INSERT INTO users (first_name, last_name) 
VALUES 
    ('Amy', 'Giver'),
    ('Eli', 'Byers'),
    ('Big', 'Bird'),
    ('Kermit', 'The Frog'),
    ('Marky', 'Mark'),
    ('Cookie', 'Monster');

#3
INSERT INTO friendships (user_id, friend_id) VALUES (1, 2), (1, 4), (1, 6);

#4
INSERT INTO friendships (user_id, friend_id) VALUES (2, 1), (2, 3), (2, 5);

#5
INSERT INTO friendships (user_id, friend_id) VALUES (3, 2), (3, 5);

#6
INSERT INTO friendships (user_id, friend_id) VALUES (4, 3);

#7
INSERT INTO friendships (user_id, friend_id) VALUES (5, 1), (5, 6);

#8
INSERT INTO friendships (user_id, friend_id) VALUES (6, 2), (6, 3);

#9
SELECT 
    users.first_name, 
    users.last_name, 
    user2.first_name AS friend_first_name, 
    user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id;

#10
SELECT 
    user2.first_name AS friend_first_name, 
    user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 1;

#11
SELECT COUNT(*) AS total_friendships 
FROM friendships;

#12
SELECT 
    users.first_name, 
    users.last_name, 
    COUNT(friendships.friend_id) AS total_friends
FROM users
JOIN friendships ON users.id = friendships.user_id
GROUP BY users.id
ORDER BY total_friends DESC
limit 1;


#13
SELECT 
    user2.first_name AS friend_first_name, 
    user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 3
ORDER BY friend_first_name ASC;