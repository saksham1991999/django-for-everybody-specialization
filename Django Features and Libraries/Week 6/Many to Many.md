Week 5 Quiz - Many to Many

1. A one-to-many relationship in a data model involved two database tables. How many tables are involved in representing a many-to-many relationship?

    - [x] 3
    
2. If you were looking at a link in a data model diagram, which of these would represent a many-to-many relationship?

    - [x] 0..* --- 1..*

3. In Django, what type of field is used to represent a many-to-many relationship?

    - [x] models.ManyToManyField

4. Which of the following is NOT a common name for the additional table needed to represent a many-to-many relationship between two tables?

    - [x] Lookup table

5. In models.py when you want to explicitly model a Junction table, what is the attribute in the two lined table models used to indicate which Junction table to use to connect the two tables?

    - [x] through

6. What kind of model fields will be found in every Junction table?

    - [x] models.ForeignKey

7. If you have a many-to-many relationship between books and authors and you are inserting a new author for a book, which of the following orders of operations will work?

    - [x] insert the book, insert the author, insert the connection

8. You should never have any fields other than keys in a Junction table.

    - [x] False
