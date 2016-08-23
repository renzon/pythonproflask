# -*- coding: utf-8 -*-
"""`main` is the top level module for your Flask application."""
from __future__ import absolute_import, unicode_literals

# Import the Flask Framework
from flask import Flask, request
from flask.ext.babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'en'


@babel.timezoneselector
def get_timezone():
    'UTC'


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    request.form.get('')
    return 'Hello World Flask!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
