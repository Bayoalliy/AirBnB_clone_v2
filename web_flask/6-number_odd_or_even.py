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

/number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY

/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY

You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:num>", strict_slashes=False)
def display_num_in_html(num):
    return render_template('5-number.html', n=num)


@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def odd_or_even(num):
    return render_template('6-number_odd_or_even.html', n=num)


if __name__ == '__main__':
    app.run()
