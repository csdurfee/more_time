from view_imports import *

base_blueprint = Blueprint('base', __name__)

@base_blueprint.route("/")
def home():
    ctx = {'title' : 'fixme'}
    g.logger.debug("fancypants!")
    if session.new:
	    flash("Welcome to more_time!")
    resp = make_response(render_template("welcome.html", page=ctx))
    return resp