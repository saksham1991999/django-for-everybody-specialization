# One to Many

### 1. What is the primary value add of relational databases over flat files?

- [x] Ability to scan large amounts of data quickly
- [ ] Ability to execute Python code within the file
- [ ] Ability to execute JavaScript in the file
- [ ] Ability to quickly convert data to HTML
- [ ] Ability to store data in a format that can be sent across a network

### 2. Which of the following is NOT a good rule to follow when developing a database model?

- [ ] Never repeat string data in more than one table in a data model
- [ ] Use integers as primary keys
- [ ] Model each "object" in the application as one or more tables
- [x] Use a person's email address as their primary key

### 3. If our user interface (i.e., like iTunes) has repeated strings on one column of the UI, how should we model this properly in a database?

- [ ] Put the string in the first row where it occurs and then NULL in all of the other rows
- [ ] Put the string in the last row where it occurs and put the number of that row in the column of all of the rest of the rows where the string occurs
- [ ] Encode the entire row as JSON and store it in a TEXT column in the database
- [ ] Put the string in the first row where it occurs and then put that row number in the column of all of the rest of the rows where the string occurs
- [x] Make a table that maps the string in the column to numbers and then use those numbers in the column

### 4. Which of the following is the label we give a column that the "outside world" uses to look up a particular row?

- [ ] Primary key
- [x] Logical key
- [ ] Local key
- [ ] Remote key
- [ ] Foreign key

### 5. What is the label we give to a column that is an integer and is used to point to a row in a different table?

- [ ] Local key
- [ ] Remote key
- [ ] Logical key
- [ ] Primary key
- [x] Foreign key

### 6. What is a simple rule that captures much of the concepts of "database normalization"?

- [ ] Do not point to a primary key more than once
- [ ] Every SELECT statement must use a JOIN clause
- [x] Don't replicate string data in a column
- [ ] Don't use any non-standard SQL statements

### 7. What is the SQL keyword that reconnects rows containing foreign keys with the corresponding data in the table that the foreign keys point to?

- [ ] CONSTRAINT
- [x] JOIN
- [ ] COUNT
- [ ] APPEND
- [ ] CONNECT

### 8. If we are following the default convention in Django, which of the following column names would be used for a foreign key in table "abc" that is pointing to a primary key in table "xyz"?

- [ ] id
- [ ] abc_xyz_id
- [x] xyz_id
- [ ] abc_id

### 9. If we are following the default convention in Django, which of the following column names would be used for a primary key in table "xyz" that is pointed to from a foreign key in table "abc"?

- [x] id
- [ ] abc_id
- [ ] xyz_id
- [ ] abc_xyz_id

### 10. Which of the following model field types is used for a foreign key?

- [ ] OneToManyKey
- [ ] OneToManyField
- [x] ForeignKey
- [ ] RemoteKey

### 11. What does an "on_delete=models.CASCADE" clause imply in a Model field in Django?

- [x] When a row in the parent table is deleted, all the rows in a child table that point to that row via a foreign key are deleted.
- [ ] When rows in a child table are deleted, the primary key of the corresponding row in the parent table is set to NULL
- [ ] Whenever a row is deleted, it is moved into a table named "CASCADE".
- [ ] Whenever a row is deleted from the table, the other rows are scanned to insure that the logical key is unique and any duplicates are removed.

### 12. When you add an index to a field in a database table, how are performance and storage affected?

- [ ] Read performance is faster, insert performance is the same, and no extra storage is required
- [ ] Read performance is the faster, insert performance is faster, and extra storage is required
- [ ] Read performance is the same, insert performance is faster, and no extra storage is required
- [x] Read performance is faster, insert performance is slower, and extra storage is required
