- This is the **Flask** learning.
- Flask has two components:
  1. WSGI: Web Server Gateway Interface
  2. Jinja2: Template

**WSGI**: to handle the request and response between the client and the server. It can process one request at a time.

**Jinja**: Can help to build dynamic webpages, support inheritance and can help to reduce the repetativeness of the code and it's complexity.

_Two kinds of Parameters_

1. Path parameters: Use to access the perticular endpoint
2. Query parameters: Filtering the data of perticular endpoint

\***\* Use of Conditional clause to start the server \*\***

- The app.run() command must be in the if **name** == "**main**" statement.
- Unlike JavaScript where each file is saperate module by default, Python files can be imported inside other file.
- If the script is imported as a module into another Python script, **name** is set to the name of the file.

_Path Parameter_

- The (string) parameters can be passed in the end point using <> brackets.
- To pass the parameters of the specific type, we need to mention the datatype, eg "<int:num>"

-> For the different endpoints, we can not have the same calling function.
-> While server is running, any the changes in the file will be saved automatically except the web page needs to be refreshed manually.

**Difference between Path Parameters and Dynamic URL**

- In the context of the web development, to say the Path parameters and dynamic url are the same thing.
- Path parameters are the variable emebeded in the query, while dynamic url are the url that change according to user input.
- e.g., "@app.route('/user/<int:user_id>')", here, /user/123 is a dynamic URL, while <int:user_id> is a path parameter.s

**URL Redirection**

- The URL can be redirected to another url using 'redirect' package of Flask.
- Instead of writing the url manually, we can use url_for to automatically find the corresponding redirected URL.
- We need to use function name of the specific route for the redirection.

**Templates**

- The HTML structure of each and every page is stored in a saperate file called as templates.
- Default naming convention of the folder is itself, 'templates', otherwise needs to be mention about the folder in the app.
- Importing all the templates using 'render_template' package.

- Instead of repetating the layout of html pages, the better way would be to save the layout in one file and extend it wherever we need.
- If we want to display some content specific to the pages, then we can use block to show it. e.g., {%block variable%}... {%endblock variable%}

_If-else block_

- The if-else block will start with {%if%} and ends with {%endif%}, to add elseif statement in between we can write like {%elif%}.

_For loop_

- The for loop has the similar syntax like if-else block that is, {%for%} and ends with {%endfor%}

\***\*CSRF (Cross Site Request Forgery) Attack\*\***

**How it works?**

- A type of an attack where attaker tricks the end-user by performing unintended actions over web application specially when web applications are taking input eg., forms
- An attacker generates an email or a website containing the link containing the request message.
- When a user clicks on it, they will redirected to the web-application, a request will be invoked. The server will have a request from the user, and server will response to that request which is eiter the leakage of the data or some sort of transaction.

**How to prevent?**

- CSRF token : a long, unpredictable string generated at server side when user sign-in for the 1st time and send it back to user's browser.
- Whenever making a request to the server, the CSRD token is must.
- If the token matches with the existing token at server, only then the request will be processed otherwise not.
- So now the token are at two places: with user and at server. If an attacker wants to attack, unless user has shared the token it will be impossible for attacker to attack because to get it from the server, you still need that token.

\***\*WTForms\*\***

- A python liberary to manage, create, validate and handle webforms for python web development
- Supports input validation, CSRF security, integrated with flask (flask-wtf)
- Compliant with 'pythonic' coding style; treat forms as python class, work with forms as objects and attributes and no need to write extensive HTML code

**Login and Sign-up Forms**

- To design the fields of the form, we need variables and invoke the class for the respective field. In which we give the label and the validators. Additionally, for the validators we just import the classes for that.
- That's why the WTForms are called the 'Pythonic' way of designing the forms.

**How to use those forms in the website?**

- Import all the forms to main app.py file and create a object of that imported class whenever we route to the respective pages.
- Now, to send these form to out HTML code files is by passing the object as a parameter in the render_template.
- We still can not use the forms in our website because the WTForms need the CSRF token to be passed before accessing it.

- So,store a SECRET_KEY in app.config[] in app.py and in the html template, the first line of code in the form tag must be '{{form.hidden_tag()}}'

- In the app.route(), we need to pass the methods. Now, because we are going to receive and store the data to the server, we need POST request to be passed. But, firstly we required to have form on the website in order to receive the data. So, the GET request is must.
- To perform the validation of all the input fields, we ought to put the validation on the submit button to check whether all input fields are fulfilling the requirements.
- We can use the flash messages to show successfully regiestered user after navigating to some other page.
- The Flash message appear only once.

**Flask does not have in-built {%comment%} class like Django.**

**SQLAlchemy: The bridge between python and database servers**

| Concept     | Database | Python          |
| ----------- | -------- | --------------- |
| Data        | Table    | Class           |
| Feature     | Column   | Attribute       |
| Observation | Row      | Class Instance  |
| Operation   | Query    | Calling Methods |

- This is how the python understands the concepts of the data, rows, columns and tables.
- After defining the model in form of class, go to the python shell and run the following command

```
from app import db
db.create_all() - Now, this code will give error, because we need to define the application context here.

so, the code will go like:

from app import app, db
app_context = app.app_context()
app_context.push()
db.create_all()
```

_CREATE Operation: After that, to insert the data in the database ,firstly import the class from the main file._

```
from app import Employee
Lucy = Employee(name='Lucy', email='lucy59@xmail.com',age=28)

#after adding all of the data, add those session data and commit the changes to reflect in the database.

db.session.add(Lucy)
db.session.commit()

# for multiple data, we can pass the list;
db.session.add([Will, John])
db.session.commit()
```

_READ Operation: To retrieve all the data of database to our python shell, we need to pass the query._

```
#to get all the rows
employees = Employee.query.all() #the output is a list, can use the loop to print all of them

for emp in employees:
    print(f"{emp.name} is {emp.age} years old, has email {emp.email}")

#to get the first instance
Employee.query.first()

#to get the last instance
Employee.query.last()

#the filter query to find the instance of Will
Employee.query.filter_by(name='Will') #this query is just filtering the data.

#to show the data on console,
Employee.query.filter_by(name='Will').all()
Employee.query.filter_by(name='Will').first()

#extract the data from the ID
db.session.get(Employee, 2)

```

_UPDATE Operation: just pass the new value to respective attribute and commit those changes, it will update the information in the databse_

```
#update the age of John
john = employees[-1]
john.age = 57
db.session.commit()

```

_DELETE Operation: the same way as the update operation_

```
john = employees[-1]
db.session.delete(john)
db.session.commit()

```

_One to Many Operation_

- With the 'backref' passing in the main table, we don't need the id to specify entry in the either table. we can just pass the object name as an id to pass it rather than finding an id and putting it there.

**We can add all the objects together without passing which is which. The SQLAlchemy will identify it's table and push the data in it while commitng the changes.**

- If we want to find the player playing for CSK, then we can do like;

```
csk_team = Team.query.first()
csk_team.members
```

- If we know the player name and we wanted to find which team he's playing for;

```
msd_player = Player.query.first()
msd_player.team #the members refrence work both ways.
```

_Many to Many Relationship: need an associate table additioanlly_

- the Alchemy doesn't know that this associate table is connected with the two primaraly table. So, for that we need to pass backref in one of the table along with an additional argument; secondary='table_name'.
- While adding the data, we can add the data normally by passing the value to all the attributes without caring about the refrences to associate table.

- Now, the items part, the steve.items is a list; SQLAlchemy list. So, in order to add the products in it, we just need to append or extend(if more than 1) the list.

```
steve.items
type(steve.items)
cup.owners
type(cup.owners)

steve.items.append(cup) #steve buys the cup
knife.owners.extend([carl, john]) #knife has been bought by carl and john
```
