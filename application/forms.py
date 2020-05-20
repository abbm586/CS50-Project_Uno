from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=15)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=15)])
    # occupation = StringField('Ocupation', validators=[DataRequired(), Length(max=15)])
    smart_nr = StringField('Smart Number', validators=[DataRequired(), Length(max=15)])
    email = StringField('Email', validators=[DataRequired(), Length(max=25),
                            Email(message='A Valid email format is required'),])
    bio = TextAreaField('Biography', validators=[Length(max=250)], default='Give a small description of function')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    date_created = DateField('date Created', default=datetime.utcnow)
    submit = SubmitField('Create Account')


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=25),
                                        Email(message='A Valid email format is required')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=25)])
    submit = SubmitField('Create Account')