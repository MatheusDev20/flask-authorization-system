from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8), EqualTo('password')])
    role = SelectField( choices=[('operation', 'Operation'), ('intern', 'Intern'), ('manager', 'Manager')] ,validators=[DataRequired()])
    avatar = FileField(validators=[FileRequired()])
    submit = SubmitField('Create User')


class LoginUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')