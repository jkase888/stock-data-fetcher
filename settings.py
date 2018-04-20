class Helper():
    stockList = ["XNAS:AMZN", "XNAS:MSFT", "XNAS:AAPL", "XNYS:CRM", "XNYS:RTN",
    "XNAS:FB", "XNYS:TWTR", "XNAS:PYPL", "XNAS:TSLA","XNYS:SPOT", "XNAS:INTC",
    "XNYS:WMT", "XNYS:LMT", "XNYS:FDX", "XNAS:BABA", "XNAS:GOOG", "XNAS:ADBE",
    "XNYS:UPS", "XNYS:DIS", "XNYS:SBUX", "XNYS:HD", "XNYS:BAC", "XNYS:MCD",
    "XNAS:PANW", "XNAS:SPLK", "XNAS:EA", "XNAS:TTWO", "XNYS:BB", "XNAS:SQ",
    "XNAS:NVDA", "XNYS:NOC", "XNYS:BA", "XNYS:GS", "XNAS:NFLX", "XNYS:SNAP",
    "XNYS:GRUB", "XNYS:IBM", "XNAS:IBB", "XTSE:T.CNR", "XTSE:T.CP", "XTSE:T.IFC",
    "XTSE:X", "XTSE:DOL", "XTSE:CAE", "XTSE:TO", "XNAS:WYNN", "XNYS:RCL",
    "XNYS:SHOP", "XTSE:CSU", "XTSE:OSB", "XTSE:PBH", "XTSE:GOOS", "XNYS:MA",
    "XNYS:V", "XTSE:TSGI", "XNYS:COST", "XNYS:ACN", "XTSE:WSP", "XNYS:LOW",
    "XNAS:WDAY", "XNAS:LULU"]

    period = "6m"


    price_history_front_url = "https://performance.morningstar.com/perform/Performance/stock/exportStockPrice.action?"
    price_history_back_url = "&pd=" + period + "&freq=d&sd=&ed=&pg=0&culture=en-US&cur=USD"
    price_history_symbol_query_url ="t=" #t=XNAS:AMZN

    def getPriceHistoryUrl(self, symbol = None, exchange = None, exchangeAndStock = None):
        if ((symbol is not None) and (exchange is not None)):
            self.price_history_symbol_query_url = self.price_history_symbol_query_url + exchange + ":" + symbol
        if (exchangeAndStock is not None):
            self.price_history_symbol_query_url = self.price_history_symbol_query_url + exchangeAndStock
        return self.price_history_front_url + self.price_history_symbol_query_url + self.price_history_back_url

    def resetURL(self):
        self.price_history_front_url = "https://performance.morningstar.com/perform/Performance/stock/exportStockPrice.action?"
        self.price_history_back_url = "&pd=" + self.period + "&freq=d&sd=&ed=&pg=0&culture=en-US&cur=USD"
        self.price_history_symbol_query_url ="t="
