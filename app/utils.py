from io import StringIO
import csv
from app.models import Stock


def get_all_stocks():
    return Stock.query.all()


def get_all_stocks_with_paging(page, per_page):
    return Stock.query.order_by(Stock.date.desc())\
            .paginate(page, per_page, error_out=False)


def get_all_stocks_as_csv():
    si = StringIO()
    cw = csv.DictWriter(si, Stock.keys(), quoting=csv.QUOTE_NONNUMERIC)
    cw.writeheader()
    cw.writerows([s.to_dict() for s in get_all_stocks()])
    return si.getvalue()
