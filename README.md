<h1 align="center"> CNPvalidator</h>

<p align="center">
  <img src="https://img.shields.io/github/repo-size/razcristea/CNPvalidator?color=green" /> <img src="https://img.shields.io/github/license/razcristea/CNPvalidator" /> <img src="https://img.shields.io/badge/python-3.7-green?logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/debian-VPS-red?logo=debian&logoColor=white" /> <img src="https://img.shields.io/badge/Flask-framework-red?logo=flask&logoColor=white" />
</p>

<p align="center"><img src="http://www.razvancristea.ro/img/SS_cnp.png" href="http://www.razvancristea.ro/CNPvalidator" width="300px"/></p>

## Description
<a href="http://www.razvancristea.ro/CNPvalidator">CNPvalidator</a> is a tool that checks the romanian personal identification number and if valid, gives details about the person, such as date of birth, gender, and the county where this ID was generated for the first time.

## Backend
As a backend it is a Flask web app that uses mod_wsgi module to "talk" with the Apache web server that is hosted on a debian VPS. Server templating it's made using Jinja2 (included in Flask framework).

## Frontend
Frontend is based on Bootstrap and uses a minimal design.

## How it works
When deployed on a production server (Apache, in this case), there is a file `*.wsgi` that imports the Flask function called app from the application directory (defined as such in `__init__.py` file) and renders it to Apache as html.
In `models.py` a class is defined as an object of the WTForms Form class. So, using ORM (Object Relational Mapping) the form that is rendered in browser it is basically an object that takes the input from user and validates it using a function defined in `validators.py`. I could've define the validation function *validate_CNP()* inside the class, but for the sake of usability and to maintain the structure of a modular app, I decided to declare it in its own file. Do note that in that file there are also 3 dictionaries that held some details used for rendering results for valid CNPs'.

After the button is pressed (a request of POST type is sent to the server, containing the user input) and validation is successful (`if request.method == 'POST' and form.validate():`) the file `views.py` is responsible for rendering the results, using some paths called __routes__ - in this case the result is rendered using the same file - `index.html`.

Using the power of Jinja2, we can create a template that dynamically outputs html code using conditions and variables, but also strips and concatenates the string that was entered by the user in form. Let's take for example the date of birth, that shows up in html if you view source in a browser as a simple paragraph and is formatted as "dd-month-yyyy". But what Jinja2 does to render it is this:
```
{{ form.cnp_string.data[5:7]}}-{{ luna[form.cnp_string.data[3:5]] }}-{{ status[form.cnp_string.data[0] |int ][2] }}{{ form.cnp_string.data[1:3] }}
```
`dd` is extracted from CNP itself (CNP is the data stored as a string received from a form that was given to a variable called `cnp_string`, defined as a CNPForm class: `form.cnp_string.data`) and represents the 6th and 7th characters.
`month` is extracted from a dictionary called `luna` that stores in "key":"value" pairs the months of the year, and it takes as a "key" the 4th and 5th characters of the CNP string (basically that's the month in `mm` format) and returns the name of the month corresponding.
`yyyy` is a bit tricky, as only the last 2 digits are extracted from the CNP string - the 2nd and 3rd characters. The first two characters are extracted from the status dictionary, based on the first character of the CNP (`form.cnp_string.data[0]`) - but because is a string and the "key" in this case is an integer, we need to change it, using `| int` - and we need to iterate the "value" returned from dict, as the first two digits are stored in a tuple as the third value: `status[form.cnp_string.data[0] |int ][2]`
If you did check the source of the page, you might've seen a hidden paragraph that shows the date of birth in "mm/dd/yyyy" format. It is there just for calculating age using a JS snippet located in `custom.js`.

## Conclusion
That's the beauty of creating dynamic webpages - you can use multiple programming languages to "do the math" and give the output for the user. In this case there was no need to calculate age server-side, when the browser can do it for us. Same for concatenating date - I could've done it inside the app, but Jinja2 can handle this with great ease, so the final application becomes more structured and code is easier to read and maintain.
