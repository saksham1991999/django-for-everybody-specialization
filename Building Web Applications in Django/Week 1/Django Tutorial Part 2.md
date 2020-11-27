# Django Tutorial Part 2

### 1. These questions come from the Django project tutorial materials.<br>What is the default database backend for Django projects when they are first set up?

- [x] sqlite3
- [ ] Oracle
- [ ] MySQL
- [ ] MongoDB
- [ ] PostgreSQL

### 2. What file contains the list of INSTALLED_APPS in a Django project?

- [ ] views.py
- [ ] apps.py
- [ ] manage.py
- [ ] urls.py
- [x] settings.py

### 3. What does the "python manage.py migrate" command do?

- [ ] Moves login sessions to the backing store
- [ ] Makes a backup copy of db.sqlite3
- [x] Builds/updates the database structure for the projecty
- [ ] Moves the application to a new server

### 4. What is the purpose of the models.py file?

- [ ] To apply a regular expression to the incoming path in the request object
- [ ] To make building views for your application simpler
- [x] To define the shape of the data objects to be stored in a database
- [ ] To connect your database to the Django administration interface

### 5. What does the "sqlmigrate" option accomplish in a Django application?

- [ ] It copies all of your SQL into a REST-based API
- [ ] It moves all of your non-SQL data into flat files
- [x] It lets you see the SQL that will run to effect a migration
- [ ] It builds/updates the database structure for the project

### 6. What does the `_str_` method in a Django model accomplish?

- [ ] It indicates how strict the storage model will be in terms of column length
- [x] It lets you specify how an instance of the model will be represented as a string
- [ ] It improves the strength of the binding between SQL and the model
- [ ] It determines how the model will respond to stress

### 7. What is the difference between the Django shell and a normal interactive Python shell?

- [ ] You can run Django commands in a Python shell
- [ ] The Django shell uses JavaScript instead of Python
- [ ] Only the Python shell can print values
- [x] The Django shell loads all of the objects before starting

### 8. What is the Django command to create a user/password for the admin user interface?

- [ ] MOVE CORRESPONDING INTO USER
- [x] createsuperuser
- [ ] INSERT INTO User;
- [ ] //SYSIN DD USER

### 9. What file in a Django application do you edit to make sure a model appears in the admin interface?

- [x] admin.py
- [ ] module.py
- [ ] sakaiger.py
- [ ] views.py
