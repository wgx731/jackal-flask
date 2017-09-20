from io import StringIO
import csv
from app.models import User, Stock
from app import db


def get_sample_user():
    return User('wgx731')

def get_all_stocks():
    return Stock.query.all()

def get_all_stocks_as_csv():
    si = StringIO()
    cw = csv.DictWriter(si, Stock.keys(), quoting=csv.QUOTE_NONNUMERIC)
    cw.writeheader()
    cw.writerows([s.to_dict() for s in get_all_stocks()])
    return si.getvalue()

