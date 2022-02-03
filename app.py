#app.py

from crypt import methods
from myproject import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm,RegistrationForm


@app.route("/")
def home():
    return render_template('home.html')




@app.route("/welcome")
@login_required
def welcome_user():
    return render_template('welcome_user.html')



@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))



@app.route("/login",methods=['GET','POST'])
def login():

    pass