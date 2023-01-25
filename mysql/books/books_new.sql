-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ("Jane", "Amsden", NOW(), NOW()), ("Emily", "Dixon", NOW(), NOW()), ("Theodore", "Dostoevsky", NOW(), NOW()), ("William", "Shapiro", NOW(), NOW()), ("Lao", "Xiu", NOW(), NOW());

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
-- INSERT INTO books (title, num_of_pages, created_at, updated_at)
-- VALUES ("C Sharp", 125, NOW(), NOW()), ("Java", 244, NOW(), NOW()), ("Python", 397, NOW(), NOW()), ("PHP", 89, NOW(), NOW()), ("Ruby", 301, NOW(), NOW());

-- Query: Change the name of the C Sharp book to C#

-- UPDATE books
-- SET title = "C#"
-- WHERE id = 1;

-- Query: Change the first name of the 4th user to Bill

-- UPDATE users
-- SET first_name = "Bill"
-- WHERE id = 4;

-- Query: Have the first user favorite the first 2 books
INSERT INTO favorites (user_id, book_id)
VALUES (1, 1), (1, 2);


SELECT *
FROM favorites;

-- Query: Have the second user favorite the first 3 books

-- Query: Have the third user favorite the first 4 books

-- Query: Have the fourth user favorite all the books

-- Query: Retrieve all the users who favorited the 3rd book

-- Query: Have the 5th user favorite the 2nd book

-- Find all the books that the 3rd user favorited

-- Query: Find all the users that favorited to the 5th book