# Query: Create 3 new users

#INSERT INTO users (first_name, last_name, email, created_at, updated_at)
#VALUES ("Samin", "Nosrat", "samin@ciaosamin.com", NOW(), NOW()), ("Deb", "Perelman", "deb@smittenkitchen.com", NOW(), NOW()), ("Julia", "Turshen", "julia@juliaturshen.com", NOW(), NOW());

# Query: Retrieve all the users
#SELECT *
#FROM users; 

# Query: Retrieve the first user using their email address
SELECT first_name, last_name
FROM users
WHERE email = "samin@ciaosamin.com"; 

# Query: Retrieve the last user using their id

# Query: Change the user with id=3 so their last name is Pancakes

# Query: Delete the user with id=2 from the database

# Query: Get all the users, sorted by their first name

# BONUS Query: Get all the users, sorted by their first name in descending order

