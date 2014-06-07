from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'
    idDepartment = Column(Integer, primary_key=True)
    name = Column(String)

class User(Base):
    __tablename__ = 'user'
    idUser = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    idDepartment = Column(Integer, ForeignKey('department.idDepartment'))
    department = relationship(Department,
                              backref=backref('users',
                                              uselist=True,
                                              cascade='all'))

class Address(Base):
    __tablename__ = 'address'
    idAddress = Column(Integer, primary_key=True)
    name = Column(String)

class UserAddress(Base):
    __tablename__ = 'userAddress'
    idUserAddress = Column(Integer, primary_key=True)
    idAddress = Column(Integer, ForeignKey('address.idAddress'))
    address = relationship(Address,
                           backref=backref('addressses',
                                           uselist=True))
    idUser= Column(Integer, ForeignKey('user.idUser'))
    user = relationship(User,
                        backref=backref('addressses',
                                        uselist=True))
 
class State(Base):
    __tablename__ = 'state'
    idState = Column(Integer, primary_key=True)
    name = Column(String)

class Mail(Base):
    __tablename__ = 'mail'
    idMail = Column(Integer, primary_key=True)
    idState = Column(Integer, ForeignKey('state.idState'))
    state = relationship(State)
    idDestinationUserAddress = Column(Integer, ForeignKey('userAddress.idUserAddress'))
    destination = relationship(UserAddress, foreign_keys = 'Mail.idDestinationUserAddress')
    idSenderUserAddress = Column(Integer, ForeignKey('userAddress.idUserAddress'))
    sender = relationship(UserAddress, foreign_keys = 'Mail.idSenderUserAddress')

class MailStateHistory(Base):
    __tablename__ = 'mailStateHistory'
    idState = Column(Integer, ForeignKey('state.idState'), primary_key=True)
    state = relationship(State)
    idMail= Column(Integer, ForeignKey('mail.idMail'), primary_key=True)
    mail = relationship(Mail,
                        backref=backref("stateHistory",
                                        uselist=True,
                                        cascade="all, delete-orphan"))
    date = Column(DateTime, primary_key=True, default=func.now())

from sqlalchemy import create_engine
engine = create_engine('sqlite:///db1sqlite')
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)