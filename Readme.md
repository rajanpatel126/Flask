- This is the **Flask** learning.
- Flask has two components:
  1. WSGI: Web Server Gateway Interface
  2. Jinja2: Template

**WSGI**: to handle the request and response between the client and the server. It can process one request at a time.

**Jinja**: Can help to build dynamic webpages, support inheritance and can help to reduce the repetativeness of the code and it's complexity.

_Two kinds of Parameters_

1. Path parameters: Use to access the perticular endpoint
2. Query parameters: Filtering the data of perticular endpoint

**_ Use of Conditional clause to start the server _**

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
