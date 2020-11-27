# Tutorial 4

### 1. These questions come from the Django project tutorial materials.<br>What is stored in the variable request.POST?

- [ ] The name of the model to store an extra copy of the incoming data
- [x] A dictionary-like object that lets you access submitted POST data
- [ ] The code that runs after a view method is complete
- [ ] The next page to redirect the browser to after the processing is complete

### 2. What does the django.urls.reverse() function do?

- [ ] It reverses the order of the characters in a string
- [ ] It sends the POST data back to the browser if there is an error
- [x] It constructs the path to a view using the name of a path entry in urls.py
- [ ] It sends a 404 error if the record cannot be loaded

### 3. What happens if you access a detail view like results() in Django tutorial 4 and provide a key that does not exist on the URL?

- [ ] The record is automatically created but left empty
- [x] You get a 404
- [ ] You get a 200
- [ ] The server crashes and sends you a 500

### 4. In the polls/templates/polls/detail.html file in Django tutorial 4, what happens if you leave out the csrf_token line in the form?

- [x] The POST data will be blocked by the server
- [ ] The form will look strange in the user's browser
- [ ] The favicon will not show up properly in the title bar
- [ ] The server will not know which object to retrieve once the POST data is sent

### 5. In the polls/templates/polls/detail.html file in Django tutorial 4, which bit of code tells the view that will receive the POST data which question to associate this vote with?

- [ ] question.question_text
- [ ] forloop.counter
- [ ] choice.choice_text
- [x] url 'polls:vote' question.id

### 6. Which HTTP method is used when sending data to the server that will modify or update data?

- [ ] 200
- [x] POST
- [ ] 404
- [ ] GET

### 7. What does the Django template filter "pluralize" do?

- [x] It emits an 's' if the value is > 1
- [ ] It converts a word to the plural form depending on the user's selected language
- [ ] It splits a string using a specific delimiter character
- [ ] It returns a random item from the given list
