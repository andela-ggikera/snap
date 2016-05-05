"""Initial db configuration."""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
app.config['SECRET_KEY'] = "fsdfsgvetw4hb34523r14"
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app.users import models as user_models
from app.users.views import users


def create_app(config='defualt'):
    """Create app."""
    app.register_blueprint(users, url_prefix='/users')
    return app


@login_manager.user_loader
def load_user(user_id):
    """Get the user using his id."""
    return app.user_models.query.get(int(user_id))
