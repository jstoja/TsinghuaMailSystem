'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import MailStateHistory

class MailStateHistoryService:
    @staticmethod
    def selectById(db_department, idmail):
        return db_department.session().query(MailStateHistory).get(idmail)
    
    @staticmethod
    def add(db_department, idstate, idmail):        
        insertStatement = db_department.statement(MailStateHistory, "insert")\
                                    .values(idstate = idstate,
                                            idmail = idmail)
        result = db_department.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1