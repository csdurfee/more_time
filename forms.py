from flaskext.wtf import *

### 

class SignupForm(Form):
    user_name = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.Required()])
    email = TextField('email', [validators.Required()])
    accept_tos = BooleanField('I accept the TOS', [validators.Required])

class LoginForm(Form):
    user_name = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
