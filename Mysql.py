#coding=utf-8

import pymysql

class Mysql:
    database = {
            'host': 'localhost', 
            'user': 'root', 
            'passwd': '123456', 
            'db': 'we', 
            'charset': 'utf8mb4', 
            'port': 3306
            }

    connector = None
    cursor = None

    def __init__(self):
        self.connectMysql()
        self.cursor = self.connector.cursor()
        return

    def connectMysql(self):
        try:
            self.connector = pymysql.connect(host=self.database['host'], user=self.database['user'], passwd=self.database['passwd'], db=self.database['db'], charset=self.database['charset'], port=self.database['port'])
        except Exception:
            print('链接数据库失败')
            print(Exception)

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.connector.commit()
        except Exception:
            self.connector.rollback()
            print('sql语句执行失败')
            print(Exception)
            print(sql)


    def query(self, sql):
        try:
            result = self.cursor.execute(sql)
            return result
        except Exception:
            print('sql语句执行失败')
            print(Exception)
            print(sql)

    def getOne(self, sql):
        sql = sql + ' limit 1'
        self.query(sql)
        return self.cursor.fetchone()
        

    def closeConnect(self):
        self.cursor.close()
        self.connector.close()
