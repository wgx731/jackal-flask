from flask import render_template, request, jsonify, Response
from app.utils import get_sample_user, get_all_stocks, \
        get_all_stocks_as_csv
from app import app
from app import manager
from app.models import Stock


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

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    user = get_sample_user()
    stocks = get_all_stocks()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)

# list stocks txt api
@app.route('/api/stocks.txt', methods = ['GET'])
def get_stocks_in_txt():
    return Response('\n'.join([str(s) for s in get_all_stocks()]), mimetype='text/plain')

# list stocks csv api
@app.route('/api/stocks.csv', methods = ['GET'])
def get_stocks_in_csv():
    return Response(get_all_stocks_as_csv(), mimetype='text/csv')

# list stocks json api
@app.route('/api/stocks.json', methods = ['GET'])
def get_stocks_in_json():
    return jsonify([s.to_dict() for s in get_all_stocks()])

# list stocks content negotiation api
@app.route('/api/stocks', methods = ['GET'])
def get_stocks():
    if accept_csv():
        return get_stocks_in_csv()
    elif accept_json():
        return get_stocks_in_json()
    else:
        return get_stocks_in_txt()

manager.create_api(Stock, methods=['GET', 'POST', 'DELETE'])

