'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import UserAddress
from src.com.mailsystem.services.UserService import UserService

class UserAddressService:    
    @staticmethod
    def selectById(db_users, idua):
        return db_users.session().query(UserAddress).get(idua)
    
    @staticmethod
    def listByUser(db_users, iduser):
        user = UserService.selectById(db_users, iduser)
        return user.addresses
    
    @staticmethod
    def add(db_users, idaddress, iduser):
        insertStatement = db_users.statement(UserAddress, "insert")\
                                    .values(idaddress = idaddress,
                                            iduser = iduser)
        result = db_users.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(db_users, idua, idaddress, iduser):
        updateStatement = db_users.statement(UserAddress, "update")\
                                    .where(UserAddress.__table__.c.iduseraddress == idua)\
                                    .values(idaddress = idaddress,
                                            iduser = iduser)
        result = db_users.execute(updateStatement)
        return result is not None