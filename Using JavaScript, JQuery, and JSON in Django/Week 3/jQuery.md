# jQuery

### 1. What is the purpose of the following JQuery ready() call?

```JavaScript
{(document).ready(function(){ window.console && console.log('Hello JQuery..'); });
```

- [ ] Ascertain if the document is ready to load
- [ ] Clear the browser window so drawing can start in the upper left hand corner
- [x] Register a function that will be called when the HTML document is completely loaded
- [ ] Enable the retrieval of data in the JSON format

### 2. What portion of the DOM (Document Object Model) will be affected by the following JQuery statement:

```JavaScript
$('#para').css('background-color', 'red');
```

- [ ] A tag with a class attribute of "para"
- [ ] All elements in the DOM
- [ ] All tags with a class attribute of "para"
- [x] A tag with an id attribute of "para"

### 3. What does the following JQuery code do?

```JavaScript
$('#spinner').toggle();
```

- [ ] Indicate that page loading has completed
- [ ] Call the global JavaScript function toggle with the spinner tag as its parameter
- [x] Hide or show the contents of a tag with the id attribute of "spinner"
- [ ] Switch the spinner.gif with the image spinner_toggle.gif

### 4. What would the following JavaScript print out?

```JavaScript
data = {'one':'two', 'three': 4, 'five' : [ 'six', 'seven' ], 'eight' : { 'nine' : 10, 'ten' : 11 } };
alert(data.eight.nine);
```

- [ ] nine
- [ ] 11
- [ ] seven
- [x] 10
- [ ] six

### 5. Which of the following JQuery statements will hide spiner.gif in this HTML?

```JavaScript
<div id="chatcontent"> <img src="spinner.gif" alt="Loading...</div>
```

- [ ] $("img>spinner.gif").hide();
- [ ] $("spinner.gif").alt =-1;
- [ ] $("spinner.gif").suppress();
- [ ] $(".chatcontent").off();
- [x] $("#chatcontent").hide();
