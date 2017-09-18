from flask import render_template
from datetime import date
from app.models import User, Stock
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = User('wgx731')
    stock1 = Stock()
    stock1.date = date(1985, 11, 1)
    stock1.open = 115.48
    stock1.high = 116.78
    stock1.low = 115.48
    stock1.close = 116.28
    stock1.volume = 900900
    stock1.symbol = 'GOOGL'
    stock2 = Stock()
    stock2.date = date(1985, 11, 4)
    stock2.open = 116.28
    stock2.high = 117.07
    stock2.low = 115.82
    stock2.close = 116.04
    stock2.volume = 753400
    stock2.symbol = 'AAPL'
    stocks = [stock1, stock2]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)
