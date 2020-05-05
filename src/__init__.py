import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config.from_object('src.config')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['DEBUG'] = os.getenv('DEBUG')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
app.config['ALLOWED_EXTENSIONS'] = ['txt', 'svc']

db = SQLAlchemy(app)

from src import routes
