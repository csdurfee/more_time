from redisco import models


class Validators:
    @staticmethod
    def passwordOK(field_name, field_value):
        if not field_value or len(field_value) < 5:
            return (field_name, u"Password too short!")

class StaticPage(models.Model):
    title = models.Attribute(required=True)
    text = models.Attribute(indexed=False)
    
#@fixme: blort    
class User(models.Model):
    real_name = models.Attribute(required=True)
    user_name = models.Attribute(required=True)
    password  = models.Attribute(required=True, validator=Validators.passwordOK)
    active = models.BooleanField(default=True)
    
class UnitOfWork(models.Model):
    note = models.Attribute()
    start_time = models.DateTimeField()
    end_time = models.DateField()
    
    def elapsed(self):
        if not self.end_time:
            return 0
        return self.end_time - self.start_time

class Task(models.Model):
    name = models.Attribute()
    units_of_work = models.ListField(UnitOfWork)
    
    def elasped(self):
        _all_times = [x.elapsed() for x in self.units_of_work]
        return sum(_all_times)
    
class Project(models.Model):
    name = models.Attribute()
    tasks = models.ListField(Task)
    
class UserSpace(models.Model):
    users = models.ListField(User)
    name = models.Attribute(required=True)