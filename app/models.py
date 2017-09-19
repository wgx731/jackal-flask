from app import db


class User:
    """A User class"""
    def __init__(self, nickname):
        self.name = nickname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nickname):
        self.__name = nickname


class Stock(db.Model):
    """A Stock class"""
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Integer)
    symbol = db.Column(db.String(10), unique=True)

    def __init__(self, date, open, high, low, close, volume, symbol):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.symbol = symbol

    @classmethod
    def keys(cls):
        return [
            'symbol', 'open', 'high',
            'low', 'close', 'volume', 'date'
        ]

    def __repr__(self):
        return '<Stock %r>' % self.symbol

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume,
            'date': self.date.isoformat()
        }

    def __str__(self):
        return 'Stock - {} with price: {}, {}, {}, {}, {} on {}'.format(
            self.symbol,
            self.open,
            self.high,
            self.low,
            self.close,
            self.volume,
            self.date)

