#!/usr/bin/python3
""" script that start flask web app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """ return HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def C(text):
    """ return C followed by the value of text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<string:text>', strict_slashes=False)
def Python(text="Python"):
    """ return C followed by the value of text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)