#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    returns a rendered html template
    using the data from states and amenities
    """
    states = storage.all('State').value()
    citites = storage.all('City').value()
    amenities = storage.all('Amenity').value
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
