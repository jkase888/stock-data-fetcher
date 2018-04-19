import urllib2
import csv
import psycopg2
import os
from stock import Stock
from var_dump import var_dump
from settings import Helper

DATABASE_URL = os.environ['DATABASE_URL']

#connect to database
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
try:
    cursor.execute("SELECT * from historical_prices")
except psycopg2.Error as e:
    print e.pgerror
    pass

print(cursor.fetchall())

helper = Helper()
url = helper.getPriceHistoryUrl("AMZN", "XNAS")

#response = urllib2.urlopen(url)
#cr = csv.reader(response)

#for row in cr:
#    print(row)
