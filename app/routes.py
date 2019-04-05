# the first 'app' is directory, and second 'app' is variable defined in the __init__.py
from flask import render_template, flash, redirect, url_for
from app import app

# decorator is a feature of the Python language that allows you to enhance functions with additional behavior
# in this case, two urls map to a same function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dom_vio_sta')
@app.route('/index/dom_vio_sta')
def dom_vio_sta():
    return render_template('dom_vio_sta.html')

# As setting the action attribute to an empty string, it will going to come back on the same url when the browser submits the form to us