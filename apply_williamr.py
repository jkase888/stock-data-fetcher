from database import DatabaseGateway
from var_dump import var_dump
from settings import Helper


getWiliamrHighSQL = """select max(high) from
    (select * from historical_prices
        where datestamp > (CURRENT_DATE - 30) and symbol = '[SYMBOL]'
        order by datestamp desc
        limit 14
    ) as williamMax"""

getWiliamrLowSQL = """select min(low) from
    (select * from historical_prices
        where datestamp > (CURRENT_DATE - 30) and symbol = '[SYMBOL]'
        order by datestamp desc
        limit 14
    ) as williamMax"""

getRecentCloseSQL = """select close, datestamp from historical_prices
  where symbol = '[SYMBOL]'
  order by datestamp desc
  limit 1"""

helper = Helper()
db = DatabaseGateway("LOCAL")
db.connect()
for stock in helper.stockList:
    statement = getWiliamrHighSQL.replace("[SYMBOL]",stock)
    db.executeSQL(statement)
    high = float(db.getCursor().fetchone()[0])

    statement = getWiliamrLowSQL.replace("[SYMBOL]",stock)
    db.executeSQL(statement)
    low = float(db.getCursor().fetchone()[0])

    statement = getRecentCloseSQL.replace("[SYMBOL]",stock)
    db.executeSQL(statement)
    rs = db.getCursor().fetchone()
    datetime = rs[1]
    close = rs[0]

    williamR = ((high - close)/(high - low))*-100
    print(williamR)
    

db.close()
