from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Sequence, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import UniqueConstraint

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'
    iddepartment = Column(Integer, Sequence('department_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)

class User(Base):
    __tablename__ = 'userthu'
    iduserthu = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    studentnumber = Column(Integer, unique=True)
    name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    #iddepartment = Column(Integer, nullable=False)
    iddepartment = Column(Integer, ForeignKey('department.iddepartment'), nullable=False)
    department = relationship(Department,
                              backref=backref('users',
                                              uselist=True,
                                              cascade='all'))

class Address(Base):
    __tablename__ = 'address'
    idaddress = Column(Integer, Sequence('address_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)

class UserAddress(Base):
    __tablename__ = 'useraddress'
    iduseraddress = Column(Integer, Sequence('user_address_id_seq'), primary_key=True)
    #idaddress = Column(Integer, nullable=False)
    idaddress = Column(Integer, ForeignKey('address.idaddress'), nullable=False)
    address = relationship(Address,
                           backref=backref('addresses',
                                           uselist=True))
    #iduser = Column(Integer, nullable=False)
    iduser = Column(Integer, ForeignKey('userthu.iduserthu'), nullable=False)
    user = relationship(User,
                        backref=backref('addresses',
                                        uselist=True))
 
class State(Base):
    __tablename__ = 'state'
    idstate = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)

class Mail(Base):
    __tablename__ = 'mail'
    idmail = Column(Integer, Sequence('mail_id_seq'), primary_key=True)
    barcode = Column(String(20), unique=True)
    idstate = Column(Integer, nullable=False)
    #idstate = Column(Integer, ForeignKey('state.idstate'), nullable=False)
    #state = relationship(State)
    idreceiveruseraddress = Column(Integer, nullable=False)
    #idreceiveruseraddress = Column(Integer, ForeignKey('useraddress.iduseraddress'), nullable=False)
    #destination = relationship(UserAddress, foreign_keys='Mail.idreceiveruseraddress')
    idsenderuseraddress = Column(Integer, nullable=False)
    #idsenderuseraddress = Column(Integer, ForeignKey('useraddress.iduseraddress'), nullable=False)
    #sender = relationship(UserAddress, foreign_keys='Mail.idsenderuseraddress')

class MailStateHistory(Base):
    __tablename__ = 'mailstatehistory'
    idstate = Column(Integer, primary_key=True)
    #idstate = Column(Integer, ForeignKey('state.idstate'), primary_key=True)
    #state = relationship(State)
    idmail = Column(Integer, ForeignKey('mail.idmail'), primary_key=True)
    mail = relationship(Mail,
                        backref=backref("statehistory",
                                        uselist=True,
                                        cascade="all, delete-orphan"))
    date = Column(DateTime, primary_key=True, default=func.now())

class Schema:
    @staticmethod
    def create(engine):
        Base.metadata.create_all(engine)
