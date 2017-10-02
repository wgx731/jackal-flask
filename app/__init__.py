from flask import Flask
from raven.contrib.flask import Sentry
import flask_restless
import flask_sqlalchemy
import flask_bcrypt
import flask_cors
import os

default_db_path = os.path.join(os.path.dirname(__file__), '../db/local.sqlite')
default_db_uri = 'sqlite:///{}'.format(default_db_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', default_db_uri
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.gtag_tracking_id = os.environ.get(
    'GTAG_TRACKING_ID',
    'your-google-tracking-id'
)

cors = flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})
db = flask_sqlalchemy.SQLAlchemy(app)
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
bcrypt = flask_bcrypt.Bcrypt(app)
sentry = Sentry(app)

from app import models, auth, views
