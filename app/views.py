from flask import render_template, request, jsonify, Response
from app.utils import get_sample_user, get_all_stocks, \
        get_all_stocks_as_csv
from app import app


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


@app.route('/')
@app.route('/index')
def index():
    user = get_sample_user()
    stocks = get_all_stocks()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)

@app.route('/api/stocks.txt')
def stocks_txt():
    return Response('\n'.join([str(s) for s in get_all_stocks()]), mimetype='text/plain')

@app.route('/api/stocks.csv')
def stocks_csv():
    return Response(get_all_stocks_as_csv(), mimetype='text/csv')

@app.route('/api/stocks.json')
def stocks_json():
    return jsonify([s.to_dict() for s in get_all_stocks()])

@app.route('/api/stocks')
def stocks():
    if accept_csv():
        return stocks_csv()
    elif accept_json():
        return stocks_json()
    else:
        return stocks_txt()

