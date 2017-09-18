from flask import render_template
from datetime import date
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'wgx731'}
    stocks = [
        {
            'date': date(1985, 11, 1),
            'open': 115.48,
            'high': 116.78,
            'low': 115.48,
            'close': 116.28,
            'volume': 900900,
            'symbol': 'GOOGL'
        },
        {
            'date': date(1985, 11, 4),
            'open': 116.28,
            'high': 117.07,
            'low': 115.82,
            'close': 116.04,
            'volume': 753400,
            'symbol': 'AAPL'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)
