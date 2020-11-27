# Django Forms

### 1. Which of the following is NOT a benefit of using the Django forms capability?

- [x] Database portability
- [ ] You reduce the amount of HTML you need to generate
- [ ] You can add complex form validation rules to your application
- [ ] You can easily create attractively styled forms
- [ ] You can have a mapping layer between your models and templates

### 2. What happens when a Create form is submitted and Django forms detects a validation error?

- [ ] The form is re-displayed with the incorrect data
- [ ] The form is re-displayed with the error messages
- [ ] The record is deleted form the database
- [x] The form is re-displayed with the incorrect data and error messages
- [ ] A 403 (Not authorized) is sent back to the browser

### 3. You cannot use a Django form unless it is connected to a Django Model.

- [ ] True
- [x] False

### 4. How do you indicate that you want to display a form using the Crispy library in a template?

- [ ] form.as_crispy
- [ ] csrf_token
- [ ] form.as_table
- [x] form | crispy

### 5. What does the fields="_all_" statement do in the Meta section of a Django form class?

- [ ] Indicates that the owner field is not supposed to be shown to the user when the form is displayed
- [ ] Indicates that none of the model fields are to be saved
- [x] Indicates that all of the underlying model fields should be in the form

### 6. In what method in a view class would you expect to see "form.save()" to save data from an incoming form?

- [ ] dispatch()
- [x] post()
- [ ] get()
- [ ] get_queryset()

### 7. What is the purpose of the *next* parameter on a login or logout URL?

- [ ] render_to_template_with_check()
- [ ] load_try_except()
- [ ] contitional_render_404()
- [x] get_object_or_404()
