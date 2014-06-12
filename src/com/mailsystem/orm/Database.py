'''
Created on 8 juin 2014

@author: Romain
'''

from __future__ import print_function
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.orm import sessionmaker
from src.com.mailsystem.orm import Schema
import sys, os, ast, re

class Database:
    def __init__(self, name, uri = "mysql+mysqlconnector://root:root@localhost:3306"):
        self.name = name
        self.logfile = open(name + '.logfile', 'a+')
        self.mustRecover = os.stat(name + '.logfile').st_size > 0
        self.recovering = False
        self.logRegex = re.compile(r"\%\(([^\)]+)\)s")

        if uri.split(':')[0].split('+')[0] in ["mysql", "postgresql"]:
            self.engine = create_engine(uri, encoding='utf8')
            try:
                self.engine.execute("CREATE DATABASE IF NOT EXISTS `" + name + "` CHARACTER SET utf8 COLLATE utf8_general_ci") #create db
            except:
                pass
        self.engine = create_engine(uri + '/' + name, encoding='utf8')

        self.session = sessionmaker(expire_on_commit=False)
        self.session.configure(bind=self.engine)
        Schema.create(self.engine)

    def session(self):
        return self.session()

    def statement(self, table, func):
        statement = getattr(table.__table__, func)()
        statement.bind = self.engine
        return statement

    def __recover(self):
        try:
            self.recovering = True
            self.logfile.seek(0)
            while True:
                line1 = self.logfile.readline()
                line2 = self.logfile.readline()
                if not line2: break  # EOF
                print('Recover statement ' + line1 + line2)
                mdict = ast.literal_eval(line2)
                s = text(line1)
                self.execute(s, **mdict)
            self.logfile.truncate(0)
            self.mustRecover = False
            self.recovering = False
            print('Successfully recovered \'' + self.name + '\'')
        except:
            self.mustRecover = True
            self.recovering = False
            print("Failed recovery of '" + self.name + "': ", sys.exc_info()[0], " - ", sys.exc_info()[1])

    def execute(self, statement, **kwargs):
        if self.mustRecover and self.recovering == False:
            self.__recover()
            if self.mustRecover:
                print(self.logRegex.sub(r":\1", str(statement)), file=self.logfile)
                print(str(statement.compile().params), file=self.logfile)
                return None
        try:
            conn = self.engine.connect()
            result = conn.execute(statement, kwargs)
            conn.close()
            return result
        except IntegrityError, ProgrammingError:
            print("ERROR: " + self.name + ": ", sys.exc_info()[1])
        except:
            if self.recovering:
                raise
            #Log
            print(self.logRegex.sub(r":\1", str(statement)), file=self.logfile)
            print(str(statement.compile().params), file=self.logfile)
            print("FAIL: " + self.name + ": ", sys.exc_info()[1])
            self.mustRecover = True
            return None
