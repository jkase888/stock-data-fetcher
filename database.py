import psycopg2
#from database_private import DatabasePrivateSettings

class DatabaseGateway():

    def __init__(self):
#        if (env == "LOCAL"):
#            self.DATABASE_URL = DatabasePrivateSettings.DATABASE_URL
#        else:
            self.DATABASE_URL = os.environ['DATABASE_URL']

    def connect(self):
        self.connection = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insertHistroicalPrice(self, row, symbolandExchange):
        try:
            if (self.connection != 0):
                self.connect()
            self.cursor.execute("INSERT INTO historical_prices VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[0], symbolandExchange, row[1], row[2], row[3], row[4], row[5]))
            self.commit()
            return False
        except psycopg2.Error as e:
            print(e.pgcode + "\n" + e.pgerror)
            self.connection.close()
            return True
