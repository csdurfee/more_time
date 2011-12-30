from view_imports import *


from models import User, UserManager

from flaskext.wtf import *

### TODO? move these back to their own file?  not really model or view.

class SignupForm(Form):
    user_name = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.Required()])
    email = TextField('email', [validators.Required()])
    accept_tos = BooleanField('I accept the TOS', [validators.Required])

class LoginForm(Form):
    user_name = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

#####################

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if request.method == "POST" and form.validate():
		# lookup user by username
		potential_user = User.objects.filter(user_name=form.data['user_name'])
		if len(potential_user):
			g.logger.debug("found a user!")
			first_user = potential_user[0]
			if first_user.check_password(form.data['password']):
				g.logger.debug("successful login")
				flash("You've been successfully logged in")
				session['user_name'] = form.data['user_name']
				return redirect(url_for('base.home'))

			else:
				g.logger.debug("login failsed!")
				flash("Incorrect login or password")


		else:
			flash("Incorrect login or password")
			g.logger.debug("no user found, ruh roh.")

	return render_template("login.html", form=form, page = {})
    

def logout():
    pass

def account():
    pass

def create_account():
	pass

