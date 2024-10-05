# import flask to create the server
from flask import Flask
import json

# create the app
app = Flask(__name__)

# this is our first endpoint
@app.get("/")
def home():
    # return the component
    return "hello from flask" 
@app.get("/about")
def about():
    #return your name on a json format. 
    name2 = {"name":"Adrian Aguinaga"}
    return json.dumps(name2)
# when you were using JS, the "`" helps you to concatenate,
#  here in python we use f"""<h1></h1>"""

# minichallange
# Create 3 new routes:
1#/greet/{name}: This route should accept a name as part of the URL and return an HTML 
# message saying "Hello, {name}!" styled with CSS.

@app.get("/greet/<name>")
def greet(name):
    return f"""
    <h1 style='color:blue;text-aling:center;'>
    Hello, {name}
    </h1>
    """
2#/square/{number}: This route should take a number as part of the URL and return 
# the square of that number in a styled <p> tag.
@app.get("/square/<int:number>")
def square(number):
    return f"""
    <p style='font-size:20px;color:green;'>
    the square of {number} is {number*number}
    </p>
    """

3#Add a /farewell/{name} route that says goodbye to the person in a <h2> tag with 
# some CSS styling (e.g., font color, size, etc.).
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
    <h1 style='color:blue;text-aling:center;'>
    Goodbye, {name}
    </h1>
    """




# when i save my code, the changes will be applied
app.run(debug=True)
