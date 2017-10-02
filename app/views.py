from flask import render_template, jsonify, Response, request
from app import app, manager
from app.utils import get_all_stocks, get_all_stocks_with_paging,\
        get_all_stocks_as_csv
from app.models import User, Stock
from app.auth import jwt_auth_func, jwt_required, http_basic_required


def accept_json():
    best = request.accept_mimetypes \
            .best_match(['application/json', 'text/plain'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/plain']


def accept_csv():
    best = request.accept_mimetypes \
            .best_match(['text/csv', 'text/plain'])
    return best == 'text/csv' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/plain']


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index/<int:page>', methods=['GET'])
@http_basic_required
def index(page=1):
    per_page = 10
    user = User.query.filter_by(
        username=request.authorization.username
    ).scalar()
    stocks = get_all_stocks_with_paging(page, per_page)
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)


@app.route('/graph', methods=['GET'])
@http_basic_required
def graph():
    user = User.query.filter_by(
        username=request.authorization.username
    ).scalar()
    return render_template("graph.html",
                           title='Graph',
                           user=user)


# list stocks txt api
@app.route('/api/stocks.txt', methods=['GET'])
def get_stocks_in_txt():
    return Response(
        '\n'.join([str(s) for s in get_all_stocks()]),
        mimetype='text/plain'
    )


# list stocks csv api
@app.route('/api/stocks.csv', methods=['GET'])
def get_stocks_in_csv():
    return Response(get_all_stocks_as_csv(), mimetype='text/csv')


# list stocks json api
@app.route('/api/stocks.json', methods=['GET'])
def get_stocks_in_json():
    return jsonify([s.to_dict() for s in get_all_stocks()])


# list stocks content negotiation api
@app.route('/api/stocks', methods=['GET'])
@jwt_required
def get_stocks():
    if accept_csv():
        return get_stocks_in_csv()
    elif accept_json():
        return get_stocks_in_json()
    else:
        return get_stocks_in_txt()


manager.create_api(
    Stock,
    methods=['GET', 'PUT', 'POST', 'DELETE'],
    preprocessors=dict(
        PUT=[jwt_auth_func],
        POST=[jwt_auth_func],
        DELETE=[jwt_auth_func]
    )
)
