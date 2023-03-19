# Educational and Amusement Quizzes
#### Video Demo:  <https://youtu.be/BGD7Y2MhETg>
#### Description:

## The Objective:
Trying to combine education, challenge and entertainment in various areas and make the bulk of it in Arabic.

## The Motivation:
The idea for all this came from the principle that each human has to learn basic things from severa fields or as the saying goes “A Renaissance
Man is a person whose expertise spans a significant number of different subject areas”.

To accomplish this principle, agreement was reached to build a web based application by using the programming languages that we have learned in the CS50 course. The website should contain various areas and sections, each section has basic questions that provide a bit of brevity in this area. Because of the human nature of beings love competition and challenges, we made the information in the form of questions and a point for every question, and the user will try to gather as many points as they can. Therefore, we were able to do a combination of education and entertainment.

## Used Tools:
Frontend:
* HTML 
* CSS
* JavaScript 

Backend:
* Python (Flask)
* SQL

We used HTML, CSS and JavaScript because they are mostly used in web programming. And Python because it provides a good web framework which makes it possible to make the best use of the database in an easy way.

## Website Components and Details:
The website consists of 12 HTML pages:

1- The fundamental page is the home page which contains a small brief about the website and all quiz sections, with a simple user interface to realize all components with no complications. In addition, the website contains a pie chart that illustrates the percentage of visitors to each section and updated automatically according to the visitor up to that time.

#### All this done by:

* HTML and CSS with Bootstrap framework for designing and building the web page interface. Also, HTML have been used to send the received data from Flas to JavaScript to manipulate these data.

* JavaScript for building the pie chart with the help of a lightweight and robust JavaScript charting library which called AnyChart. AnyChart is an Interactive JavaScript charts designed to be embedded and integrated into web- application.

* We used Flask and SQL to get all sections and their details from the database to Flask endpoint, send these data to the HTML Home Page and then present the required information to the users.

* Finally, we add simple details which include our names and github accounts.

2- The other 10 pages which are the quizzes and each one contains 10 questions. The options order of each question are shuffled every time the user enters the quiz and that to keep the user focused even when the user repeats the quiz. At the end of each questionnaire, the score the user earns will be displayed. We hide the right answers, because we want the user to search for the right answers and this is the best way to learn.

#### All this done by:

* HTML and CSS for designing the quiz page interface. We tried to make it as simple as much, so the users can focus without any distractions.

* JavaScript to build the whole function from starting the quiz, through transition between questions into wrapping up the quiz and get the final score. All these steps have been done by manipulating the received data from the server.

* SQL and Flask for the backend. SQL contains all sections, their questions, and answers and these are acceded by Flask. Flask gets the questions and answers for specific section to be used in the HTML page and JavaScript code.

3- The last page is the score page, which is linked to all quiz pages. Includes the final total score and the button to return to the home page.

#### All this done by:

* HTML and CSS with Bootstrap framework for designing the web page interface.

* JavaScript for counting the total points, send them to the HTML page and present the points to users.

## Folder Components:
Project Folder includes:
* Static Folder: contains all images have been used in the website, the CSS file and JavaScript file.
* Templates Folder: contains all the HTML pages.
* Python File (app.py)
* The SQL database (results.db) which include two tables one for the Home Page sections and one for the questions.

## Faced Challenges:
* Attempt to move between questions without getting out of the page or update the page.
* Attempt to send data from database to JavaScript and use them efficiently.
* Attempt to reduce the number of code lines as much as possible.

## Future Work:
* Increase the number of fields as much as possible.
* Integrate a discussion service for each field, to allow people with similar interests to discuss with each other.
* Improve UI/UX


## Team members:
* Taghreed Mohammed - <https://github.com/taghreedmoh128>
* Mashael Turki - <https://github.com/mashaelalziedy>