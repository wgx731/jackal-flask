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

class Stock:
    """A Stock class"""
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def open(self):
        return self.__open

    @open.setter
    def open(self, open):
        self.__open = open

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, high):
        self.__high = high

    @property
    def low(self):
        return self.__low

    @low.setter
    def low(self, low):
        self.__low = low

    @property
    def close(self):
        return self.__close

    @close.setter
    def close(self, close):
        self.__close = close

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol

    @classmethod
    def keys(cls):
        return [
            'symbol', 'open', 'high',
            'low', 'close', 'volume', 'date'
        ]

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

