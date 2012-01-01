import os
import pprint
from optparse import OptionParser
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort

import redisco

app = Flask(__name__)
app.config.from_pyfile("config.py")
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

# TODO: make this less ugly
# NB. these have to go after config.from_pyfile, etc.
from views.project import project_blueprint
from views.base import base_blueprint
from views.admin import admin_blueprint
from views.account import account_blueprint

# register sub-apps
app.register_blueprint(project_blueprint)
app.register_blueprint(base_blueprint)
app.register_blueprint(account_blueprint)

if __name__ == '__main__':
    print "%r" % app.config

    app.debug = True
    # TODO: go off debug command-line flag
    if app.debug:
        app.register_blueprint(admin_blueprint)
    app.run()
    