# Write the query to select all the names in the database. 
# The columns should appear, even if there are no records in the database yet.
SELECT * 
FROM names;

# Insert your own name into the database!
INSERT INTO names (name, created_at, updated_at)
VALUES ("Katie", NOW(), NOW());

# Insert another name or, NINJA BONUS: insert more than one name in a single statement. 
INSERT INTO names (name, created_at, updated_at)
VALUES ("Baldvin", NOW(), NOW()); 

INSERT INTO names (name, created_at, updated_at)
VALUES ("Brynjar", NOW(), NOW()), ("Freyja", NOW(), NOW());

# Optional: Try creating, updating and deleting records using the statements you've learn about.
DELETE FROM names
WHERE id = 7;

UPDATE names
SET name = "Katharine"
WHERE ID = 17; 


