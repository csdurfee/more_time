import os, pprint
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort

import flask

import views

app = flask.Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(flask.g, 'db'):
        flask.g.db.close()

# ROUTES
app.route('/<int:idx>')(views.index)

app.route('/record_time', methods=['GET', 'POST'])(views.record_time)

app.route('/projects', methods=['GET', 'POST'])(views.projects)

app.route('/account', methods=['GET', 'POST'])(views.account)

app.route('/stats')(views.stats)

if __name__ == '__main__':
    app.debug = True
    app.run()
    