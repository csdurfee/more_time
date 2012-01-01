# common imports used by all views (or harmless if in all views)
# NOT model code!  framework stuff.
from functools import wraps
import json

from flask import (make_response, render_template, flash,
                   Flask, request, session, g,
                   redirect, url_for, abort, escape, Blueprint,)

# stolen directly from flask documentation.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.has_key('user_name') and session['user_name']:
        	pass
        else:
            return redirect(url_for('account.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function