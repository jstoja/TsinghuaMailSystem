'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Department

class DepartmentService:
    @staticmethod
    def listAll(database):
        return database.session().query(Department).all()