from sqlalchemy.orm import eagerload_all
from src.com.mailsystem.orm import User

class UserService:
    @staticmethod
    def listAll(db_users):
        s = db_users.session()
        ret = s.query(User).all()
        s.close()
        return ret

    @staticmethod
    def selectById(db_users, iduserthu):
        s = db_users.session()
        ret = s.query(User).options(eagerload_all('addresses')).get(iduserthu)
        s.close()
        return ret

    @staticmethod
    def selectByStudentnumber(db_users, studentnumber):
        s = db_users.session()
        ret = s.query(User).options(eagerload_all('addresses')).filter(User.__table__.c.studentnumber == studentnumber).one()
        s.close()
        return ret

    @staticmethod
    def add(db_users, studentnumber, name, email, iddepartment):
        insertStatement = db_users.statement(User, "insert")\
                                    .values(studentnumber = studentnumber,
                                            name = name,
                                            email = email,
                                            iddepartment = iddepartment)
        result = db_users.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key[0]
        return -1

    @staticmethod
    def update(db_users, studentnumber, name, email, iddepartment):
        updateStatement = db_users.statement(User, "update")\
                                    .where(User.__table__.c.studentnumber == studentnumber)\
                                    .values(name = name,
                                            email = email,
                                            iddepartment = iddepartment)
        result = db_users.execute(updateStatement)
        return result is not None
