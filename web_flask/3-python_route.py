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
    Displays:
        “C ” followed by the value of the <text>
        variable (replace underscore _ symbols with a space )
Route 4:
    '/python/(<text>)'
    Dispalys:
    “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space ) and sets
    the default value of <text> to “is cool”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """Dispalys 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dispaly_hbnb():
    """Dispalys 'HBNB!'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C_var_value(text):
    """Dispays 'C' followed by the value of <text> param in the url"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
# The below route displays the default value of param
# if no value is specified in the url
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """
    Displays “Python ”, followed by the value of the <text> param in 
    the url, or displays “Python ” followed by the default value of text
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
