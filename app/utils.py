from io import StringIO
from datetime import date
import csv
from app.models import User, Stock


def get_sample_user():
    return User('wgx731')

def get_sample_stocks():
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
    return [stock1, stock2]

def get_sample_stocks_as_csv():
    si = StringIO()
    cw = csv.DictWriter(si, Stock.keys())
    cw.writeheader()
    cw.writerows([s.to_dict() for s in get_sample_stocks()])
    return si.getvalue()

