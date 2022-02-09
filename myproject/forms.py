#forms
from flask_wtf import FlaskForm
from myproject.models import User
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")



class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',
    message='Passwords must match!!'),Length(min=8,max=50)])


    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')



    def check_email(self,field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('your email has already been registred')


    def check_username(self,field):
        user_name = User.query.filter_by(username=field.data).first()
        if user_name:
            raise ValidationError('Username is Taken!!')