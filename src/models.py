from datetime import datetime
from src import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='default-male.png')

    def __repr__(self):
        return f"User('{self.email}', '{self.avatar}')"


class Book():
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    published_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.isbn}','{self.published_date}',)"


