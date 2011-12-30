import os
import pprint
from optparse import OptionParser
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort

import redisco

Flask.secret_key = '189829iqwoeprjqwpoer12341234124321'

app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
@app.before_request
def before_request():
    g.redisco_client = redisco.get_client()
    #flask.g.app = app
    g.logger = app.logger

@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    # this blows away everything in the DB!
    #flask.g.redisco_client.flushdb()
    
# ROUTES
# TODO: replace these with blueprints.
#
#app.register_blueprint(base)

from views.task import task_blueprint
from views.base import base_blueprint
from views.admin import admin_blueprint
from views.account import account_blueprint
        

app.register_blueprint(task_blueprint)
app.register_blueprint(base_blueprint)
app.register_blueprint(account_blueprint)

#from views import base, task, admin, account, user
#app.route('/<int:idx>')(base.index)
#
#app.route('/record_time', methods=['GET', 'POST'])(task.record_time)

#app.route('/projects', methods=['GET', 'POST'])(user.projects)

#app.route('/account', methods=['GET', 'POST'])(account.account)

#app.route('/stats')(views.stats)


if __name__ == '__main__':
    app.debug = True
    # TODO: go off debug command-line flag
    if app.debug:
        app.register_blueprint(admin_blueprint)
    app.run()
    