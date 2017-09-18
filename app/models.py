from datetime import date


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

def get_sample_user():
    return User('wgx731')

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

