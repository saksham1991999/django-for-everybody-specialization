# JavaScript

### 1. Where does the following JavaScript code execute?

```JavaScript
<p>One Paragraph</p>

<script type="text/javascript">
document.write("<p>Hello World</p>")
</script>

<p>Second Paragraph</p>
```

- [x] In the browser
- [ ] In the web server
- [ ] In the database server
- [ ] On the network

### 2. What happens when JavaScript runs the alert() function?

- [ ] A message is sent back to the Django code to be logged on the server
- [ ] JavaScript pops up a dialog box and execution continues until the `</alert>` tag is encountered
- [ ] JavaScript checks to see if there are any unprocessed events
- [x] JavaScript execution is paused and a dialog box pops up

### 3. Which of the following is NOT a way to include JavaScript in an HTML document?

- [x] By including the code the `<?javascript and ?>` tags
- [ ] On a tag using an attribute like onclick=""
- [ ] By including the code between `<script>` and `</script>` tags
- [ ] By including a file containing JavaScript using a `<script>` tag

### 4. In the following code, what does the "return false" accomplish?

```JavaScript
<a href="js-01.htm" onclick="alert('Hi'); return false;">Click Me</a>
```

- [x] It keeps the browser from following the href attribute when "Click Me" is clicked
- [ ] It sets the default for the alert() dialog box
- [ ] It suppresses the pop-up dialog that asks "Are you sure you want to navigate away from this page?"
- [ ] It is necessary to insure that the onclick code is at least two lines of code

### 5. What happens in a normal end user's browser when there is a JavaScript error?

- [ ] JavaScript prints a traceback indicating the line in error
- [ ] JavaScript skips the line in error and continues executing after the next semicolon (;)
- [ ] JavaScript logs the error to the Django error log
- [x] Nothing except perhaps a small red error icon that is barely noticeable

### 6. Where can a developer find which line in a web page of JavaScript file is causing a syntax error?

- [ ] By looking at a file on the hard disk of the system where the browser is running
- [ ] In the Django error log
- [x] In the developer console in the browser
- [ ] By doing a "View Source" to see the HTML source code

### 7. What does the following JavaScript do?

```JavaScript
console.log("This is a message");
```

- [ ] Sends the message to console.log.com
- [ ] Puts the message in the Django console log
- [x] Puts the message in the browser developer console and continues JavaScript execution
- [ ] Puts the message in the browser console and pauses JavaScript execution

### 8. Which of the following is not a valid comment in JavaScript?

- [ ] /* This is a comment */
- [ ] //This is a comment
- [x] # This is a comment

### 9. Which of the following is not a valid JavaScript variable name?

- [ ] $data
- [x] 3peat
- [ ] $_data
- [ ] _data

### 10. What is the difference between strings with single quotes and double quotes in JavaScript?

- [ ] Single-quoted strings do not treat \n as a newline
- [ ] Double-quoted strings cannot be used in JavaScript
- [ ] Double-quoted strings do variable substitution for variables that start with dollar sign ($)
- [x] There is no difference

### 11. What does the following JavaScript print out?

```JavaScript
toys = ['bat', 'ball', 'whistle', 'puzzle', 'doll'];
```

- [x] ball
- [ ] doll
- [ ] bat
- [ ] whistle

### 12. What value ends up in the variable x when the JavaScript below is executed?

```JavaScript
x = 27 % 2;
```

- [ ] 13.5
- [x] 1
- [ ] 0
- [ ] 2
- [ ] 27
- [ ] 54

### 13. What is the meaning of the "triple equals" operator (===) in JavaScript?

- [ ] Both sides of the triple equals operator are converted to boolean before comparison
- [ ] Both sides of the triple equals operator are converted to integers before comparison
- [x] The values being compared are the same without any type conversion
- [ ] Both sides of the triple equals operator are converted to strings before comparison

### 14. How do you indicate that a variable reference within a JavaScript function is a global (i.e., not local) variable?

- [ ] Use the keyword "global" when declaring the variable outside the function
- [x] Declare the variable globally before the function definition in the code
- [ ] Use the keyword "global" to declare the variable in the function
- [ ] Use the keyword "var" to declare the variable in the function
