'''
Created on 8 juin 2014

@author: Romain
'''

'''
Created on 8 juin 2014

@author: Romain
'''

from src.com.mailsystem.orm import Mail
from src.com.mailsystem.services.UserAddressService import UserAddressService
from src.com.mailsystem.services.MailStateHistoryService import MailStateHistoryService

class MailService:
    @staticmethod
    def listAll(database):
        return database.session().query(Mail).all()
    
    @staticmethod
    def selectById(database, idmail):
        return database.session().query(Mail).get(idmail)
    
    @staticmethod
    def selectByBarcode(database, barcode):
        return database.session().query(Mail).filter(Mail.barcode == barcode).scalar()
    
    @staticmethod
    def __findDatabaseForUserAddress(database, iduseraddress):
        ua = UserAddressService.selectById(database, iduseraddress)
        if ua is None:
            return None
        #TODO
        #return databases[ua.user.department.name]
        return database
    
    @staticmethod
    def __genBarcode():
        #TODO
        return "01-5901234123457"
    
    @staticmethod
    def add(database, idstate, idsenderua, iddestinationua):        
        dbsender = MailService.__findDatabaseForUserAddress(database, idsenderua)
        dbreceiver = MailService.__findDatabaseForUserAddress(database, iddestinationua)
        if dbsender is None or dbreceiver is None:
            return None
        
        generatedBarcode = MailService.__genBarcode()
        insertStatement = database.statement(Mail, "insert")\
                                    .values(barcode = generatedBarcode,
                                            idstate = idstate,
                                            iddestinationuseraddress = iddestinationua,
                                            idsenderuseraddress = idsenderua)
        # Duplicate the data in the sender database
        result = dbsender.execute(insertStatement)
        if result is not None:
            idsenderdb = result.inserted_primary_key[0]
            MailStateHistoryService.add(dbsender, 1, idsenderdb)
        if dbsender == dbreceiver:
            return generatedBarcode
        # And in the receiver database
        result = dbreceiver.execute(insertStatement)
        if result is not None:
            idreceiverdb = result.inserted_primary_key[0]
            MailStateHistoryService.add(dbreceiver, 1, idreceiverdb)
        return generatedBarcode
    
    @staticmethod
    def update(database, barcode, idstate):
        currentMail = MailService.selectByBarcode(database, barcode)
        if currentMail is None:
            return None
        
        dbsender = MailService.__findDatabaseForUserAddress(database, currentMail.idsenderuseraddress)
        dbreceiver = MailService.__findDatabaseForUserAddress(database, currentMail.iddestinationuseraddress)
        if dbsender is None or dbreceiver is None:
            return None
        
        updateStatement = database.statement(Mail, "update")\
                                    .where(Mail.__table__.c.barcode == barcode)\
                                    .values(idstate = idstate)
        MailStateHistoryService.add(dbsender, currentMail.idstate, currentMail.idmail)
        r1 = dbsender.execute(updateStatement)
        r2 = dbreceiver.execute(updateStatement)
        return r1 is not None and r2 is not None
