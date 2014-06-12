'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Address

class AddressService:
    @staticmethod
    def listAll(db_users):
        s = db_users.session()
        ret = s.query(Address).all()
        s.close()
        return ret
    
    @staticmethod
    def selectById(db_users, idadd):
        s = db_users.session()
        ret = s.query(Address).get(idadd)
        s.close()
        return ret
    
    @staticmethod
    def add(db_users, name):
        insertStatement = db_users.statement(Address, "insert")\
                                    .values(name = name)
        result = db_users.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(db_users, idadd, name):
        updateStatement = db_users.statement(Address, "update")\
                                    .where(Address.__table__.c.idaddress == idadd)\
                                    .values(name = name)
        result = db_user.execute(updateStatement)
        return result is not None