'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Address

class AddressService:
    @staticmethod
    def listAll(database):
        return database.session().query(Address).all()
    
    @staticmethod
    def selectById(database, idadd):
        return database.session().query(Address).get(idadd)
    
    @staticmethod
    def add(database, name):
        insertStatement = database.statement(Address, "insert").values(name = name)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(database, idadd, name):
        updateStatement = database.statement(Address, "update").where(Address.__table__.c.idaddress == idadd).values(name = name)
        result = database.execute(updateStatement)
        return result is not None