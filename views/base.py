from view_imports import *

base_blueprint = Blueprint('base', __name__)

@base_blueprint.route("/")
def home():
    ctx = {'title' : 'fixme'}
    g.logger.debug("fancypants!")
    flash("howdy pards")
    flash('niceta meatcha')
    resp = make_response(render_template("welcome.html", page=ctx))
    return resp