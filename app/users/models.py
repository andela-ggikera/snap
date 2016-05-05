"""Snap model."""
from datetime import datetime
from app import db, flask_bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    """User model class definition."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    _password = db.Column(db.String(255))
    created_on = db.Column(
        db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Show object instance representation."""
        return 'User: {}'.format(self.username)

    @hybrid_property
    def password(self):
        """Encrypted password of a user."""
        return self._password

    @password.setter
    def password(self, password):
        """Encrypt the password on assignment."""
        self._password = flask_bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        """Confirm a user is authenticated."""
        return True

    def is_active(self):
        """Confirm a user is active."""
        return True

    def is_anonymous(self):
        """Confirm a User is anonymous."""
        return False

    def get_id(self):
        """Get user id as a string."""
        return unicode(self.id)
