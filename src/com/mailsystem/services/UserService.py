from src.com.mailsystem.orm import User

class UserService:
    @staticmethod
    def listAll(db_users):
        return db_users.session().query(User).all()

    @staticmethod
    def selectById(db_users, iduserthu):
        return db_users.session().query(User).get(iduserthu)

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
