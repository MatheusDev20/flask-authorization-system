from flask_login import LoginManager, login_user, logout_user
from app.modules.users import users_bp
from app.modules.users import login_manager
from flask import request, render_template, redirect, url_for
from app.modules.users.user_form import LoginUserForm
from app.db.models import User
from app.db.repositories.BaseOperations import BaseDbOperations
from flask import flash
from app.db.cryptography import Bcrypt
from app.utils.UsefulFunctions import UseFullFunctions

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@users_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginUserForm()
    if form.validate_on_submit():

        db_operations = BaseDbOperations(User)
        user_info = db_operations.get_by_email(form.data['email'])

        if user_info['status'] == 404:
            flash('User not found')
            return render_template('login.html', title='Login', form=form)

        user = UseFullFunctions.sql_alchemy_to_dict(row=user_info['data'])

        if Bcrypt.check_password_hash(form.data['password'], user['password']):
            login_user(user_info['data'])

            return redirect(url_for('home_bp.home'))

    return render_template('login.html', title='Login',form=form)

@users_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('users_bp.login'))
