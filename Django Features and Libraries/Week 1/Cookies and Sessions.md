# Cookies and Sessions

### 1. What part of a Django application handles session management?

- [x] Middleware
- [ ] Views
- [ ] Models
- [ ] Templates

### 2. Where are cookies stored?

- [ ] In elasticache
- [x] In the browser
- [ ] In the database
- [ ] In the Python code

### 3. Which protocol determines how cookies are sent back and forth?

- [ ] CSS
- [ ] ORM
- [ ] HTML
- [x] HTTP
- [ ] SQL

### 4. Which of the following Python structures is most like cookie storage?

- [x] dictionary
- [ ] list
- [ ] Template
- [ ] set
- [ ] database connection

### 5. Any server can read any cookie from any other server.

- [ ] True
- [x] False

### 6. What kind of cookies are deleted when the browser is closed?

- [x] Session cookies
- [ ] Inverse cookies
- [ ] Encrypted cookies
- [ ] Bitcoin cookies

### 7. What is the method you call in a Django view to set a cookie?

- [ ] request.setCookie()
- [x] response.set_cookie()
- [ ] $_COOKIES[]
- [ ] response.cookie.set()

### 8. How many times do you need to set a cookie for it to persist across a number of incoming requests?

- [ ] On every response to a POST request
- [ ] On every reques
- [ ] tOn every non-anonymous request
- [x] Once

### 9. What is the typical approach to making a session identifier?

- [ ] Use the logged-in user's email address
- [ ] Start at 1 and add 1 for each new session (like a primary key)
- [ ] Compute an MDS hash of the user's email address
- [x] Choose a large random number

### 10. Where is session data typically stored in a Django application?

- [ ] In the browser
- [ ] In JavaScript variables
- [ ] On the end user's hard drive
- [x] In the server

### 11. How do you set a key of 'abc' to the value 'test' in the session in a Django application?

- [ ] request.session['abc', 'test'];
- [x] request.session['abc'] = 'test';
- [ ] request.session.get('abc', 'test');
- [ ] $_SESSION['abc'] = 'test';
