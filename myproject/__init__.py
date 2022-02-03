import os
from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from flask_migrate import Migrate

login_manager = LoginManager()

app = Flask(__name__)


app.config['SECRETE_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLALCHEMY(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'