class Stock():
    def __init__(self, symbol, exchange):
        self.symbol = symbol
        self.exchange = exchange
        self.trades = [] #list to hold Trade objects


class Trade():
    def __init__(self, symbol = None, open = None, high = None, low = None, close = None, volume = None, datetimestamp = None):
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.datetimestamp = datetimestamp
