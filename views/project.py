from view_imports import *

from models import *

project_blueprint = Blueprint('project', __name__)

@project_blueprint.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    g.logger.debug("getting all projects for user")
    page = dict(title='projects list')

    user_name = session.get('user_name', 'casey')

    user = User.objects.get_or_create(user_name = user_name)

    resp = make_response(
                render_template("projects.html", page=page, user=user))
    return resp    


@project_blueprint.route('/record_time', methods=['GET', 'POST'])
def record_time():
    # get user or create anonymous user.
    # create anonymous user should also create a dummy project and task.
    g.logger.debug("here I am")

    (user, active_project, active_task) = UserManager.get_for_timer(session, request)
    
    page = dict(title='record time')
    # TODO: validate user.    
    
    if request.method == "POST":
        """record the time."""
        g.logger.debug("recording time for %r" % request.values)
        
        #note = request.values['note']
        start_time = request.values['start_time']
        end_time = request.values['end_time']

        note = None # FIXME

        # create a unit of work.  save it.  associate it with task.

        work_unit = UnitOfWork( start_time=int(start_time), 
                                end_time=int(end_time),
                                task=active_task)
        g.logger.debug("cp 1")
        if not work_unit.is_valid():
            g.logger.debug("work unit not valid: %r" % work_unit.errors)
        active_task.save()
        work_unit.save()
    
        g.logger.debug("saved the work unit!")

        ctx = {'status' : 'OK'}
        resp = make_response(json.dumps(ctx))
        resp.headers['Content-Type'] = "application/javascript;";
        # make it JS!
    else:
        """return timer page."""
        #page = dict(project_id=123, task_id=234, is_temp=False)
        resp = make_response(
                render_template("record_time.html", page=page, project=active_project, task=active_task))
    return resp

def create_task():
    pass
