from flask import Flask
import flask_restless_swagger
import flask_sqlalchemy
import os

default_db_path = os.path.join(os.path.dirname(__file__), '../db/local.sqlite')
default_db_uri = 'sqlite:///{}'.format(default_db_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', default_db_uri) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
manager = flask_restless_swagger.SwagAPIManager(app, flask_sqlalchemy_db=db)

from app import models, views

