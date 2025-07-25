#!/usr/bin/python3
"""
Write a script that starts a Flask web application

Your web application must be listening on 0.0.0.0, port 5000
Routes:

/: display “Hello HBNB!”

/hbnb: display “HBNB"

/c/<text> display “C ” followed by the value of the text variable

/python/<text>: display “Python ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”

/number/<n>: display “n is a number” only if n is an integer

You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return "C " + text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_fun(text="is cool"):
    text = text.replace('_', ' ')
    return "Python " + text


@app.route("/number/<int:num>", strict_slashes=False)
def convert_int(num):
    return str(num) + " is a number"


if __name__ == '__main__':
    app.run()
