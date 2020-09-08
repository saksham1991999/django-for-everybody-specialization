Week 5 Quiz - Owned Rows

1. Why do we insist on producing a delete confirmation screen?

    - [x] Because a GET request should never modify data

2. Which of the following methods is called first in the Django generic list view?

    - [x] setup()

3. Which method do we override in the Django generic list view to keep users from making changes to rows they don't own?

    - [x] get_queryset()

4. What does OwnerUpdateView do if a user tries to delete a record that does not belong to them?

    - [x] It returns a 404 (not found error)

5. What template variable indicates the current logged-in user?

    - [x] user

6. What is the name of the model that Django uses to store User objects?

    - [x] settings.AUTH_USER_MODEL

7. What is the database relationship between the Article model and User model?

    - [x] One-to-Many

8. In views.py in the myarts sample code, what is the purpose of the "fields" class-wide value?

    - [x] To limit the model fields displayed in the form

9. For a data model named Frog, what is the generic Edit View convention for the template used when editing a Frog object?

    - [x] frog_form.html

10. In the OwnerCreateView class, what method is overridden to set the "owner" field to the current logged-in user?

    - [x] form_valid()

11. In OwnerUpdateView, how do we make sure that the current logged-in user cannot retrieve any rows that don't belong to them?

    - [x] We add a model filter

12. In OwnerUpdateView, which is the "super" or "parent" class?

    - [x] UpdateView

12. When a generic edit view is receiving POST data, which of the following steps is done first?

    - [x] clean()
