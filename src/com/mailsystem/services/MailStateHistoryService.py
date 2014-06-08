'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import MailStateHistory

class MailStateHistoryService:
    @staticmethod
    def listAll(database):
        return database.session().query(MailStateHistory).all()
    
    @staticmethod
    def selectById(database, idmail):
        return database.session().query(MailStateHistory).get(idmail)
    
    @staticmethod
    def add(database, idstate, idmail):        
        insertStatement = database.statement(MailStateHistory, "insert")\
                                    .values(idstate = idstate,
                                            idmail = idmail)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1