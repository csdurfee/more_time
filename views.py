from flask import (make_response, render_template, flash,
                   Flask, request, session, g,
                   redirect, url_for, abort)
from models import Project, Task

def index(idx):
    ctx = {'title' : 'fixme'}
    resp = make_response(render_template("index.html", page=ctx))
    return resp


def record_time():
    # get user or create anonymous user.
    # create anonymous user should also create a dummy project and task.
    #g.app.logger.debug("here I am")
    project_id = 123
    task_id = 456
    note = "fooby foo"
    page = locals()
        
    
    if request.method == "POST":
        """record the time."""
        g.app.logger.error("hoo hah")
        
        # create a unit of work.
        
        # if task assigned, add it there.  otherwise add to junk drawer.
        
        # if project assigned, add it.  otherwise add to junk drawer.
        
        project_on = Project.objects.get_or_create(id=project_id)
        task_on = Task.objects.get_or_create(id=task_id)
        
        # todo: save should trigger server-side js on successful save
        # or rather, kick up an error when unssuccessful
        
        resp = make_response("HOOTY HOO")
        resp.headers['Content-Type'] = "application/javascript;";
        # make it JS!
    else:
        """return timer page."""
        resp = make_response(
                render_template("record_time.html", page=page))
    return resp

def projects():
    pass

def account():
    pass

def stats():
    pass
