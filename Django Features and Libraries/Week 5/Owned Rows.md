# Owned Rows

### 1. Why do we insist on producing a delete confirmation screen?

- [x] Because a GET request should never modify data
- [ ] Because a POST request cannot modify data
- [ ] Because Django would not be able to delete the data
- [ ] To make sure that there are no JavaScript errors

### 2. Which of the following methods is called first in the Django generic list view?

- [ ] get()
- [ ] render_to_response()
- [ ] get_queryset()
- [x] setup()
- [ ] startup

### 3. Which method do we override in the Django generic list view to keep users from making changes to rows they don't own?

- [ ] setup()
- [ ] startup
- [ ] render_to_response()
- [x] get_queryset()
- [ ] get()

### 4. What does OwnerUpdateView do if a user tries to delete a record that does not belong to them?

- [x] It returns a 404 (not found error)
- [ ] It puts out an error message in the JavaScript console
- [ ] It redirects the user to www.djangoproject.org
- [ ] It stops and fails with an error log message

### 5. What template variable indicates the current logged-in user?

- [ ] article.owner
- [ ] myarts.owner
- [x] user
- [ ] tsugi.user
- [ ] request.user

### 6. What is the name of the model that Django uses to store User objects?

- [ ] DjangoUsers
- [ ] settings.USERS
- [ ] Users
- [x] settings.AUTH_USER_MODEL
- [ ] django.users

### 7. What is the database relationship between the Article model and User model?

- [ ] Zero-to-Zero
- [x] One-to-Many
- [ ] Many-to-Many
- [ ] One-to-One

### 8. In views.py in the myarts sample code, what is the purpose of the "fields" class-wide value?

- [ ] To make the listed fields un-editable
- [ ] To double-check that model fields are not missing
- [ ] To list the fields that will be autosaved
- [x] To limit the model fields displayed in the form

### 9. For a data model named Frog, what is the generic Edit View convention for the template used when editing a Frog object?

- [ ] frog_edit.html
- [x] frog_form.html
- [ ] frog_modify.html
- [ ] frog_update.html

### 10. In the OwnerCreateView class, what method is overridden to set the "owner" field to the current logged-in user?

- [x] form_valid()
- [ ] LoginRequiredMixin
- [ ] save(commit=False)
- [ ] add_owner()

### 11. In OwnerUpdateView, how do we make sure that the current logged-in user cannot retrieve any rows them?

- [ ] We retrieve all the objects and throw away the non-owned objects
- [ ] We call the method of the same name in the super class
- [x] We add a model tilter
- [ ] We intercept the SQL and add a WHERE clause

### 12. In OwnerUpdateView, which is the "super" or "parent" class?

- [ ] get_queryset()
- [ ] SuperUpdateView
- [ ] UpdateView::Super
- [x] UpdateView
- [ ] OwnerUpdateView

### 13. When a generic edit view is receiving POST data, which of the following steps is done first?

- [ ] pre_post()
- [ ] form_valid()
- [ ] first_post()
- [x] get_query_set()
- [ ] clean()