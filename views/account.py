from view_imports import *


from models import User, UserManager

import forms
#####################

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = forms.LoginForm()

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
				#return redirect(request.values['next']) # TODO: right?
			else:
				g.logger.debug("login failsed!")
				flash("Incorrect login or password")
		else:
			flash("Incorrect login or password")
			g.logger.debug("no user found, ruh roh.")

	g.user = None
	return render_template("login.html", form=form, page = {})
    

def logout():
    pass

def account():
    pass

def create_account():
	pass

