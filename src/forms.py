from wtforms import StringField, PasswordField, DateField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserLogin():
    email = StringField('Email',
                        validators=[DataRequired(), Email(message="valid email required here"),
                                    Length(min=2, max=15)])
    password = PasswordField('Password',
                        validators=[DataRequired(), Length(min=8, max=100)])
    twoFactor = StringField('2Factor Code',
                        validators= [DataRequired(), Length(min=2, max=15)])
    submit = SubmitField('Login')


class UserRegister():
    name = StringField('Name',
            validators= [DataRequired(), Length(min=2, max=15)])
    Surname = StringField('Surname',
                       validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email',
                       validators=[DataRequired(), Email(message="valid email required here"),
                                   Length(min=2, max=15)])
    password = PasswordField('Password',
                        validators=[DataRequired(), Length(min=8, max=100)])
    confirm = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password', message='Password must match')])
    date_registered = DateField('Date Registered', format= "'%d/%m/%Y")
    submit = SubmitField('Register')


class PasswordReset():
    twoFactor = StringField('Confirmation Code',
                      validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password',
                      validators=[DataRequired(), Length(min=8, max=100)])
    confirm = PasswordField('Confirm Password',
                      validators=[DataRequired(), EqualTo('password', message="password must match")])
    submit = SubmitField('Reset')

class FileUpload():
    file = FileField('file upload')
    submit = SubmitField('Upload')
