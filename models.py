from redisco import models

#from werkzeug import generate_password_hash, check_password_hash
 
import werkzeug

DEFAULT_PROJECT_NAME = "Junk Drawer"
DEFAULT_TASK_NAME = "My Task"


class StaticPage(models.Model):
    title = models.Attribute(required=True)
    text = models.Attribute(indexed=False)
    
class UnitOfWork(models.Model):
    note = models.Attribute()
    start_time = models.DateTimeField()
    end_time = models.DateField()
    task = models.ReferenceField("Task")
    
    def elapsed(self):
        if not self.end_time:
            return 0
        return self.end_time - self.start_time

    def __unicode__(self):
        return "%s -- %s -- %s -- %s" % (self.task, self.note,
                                         self.start_time, self.end_time)
        
class Task(models.Model):
    name = models.Attribute(default=DEFAULT_TASK_NAME)
    units_of_work = models.ListField(UnitOfWork)
    project = models.ReferenceField('Project')
    
    active = models.BooleanField(default=False)
    
    def elasped(self):
        _all_times = [x.elapsed() for x in self.units_of_work]
        return sum(_all_times)
    
    def __unicode__(self):
        return unicode(self.name)
    
class Project(models.Model):
    name = models.Attribute(default=DEFAULT_PROJECT_NAME)
    tasks = models.ListField(Task)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return unicode(self.name)
#@YAGNI    
"""    
class UserSpace(models.Model):
    users = models.ListField(User)
    name = models.Attribute(required=True)
"""
#@fixme: blort    
class User(models.Model):

    user_name = models.Attribute(required=True)
    real_name = models.Attribute()
    pwdhash  = models.Attribute(required=True)
    active = models.BooleanField(default=True)
    
    email = models.Attribute()
    
    paid = models.BooleanField(default=False)
    
    #profile = models.ReferenceField('UserProfile')
    projects = models.ListField(Project)

    created = models.DateTimeField(auto_now_add=True)

    def check_password(self, password):
        return werkzeug.check_password_hash(self.pwdhash, password)

    #def __init__(self, user_name, password, email):
        #super(User, self).__init__(user_name=user_name, email=email)

    #    self.user_name = user_name
    #    self.pwdhash = werkzeug.generate_password_hash(password)

    @staticmethod
    def create_user(user_name, password, email):
        """redisco doesn't allow you to override the constructor, hence
        the rather ugly staticmethod"""
        u = User(user_name=user_name, email=email)
        u.pwdhash = werkzeug.generate_password_hash(password)
        return u




# TODO: put this in a separate managers.py file.
class UserManager(object):
    """junk-drawer class.  ugh."""

    @staticmethod
    def getForTimer(session=dict()):
        """
        returns an anonymous user, new if necessary,
        
        and the task that is active

        returns (user, active project, active task)
        """
        """if 'username' in session:
            user = User.objects.get_or_create(user_name = escape(session['username']))
        else:
            pass
        """
        user_name = session.get('username', 'casey')

        user = User.objects.get_or_create(user_name = user_name)
        # TODO: get passed in project, not default to active
        active_project = UserManager.getOrCreateActiveProject(user)
        
        active_task = UserManager.getOrCreateActiveTask(active_project)

        return (user, active_project, active_task,)

    @staticmethod
    def getOrCreateActiveProject(user):
        """returns a default, "unclassified" project called Junk Drawer if there
        are no projects, or one isn't active.

        TODO: add last accessed timestamp attr here.
        """
        active_project = None
        first_project = None
        for p in user.projects:
            if not first_project:
                first_project = p
            if p.active:
                active_project = p
                break
        
        if not active_project:
            if first_project:
                active_project = first_project
                active_project.active = True
                active_project.save()
            else:
                active_project = Project(active=True)
                active_project.save()
                user.projects.append(active_project)
                user.save()

        return active_project
    
    @staticmethod
    def getOrCreateActiveTask(project):
        active_task = None
        first_task = None
        for t in project.tasks:
            if not first_task:
                first_task = t
            if t.active:
                active_task = t
                break

        if not active_task:
            if first_task:
                active_task = first_task
                active_task.active = True
                active_task.save()
            else:
                active_task = Task(active=True)
                active_task.save()
                project.tasks.append(active_task)
                project.save()
        return active_task
        
    