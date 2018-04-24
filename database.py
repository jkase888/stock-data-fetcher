import psycopg2
import os
import traceback
from database_private import DatabasePrivateSettings

class DatabaseGateway():

    def __init__(self, env):
        if (env == "LOCAL"):
            self.DATABASE_URL = DatabasePrivateSettings.DATABASE_URL
            pass
        else:
            self.DATABASE_URL = os.environ['DATABASE_URL']

    def connect(self):
        self.connection = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        self.cursor = self.connection.cursor()
        self.isClosed = False

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
        self.isClosed = True

    def fetchall(self):
        return self.cursor.fetchall()

    def getCursor(self):
        return self.cursor

    def insertHistroicalPrice(self, row, symbolandExchange):
        try:
            if (self.isClosed is True):
                self.connect()
            self.cursor.execute("INSERT INTO historical_prices VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[0], symbolandExchange, row[1], row[2], row[3], row[4], row[5]))
            self.commit()
            return 0
        except Exception as e:
            #print(e.pgcode + "\n" + e.pgerror)
            print(traceback.format_exc())
            self.close()
            return -1

    def executeSQL(self, statement):
        try:
            if(self.isClosed is True):
                self.connect()
            self.cursor.execute(statement)
            self.commit()
            return 0
        except Exception as e:
            print(traceback.format_exc())
            self.close()
            return -1
