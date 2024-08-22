import mysql.connector

class BDController :
    def getconnection():
        return mysql.connector.connect(user='root', password='', host='127.0.0.1')
