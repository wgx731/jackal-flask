import os
from datetime import datetime
from functools import wraps
from flask import request, jsonify, Response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from app import app, bcrypt
from app.models import User

app.secret_key = os.environ.get('SECRET_KEY', 'please-change-me')

# JWT
def authenticate(username, password):
    user = User.query.filter_by(username = username).scalar()
    if user is None:
        return None
    if bcrypt.check_password_hash(user.password, password):
        return user

jwt = JWTManager(app)

@app.route('/auth', methods=['POST'])
def auth():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    params = request.get_json()
    username = params.get('username', None)
    password = params.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = authenticate(username, password)
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    ret = {
        'access_token': create_access_token(identity={
            'id': user.id,
            'name': user.username,
            'email': user.email
        })
    }
    return jsonify(ret), 200

@jwt_required
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

