#!/usr/bin/python3
"""
A script that starts a Flask web application:
    The application listens on 0.0.0.0, port 5000
Route 1:
    '/'
Dispalys:
    'Hello HBNB!''
Route 2:
    '/hbnb'
Displays:
    “HBNB”
Route 3:
    '/c/<text>'
    Displays “C ” followed by the value of the <text>
    variable (replace underscore _ symbols with a space )
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """Dispalys 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dispaly_hbnb():
    """Dispalys 'HBNB!'"""
    return 'HBNB'

 
def remove_url_underscore(text):
    """
    Helper function for route '/c/<text>' that will replace
    underscores(_) in the url param with spaces
    """
    return text.replace("_", " ")


@app.route('/c/<text>', strict_slashes=False)
def display_C_var_value(text):
    """Dispays 'C' followed by URL parameters(<text>) value"""
    formatted_url_output = remove_url_underscore(text)
    return f'C {formatted_url_output}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
