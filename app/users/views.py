"""Snap views."""
from flask import flash, redirect, render_template, url_for
from flask import Blueprint
from flask.ext.wtf import Form
from flask.ext.login import login_user, logout_user, current_user
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
from app import flask_bcrypt
from models import User

users = Blueprint(
    'users', __name__, template_folder='templates')


class LoginForm(Form):
    """A form subclasss that represents the login form and it's validators."""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField(
        'password', validators=[DataRequired(), Length(min=6)])


@users.route('/login', methods=['GET', 'POST'])
def login():
    """User login functionality."""
    if current_user.is_authenticated:
        return redirect(url_for('snaps.listing'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data).first()
        if not user:
            flash("No such user exists")
            return render_template('users/login.html', form=form)

        if not flask_bcrypt.check_password_hash(
                user.password, form.password.data):
            flash("invalid password")
            return render_template('users/login.html', form=form)

        login_user(user, remember=True)
        flash("Success! You are logged in.")
        return redirect(url_for("snaps.listing"))

    return render_template('users/login.html', form=form)


@users.route('/logout', methods=['GET'])
def logout():
    """Log the user out."""
    logout_user()
    return redirect(url_for('snaps.listing'))
