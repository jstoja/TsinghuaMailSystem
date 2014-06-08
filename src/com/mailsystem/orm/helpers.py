'''
Created on 8 juin 2014

@author: julienbordellier
'''

# encode=utf8

from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database

def add_mail(db_sender, db_receiver, sender, receiver, state):
    s = db_sender.session()
    s.add(Mail(state=state, destination=receiver, sender=sender))
    s.commit()
    s = db_receiver.session()
    s.add(Mail(state=state, destination=receiver, sender=sender))
    s.commit()    