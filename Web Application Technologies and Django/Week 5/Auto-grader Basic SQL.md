`CREATE TABLE Ages ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  name VARCHAR(128), 
  age INTEGER
);`
<br>
<br>
<br>
`DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Rebekkah', 18);
INSERT INTO Ages (name, age) VALUES ('Ailidh', 30);
INSERT INTO Ages (name, age) VALUES ('Jaya', 34);
INSERT INTO Ages (name, age) VALUES ('Katharine', 23);
INSERT INTO Ages (name, age) VALUES ('Kiera', 21);`

<br>
<br>
<br>
`SELECT hex(name || age) AS X FROM Ages ORDER BY X`;

<br>
<br>
<br>
41696C6964683330