class Helper():
    price_history_front_url = "https://performance.morningstar.com/perform/Performance/stock/exportStockPrice.action?"
    price_history_back_url = "&pd=1y&freq=d&sd=&ed=&pg=0&culture=en-US&cur=USD"
    price_history_symbol_query_url ="t=" #t=XNAS:AMZN

    def getPriceHistoryUrl(self, symbol, exchange):
        self.price_history_symbol_query_url = self.price_history_symbol_query_url + exchange + ":" + symbol
        return self.price_history_front_url + self.price_history_symbol_query_url + self.price_history_back_url
