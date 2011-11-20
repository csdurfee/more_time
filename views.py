from flask import (make_response, render_template, flash,
                   Flask, request, session, g,
                   redirect, url_for, abort)
import models

def index(idx):
    ctx = {'title' : 'fixme'}
    resp = make_response(render_template("index.html", page=ctx))
    return resp


def record_time():
    page = dict(title="Record Time",
                project_id = 123,
                task_id = 234,
                project_name = "project foo",
                task_name = "task bar"
                )
    
    if request.method == "POST":
        """record the time."""
        # get the fucking object.
        project_on = Project.objects.get_or_create(id=project_id)
        task_on = Task.objects.get_or_create(id=task_id)
        
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
