Week 4 Quiz - Tutorial 4

1. What is stored in the variable request.POST?

    - [x] A dictionary-like object that lets you access submitted POST data

2. What does the django.urls.reverse() function do?

    - [x] It constructs the path to a view using the name of a path entry in urls.py

3. What happens if you access a detail view like results() in Django tutorial 4 and provide a key that does not exist on the URL?

    - [x] You get a 404

4. In the polls/templates/polls/detail.html file in Django tutorial 4, what happens if you leave out the csrf_token line in the form?

    - [x] The POST data will be blocked by the server

5. In the polls/templates/polls/detail.html file in Django tutorial 4, which bit of code tells the view that will receive the POST data which question to associate this vote with?

    - [x] url 'polls:vote' question.id

6. Which HTTP method is used when sending data to the server that will modify or update data?

    - [x] POST
    
7. What does the Django template filter "pluralize" do?

    - [x] It emits an 's' if the value is > 1
