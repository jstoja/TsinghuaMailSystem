'''
Created on 8 juin 2014

@author: Romain
'''

from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory, Schema
import sys, os, ast

class Database:
    def __init__(self, name, user = 'root', password = 'root', host = 'localhost', port = 3306):
        self.name = name
        self.logfile = open(name + '.logfile', 'a+')
        self.mustRecover = os.stat(name + '.logfile').st_size > 0
        self.recoverHandler = { "INSERT": self.insert }
        
        self.engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@' + host +':' + str(port) + '/' + name, echo = False)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Schema.create(self.engine)
    
    def session(self):
        return self.session()

    def insert(self, table, **kwargs):
        statement = table.__table__.insert().values(kwargs)
        statement.bind = self.engine
        
        try:
            tablename = str(table).split('\'')[1].split('.')[-1]
            return self.__execute("INSERT " + tablename, statement)
        except:
            return False
    
    def __recover(self):
        try:
            self.logfile.seek(0)
            for line in self.logfile:
                data = line.split(' ', 2)
                print('Recover statement ' + line)
                table = getattr(sys.modules[__name__], data[1])
                mdict = ast.literal_eval(data[2])
                self.recoverHandler[data[0]](table, **mdict)
            self.logfile.truncate(0)
            self.mustRecover = False
        except:
            print("Unexpected error:", sys.exc_info()[0])
            pass
        
    def __execute(self, tolog, statement):
        if self.mustRecover:
            self.__recover()
            if self.mustRecover:
                return False
        try:
            raise
            conn = self.engine.connect()
            conn.execute(statement)
            conn.close()
            return True
        except:
            #Log
            print(tolog + " " + str(statement.compile().params), file=self.logfile)
            print('Execute error on db ' + self.name)
            self.mustRecover = True
            return False    