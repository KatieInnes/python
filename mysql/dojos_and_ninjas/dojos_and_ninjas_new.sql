# Query: Create 3 new dojos
#INSERT INTO dojos (name, created_at, updated_at)
#VALUES ("Tokyo", NOW(), NOW()), ("Vienna", NOW(), NOW()), ("Honolulu", NOW(), NOW());

# Query: Delete the 3 dojos you just created

#DELETE FROM dojos
#WHERE id < 4;

# Query: Create 3 more dojos

#INSERT INTO dojos (name, created_at, updated_at)
#VALUES ("Reykjavik", NOW(), NOW()), ("Istanbul", NOW(), NOW()), ("Adelaide", NOW(), NOW());

# Query: Create 3 ninjas that belong to the first dojo

#INSERT INTO ninjas (first_name, last_name, age, dojo_id)
#VALUES ("Kristjan", "Olafsson", 34, 4), ("Lilja", "Smaradottir", 28, 4), ("Laufey", "Hafsteinsdottir", 27, 4);


# Query: Create 3 ninjas that belong to the second dojo

#INSERT INTO ninjas (first_name, last_name, age, created_at, uploaded_at, dojo_id)
#VALUES ("Serhat", "Sen", 30, NOW(), NOW(), 5), ("Ziya", "Aydi", 23, NOW(), NOW(), 5), ("Bekir", "Soylu", 36, NOW(), NOW(), 5);


# Query: Create 3 ninjas that belong to the third dojo
#INSERT INTO ninjas (first_name, last_name, age, created_at, uploaded_at, dojo_id)
#VALUES ("Julia", "Pyne", 40, NOW(), NOW(), 6), ("Adam", "McLachlan", 25, NOW(), NOW(), 6), ("Hamish", "Ford", 19, NOW(), NOW(), 6);

# Query: Retrieve all the ninjas from the first dojo
#SELECT * 
#FROM ninjas
#WHERE dojo_id = 4;


# Query: Retrieve all the ninjas from the last dojo

#SELECT *
#FROM ninjas
#WHERE dojo_id = 6;

# Query: Retrieve the last ninja's dojo

SELECT name, ninjas.id
FROM dojos
JOIN ninjas
ON dojos.id = ninjas.dojo_id
ORDER BY ninjas.id
DESC LIMIT 1;