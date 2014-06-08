'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import UserAddress

class UserAddressService:
    @staticmethod
    def listAll(database):
        return database.session().query(UserAddress).all()
    
    @staticmethod
    def selectById(database, idua):
        return database.session().query(UserAddress).get(idua)
    
    @staticmethod
    def add(database, idaddress, iduser):
        insertStatement = database.statement(UserAddress, "insert").values(idaddress = idaddress, iduser = iduser)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(database, idua, idaddress, iduser):
        updateStatement = database.statement(UserAddress, "update").where(UserAddress.__table__.c.iduseraddress == idua).values(idaddress = idaddress, iduser = iduser)
        result = database.execute(updateStatement)
        return result is not None