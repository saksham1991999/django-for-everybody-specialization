# Login and Authentication

### 1. Which came first?

- [ ] Session
- [x] Cookie
- [ ] Login

### 2. Which came second?

- [x] Session
- [ ] Cookie
- [ ] Login

### 3. Which best describes the Django functionality that puts up the login form?

- [ ] Model
- [ ] TemplateTag
- [x] Application
- [ ] Middleware

### 4. Which best describes the Django functionality that supports sessions?

- [ ] Application
- [ ] Model
- [ ] TemplateTag
- [x] Middleware

### 5. What happens when the user passes a login check?

- [ ] A new record is added to the auth_group table
- [ ] A cookie is set
- [ ] A new record is added to the auth_user table
- [x] Information is added to the session

### 6. What string is returned by in dj4e-samples?

`x = django.urls.reverse('login')`

- [ ] /login
- [x] /accounts/login
- [ ] /dj4e-samples/login
- [ ] nigo1

### 7. What is the purpose of the *next* parameter on a login or logout URL?

- [ ] It indicates which record to start with in a list that exceeds the length of the page
- [ ] It advances the iteration variable in a for loop
- [x] It tells the authentication system where to go after the action is complete
- [ ] It moves to the next item in a linked list

### 8. What is the value in a Django template to print out the current logged-in user's email address?

- [ ] user.info.address.email
- [ ] user.rmail
- [x] user.email
- [ ] user.address

### 9. In a Django template, what is stored in the request.path variable?

- [x] The URL of the currently executing request
- [ ] The actual table name of the model that is currently in use
- [ ] A string indicating the path to the 'parent' folder
- [ ] A list of breadcrumbs of recently visited URLs

### 10. What is the default name of the template that Django will load when presenting the user with a login screen?

- [ ] home/login.html
- [ ] auth/auth.html
- [x] registration/login.html
- [ ] autos/login.html

### 11. What variable do you check in a Django view to see if this request is from a logged-in user?

- [ ] request.user.auth
- [ ] request.authenticated
- [x] request.user.is_authenticated
- [ ] is_authenticated.view

### 12. What Django class does a class-based view need to extend to indicate that the view can only be accessed by logged-in users?

- [ ] MustLoginView
- [x] Login Required Mixin
- [ ] AutoRedirectView
- [ ] AutoLoginView
