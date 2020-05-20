from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(15),
                     nullable=False)
    surname = db.Column(db.String(15),
                        nullable=False)
    email = db.Column(db.String(100),
                      unique=True,
                      nullable=False)
    smart_nr = db.Column(db.String(15),
                         unique=True,
                         nullable=False)
    bio = db.Column(db.String(120),
                    default="No Information was provided")
    password = db.Column(db.String(200),
                         nullable=False)
    avatar = db.Column(db.String(20),
                       nullable=False, default='default-male.png')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
        
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
        
    def __repr__(self):
        return f"User('{self.email}', '{self.avatar}')"
