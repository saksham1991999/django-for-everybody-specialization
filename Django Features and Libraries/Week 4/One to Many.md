Week 4 Quiz - One to Many

1. What is the primary value add of relational databases over flat files?

    - [x] Ability to scan large amounts of data quickly

2. Which of the following is NOT a good rule to follow when developing a database model?

    - [x] Use a person's email address as their primary key

3. If our user interface (i.e., like iTunes) has repeated strings on one column of the UI, how should we model this properly in a database?

    - [x] Make a table that maps the strings in the column to numbers and then use those numbers in the column

4. Which of the following is the label we give a column that the "outside world" uses to look up a particular row?

    - [x] Logical key

5. What is the label we give to a column that is an integer and is used to point to a row in a different table?

    - [x] Foreign key

6. What is a simple rule that captures much of the concepts of "database normalization"?

    - [x] Don't replicate string data in a column

7. What is the SQL keyword that reconnects rows containing foreign keys with the corresponding data in the table that the foreign keys point to?

    - [x] JOIN

8. If we are following the default convention in Django, which of the following column names would be used for a foreign key in table "abc" that is pointing to a primary key in table "xyz"?

    - [x] xyz_id

9. If we are following the default convention in Django, which of the following column names would be used for a primary key in table "xyz" that is pointed to from a foreign key in table "abc"?

    - [x] id

10. Which of the following model field types is used for a foreign key?

    - [x] ForeignKey

11. What does an "on_delete=models.CASCADE" clause imply in a Model field in Django?

    - [x] When a row in the parent table is deleted, all the rows in a child table that point to that row via a foreign key are deleted.

12. When you add an index to a field in a database table, how are performance and storage affected?

    - [x] Read performance is faster, insert performance is slower, and extra storage is required