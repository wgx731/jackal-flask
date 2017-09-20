from flask import Flask
import flask_restless_swagger
import flask_sqlalchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////opt/webapp/db/local.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
manager = flask_restless_swagger.SwagAPIManager(app, flask_sqlalchemy_db=db)

from app import models, views

