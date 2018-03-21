from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sup3r$3cretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qmamvhsfyzobuc:198505cbbea1ab13419fd8d8f40fc17f79db0e7b2de963b7c96c1f099c8a3f1a@ec2-54-204-44-140.compute-1.amazonaws.com:5432/d88kvh89dd68fq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
UPLOAD_FOLDER = "./app/static/uploads"

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views



