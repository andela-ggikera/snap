"""Initial db configuration."""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypy import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from app.users import models as user_models
from app.users.views import users


@login_manager.user_loader
def load_user(user_id):
    """Get the user using his id."""
    return app.user_models.query.get(int(user_id))
