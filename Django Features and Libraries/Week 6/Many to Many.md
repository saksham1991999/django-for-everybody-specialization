# Many to Many

### 1. A one-to-many relationship in a data model involved two database tables. How many tables are involved in a representing many-to-many relationship?

- [ ] 2
- [ ] 4
- [x] 3
- [ ] 5
- [ ] 1

### 2. If you were looking at a link in a data model diagram, which of these would represent a many-to-many relationship?

- [ ] 1 -- 0..*
- [x] 0..* --- 1..*
- [ ] 0 -- 0
- [ ] 2 -- 2

### 3. In Django, what type of field is used to represent a many-to-many relationship?

- [ ] models.ManyToManyRelationship
- [ ] models.lntField
- [ ] models.ForeignKey
- [x] models.ManyToManyField
- [ ] models.ThroughKey

### 4. Which of the following is NOT a common name for the additional table needed to represent a many-to-many relationship between two tables?

- [ ] Bridge Table
- [ ] Through Table
- [ ] Association Table
- [ ] Join Table
- [x] Lookup table
- [ ] Junction Table

### 5. In models.py when you want to explicitly model a Junction table, what is the attribute in the two lined table models used to indicate which Junction table to use to connect the two tables?

- [x] through
- [ ] join_through
- [ ] junction
- [ ] on_delete
- [ ] Join

### 6. What kind of model fields will be found in every Junction table?

- [ ] models.CharField
- [ ] models.JunctionFields
- [ ] models.OutboundKeys
- [ ] models.ManyToManyField
- [x] models.ForeignKey

### 7. If you have a many-to-many relationship between books and authors and you are inserting a new author for a book, which of the following orders of operations will work?

- [ ] insert the connection, insert the author, insert the book
- [x] insert the book, insert the author, insert the connection
- [ ] insert the connection, insert the book, insert the author
- [ ] insert the book, insert the connection, insert the author

### 8. You should never have any fields other than keys in a Junction table.

- [ ] True
- [x] False
