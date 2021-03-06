'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import State

class StateService:
    @staticmethod
    def listAll(db_users):
        s = db_users.session()
        ret = s.query(State).all()
        s.close()
        return ret
    
    @staticmethod
    def selectById(db_users, idstate):
        s = db_users.session()
        ret = s.query(State).get(idstate)
        s.close()
        return ret
    
    @staticmethod
    def add(db_users, name):
        insertStatement = db_users.statement(State, "insert")\
                                    .values(name = name)
        result = db_users.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(db_users, idstate, name):
        updateStatement = db_users.statement(State, "update")\
                                    .where(State.__table__.c.idstate == idstate)\
                                    .values(name = name)
        result = db_users.execute(updateStatement)
        return result is not None
