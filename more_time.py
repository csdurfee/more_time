import os, pprint
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort
import flask

import redisco


app = flask.Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
@app.before_request
def before_request():
    flask.g.redisco_client = redisco.get_client()
    

@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    flask.g.redisco_client.flushdb()
    
    
# ROUTES
# TODO: replace these with blueprints.
#
#app.register_blueprint(base)

from views import base, task, admin, account, user
app.route('/<int:idx>')(base.index)
#
app.route('/record_time', methods=['GET', 'POST'])(task.record_time)

app.route('/projects', methods=['GET', 'POST'])(user.projects)

app.route('/account', methods=['GET', 'POST'])(account.account)

#app.route('/stats')(views.stats)


if __name__ == '__main__':
    app.debug = True
    app.run()
    