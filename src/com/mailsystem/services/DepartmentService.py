'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Department

class DepartmentService:
    @staticmethod
    def listAll(database):
        return database.session().query(Department).all()
    
    @staticmethod
    def selectById(database, iddep):
        return database.session().query(Department).get(iddep)
    
    @staticmethod
    def add(database, name):
        insertStatement = database.statement(Department, "insert").values(name = name)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(database, iddep, name):
        updateStatement = database.statement(Department, "update").where(Department.__table__.c.iddepartment == iddep).values(name = name)
        result = database.execute(updateStatement)
        return result is not None
