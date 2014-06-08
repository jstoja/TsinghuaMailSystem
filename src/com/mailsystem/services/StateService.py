'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import State

class StateService:
    @staticmethod
    def listAll(database):
        return database.session().query(State).all()
    
    @staticmethod
    def selectById(database, idstate):
        return database.session().query(State).get(idstate)
    
    @staticmethod
    def add(database, name):
        insertStatement = database.statement(State, "insert").values(name = name)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(database, idstate, name):
        updateStatement = database.statement(State, "update").where(State.__table__.c.idstate == idstate).values(name = name)
        result = database.execute(updateStatement)
        return result is not None
