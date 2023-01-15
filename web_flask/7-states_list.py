#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    states_lis = storage.all(State)
    return states_lis