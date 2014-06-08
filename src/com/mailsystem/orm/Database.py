'''
Created on 8 juin 2014

@author: Romain
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.com.mailsystem.orm import Schema

class Database:
    def __init__(self, name, user = 'root', password = 'root', host = 'localhost', port = 3306):
        self.name = name
        
        self.engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@' + host +':' + str(port) + '/' + name, echo = False)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Schema.create(self.engine)
    
    def session(self):
        return self.session()
    
    def getStatement(self, table, func):
        ins = getattr(table.__table__, func)()
        ins.bind = self.engine
        return ins
    
    def execute(self, statement):
        conn = self.engine.connect()
        print str(statement)
        print str(statement.compile().params)
        ret = conn.execute(statement)
        conn.close()
        return True