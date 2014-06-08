from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Sequence, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'
    idDepartment = Column(Integer, Sequence('department_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)

class User(Base):
    __tablename__ = 'user'
    idUser = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    idDepartment = Column(Integer, ForeignKey('department.idDepartment'), nullable=False)
    department = relationship(Department,
                              backref=backref('users',
                                              uselist=True,
                                              cascade='all'))

class Address(Base):
    __tablename__ = 'address'
    idAddress = Column(Integer, Sequence('address_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)

class UserAddress(Base):
    __tablename__ = 'userAddress'
    idUserAddress = Column(Integer, Sequence('user_address_id_seq'), primary_key=True)
    idAddress = Column(Integer, ForeignKey('address.idAddress'), nullable=False)
    address = relationship(Address,
                           backref=backref('addresses',
                                           uselist=True))
    idUser= Column(Integer, ForeignKey('user.idUser'), nullable=False)
    user = relationship(User,
                        backref=backref('addresses',
                                        uselist=True))
 
class State(Base):
    __tablename__ = 'state'
    idState = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)

class Mail(Base):
    __tablename__ = 'mail'
    idMail = Column(Integer, Sequence('mail_id_seq'), primary_key=True)
    idState = Column(Integer, ForeignKey('state.idState'), nullable=False)
    state = relationship(State)
    idDestinationUserAddress = Column(Integer, ForeignKey('userAddress.idUserAddress'), nullable=False)
    destination = relationship(UserAddress, foreign_keys = 'Mail.idDestinationUserAddress')
    idSenderUserAddress = Column(Integer, ForeignKey('userAddress.idUserAddress'), nullable=False)
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

class Schema:
    @staticmethod
    def create(engine):
        Base.metadata.create_all(engine)