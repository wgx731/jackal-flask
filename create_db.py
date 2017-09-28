from datetime import date
from app import db
from app.models import User, Stock

db.create_all()

db.session.add(Stock(
    date(1985, 11, 1),
    115.48,
    116.68,
    115.48,
    116.28,
    900900,
    'GOOGL'
))
db.session.add(Stock(
    date(1985, 11, 4),
    116.28,
    117.07,
    115.82,
    116.04,
    753400,
    'AAPL'
))
db.session.add(Stock(
    date(1985, 11, 5),
    116.04,
    116.57,
    115.88,
    116.44,
    876800,
    'BABA'
))
db.session.add(User(
    'wgx731',
    'wgx731@gmail.com',
    'hackme'
))
db.session.commit()

