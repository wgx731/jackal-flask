from datetime import datetime
from functools import wraps
from flask import request, Response
from flask_jwt import JWT, jwt_required
from app import app, bcrypt
from app.models import User


# JWT
def authenticate(username, password):
    user = User.query.filter_by(username = username).scalar()
    if user is None:
        return None
    if bcrypt.check_password_hash(user.password, password):
        return user

def identity(payload):
    return User.query.get(payload['identity']['id'])

jwt = JWT(app, authenticate, identity)

@jwt.jwt_payload_handler
def make_payload(identity):
    iat = datetime.utcnow()
    exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
    return {
        'exp': exp, 
        'iat': iat,
        'nbf': nbf, 
        'identity': {
            'id': identity.id, 
            'name': identity.username,
            'email': identity.email
        }
    }

@jwt_required()
def jwt_auth_func(**kw):
    pass

# HTTP Basic
def check_http_basic_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return authenticate(username, password) is not None

def wrong_http_basic_credentials():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def http_basic_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_http_basic_auth(auth.username, auth.password):
            return wrong_http_basic_credentials()
        return f(*args, **kwargs)
    return decorated

