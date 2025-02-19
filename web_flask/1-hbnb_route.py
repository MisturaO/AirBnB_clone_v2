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
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """Dispalys 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dispaly_hbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
