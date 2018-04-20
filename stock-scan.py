import urllib2
import csv
from stock import Stock
from database import DatabaseGateway
from var_dump import var_dump
from settings import Helper


helper = Helper()
for stock in helper.stockList:
    helper.resetURL()
    print(stock)
    url = helper.getPriceHistoryUrl(exchangeAndStock = stock)
    dataResponse = urllib2.urlopen(url=url)
    dataCsv = csv.reader(dataResponse)


    #connect to database
    db = DatabaseGateway()
    db.connect()

    j = 0
    for row in dataCsv:
        if (j > 1):
            row[5] = row[5].replace(',','')
            try:
                row[5] = int(row[5])
            except ValueError:
                row[5] = 0
            isError = db.insertHistroicalPrice(row, stock)
        j = j + 1
    db.close()
