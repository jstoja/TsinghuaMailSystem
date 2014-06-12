'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Department

class DepartmentService:
    @staticmethod
    def listAll(db_users):
        s = db_users.session()
        ret = s.query(Department).all()
        s.close()
        return ret
    
    @staticmethod
    def selectById(db_users, iddep):
        s = db_users.session()
        ret = s.query(Department).get(iddep)
        s.close()
        return ret
    
    @staticmethod
    def add(db_users, name):
        insertStatement = db_users.statement(Department, "insert")\
                                    .values(name = name)
        result = db_users.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1
    
    @staticmethod
    def update(db_users, iddep, name):
        updateStatement = db_users.statement(Department, "update")\
                                    .where(Department.__table__.c.iddepartment == iddep)\
                                    .values(name = name)
        result = db_users.execute(updateStatement)
        return result is not None
