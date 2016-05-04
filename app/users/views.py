"""Snap views."""
from flask import Blueprint
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

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

