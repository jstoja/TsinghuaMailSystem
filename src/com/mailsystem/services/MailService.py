'''
Created on 8 juin 2014

@author: Romain
'''

import uuid
from sqlalchemy.orm import eagerload_all
import src.com.mailsystem.codes as codes
from src.com.mailsystem.orm import Mail
from src.com.mailsystem.services.UserAddressService import UserAddressService
from src.com.mailsystem.services.MailStateHistoryService import MailStateHistoryService

class MailService:
    @staticmethod
    def selectById(db_department, idmail):
        s = db_department.session()
        ret = s.query(Mail).options(eagerload_all('statehistory')).get(idmail)
        s.close()
        return ret

    #@staticmethod
    #def selectByReceiverUserId(databases, receiver_id):
        #ua = UserAddressService.listByUser(databases)


    @staticmethod
    def selectByBarcode(db_department, barcode):
        s = db_department.session()
        ret = s.query(Mail).options(eagerload_all('statehistory')).filter(Mail.barcode == barcode).scalar()
        s.close()
        return ret

    @staticmethod
    def selectByUserAdresses(db_department, addresses):
        s = db_department.session()
        ret = db_department.session().query(Mail)\
            .filter(Mail.idreceiveruseraddress.in_(addresses)).all()
        s.close()
        return ret

    @staticmethod
    def __findDatabaseForUserAddress(databases, iduseraddress):
        ua = UserAddressService.selectById(databases['users'], iduseraddress)
        if ua is None:
            return None
        return (ua.user.department.name, databases[ua.user.department.name])

    @staticmethod
    def findDatabaseForBarcode(databases, barcode):
        return databases[str(codes.codes[barcode.split('-')[0]])]

    @staticmethod
    def __genBarcode(database_id):
        return (str(database_id) + "-" + str(uuid.uuid4()))

    @staticmethod
    def add(databases, idstate, idsenderua, idreceiverua):
        db_sender_name, db_sender = MailService.__findDatabaseForUserAddress(databases, idsenderua)
        db_receiver_name, db_receiver = MailService.__findDatabaseForUserAddress(databases, idreceiverua)
        if db_receiver is None or db_receiver is None:
            return None

        code = codes.rev_codes[db_sender_name]
        generatedBarcode = MailService.__genBarcode(code)
        insertStatement = db_sender.statement(Mail, "insert")\
                                    .values(barcode = generatedBarcode,
                                            idstate = idstate,
                                            idreceiveruseraddress = idreceiverua,
                                            idsenderuseraddress = idsenderua)
        # Duplicate the data in the sender database
        result = db_sender.execute(insertStatement)
        if result is not None:
            idsenderdb = result.inserted_primary_key[0]
            MailStateHistoryService.add(db_sender, 1, idsenderdb)
        if db_sender == db_receiver:
            return generatedBarcode
        # And in the receiver database
        result = db_receiver.execute(insertStatement)
        if result is not None:
            idreceiverdb = result.inserted_primary_key[0]
            MailStateHistoryService.add(db_receiver, 1, idreceiverdb)
        return generatedBarcode

    @staticmethod
    def update(databases, barcode, idstate):
        db_sender = MailService.findDatabaseForBarcode(databases, barcode)
        if db_sender is None:
            return None

        currentMail = MailService.selectByBarcode(db_sender, barcode)
        if currentMail is None:
            return None

        db_sender_name, db_sender = MailService.__findDatabaseForUserAddress(databases, currentMail.idsenderuseraddress)
        db_receiver_name, db_receiver = MailService.__findDatabaseForUserAddress(databases, currentMail.idreceiveruseraddress)
        if db_sender is None or db_receiver is None:
            return None

        updateStatement = db_sender.statement(Mail, "update")\
                                    .where(Mail.__table__.c.barcode == barcode)\
                                    .values(idstate = idstate)
        MailStateHistoryService.add(db_sender, currentMail.idstate, currentMail.idmail)
        r1 = db_sender.execute(updateStatement)
        if db_sender == db_receiver:
            return r1 is not None
        r2 = db_receiver.execute(updateStatement)
        return r1 is not None and r2 is not None
