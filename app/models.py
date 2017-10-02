from app import db, bcrypt


class User(db.Model):
    """A User class"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.LargeBinary(60))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return 'User - username {} with email {}'.format(
            self.username,
            self.email
        )


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
            self.date
        )
