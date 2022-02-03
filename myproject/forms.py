#forms

from email import message
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from myproject.models import User

from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")



class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')



    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('your email has already been registred')


    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is Taken!!')