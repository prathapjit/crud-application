CREATE DATABASE testdb;
USE testdb;
CREATE TABLE testtable (id int NOT NULL AUTO_INCREMENT, name varchar(255), age varchar(255), gender varchar(255), city varchar(255),PRIMARY KEY (id)) ;
INSERT INTO testtable (name, age, gender, city)
 VALUES 
	("Leanne Graham", "30", "Male", "Gwenborough"),
  ("Ervin Howell", "28", "Male", "Wisokyburgh"),
  ("Clementine Bauch","28", "Female", "New York"),
  (" Dennis Schulist","26", "Female", "Los Angeles"),
  ("Kurtis Weissnat","40", "Male", "Seattle"),
  ("Liam","52", "Male", "Nashville"),
  ("Olivia","32", "Female", "El Paso");
