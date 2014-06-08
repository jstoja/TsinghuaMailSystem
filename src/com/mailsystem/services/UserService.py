from src.com.mailsystem.orm import User

class UserService:
    @staticmethod
    def listAll(database):
        return database.session().query(User).all()

    @staticmethod
    def selectById(database, iduserthu):
        return database.session().query(User).get(iduserthu)

    @staticmethod
    def add(database, name, email, department):
        insertStatement = database.statement(User, "insert").values(name = name, email = email, iddepartment = department.iddepartment)
        result = database.execute(insertStatement)
        if result is not None:
            return result.inserted_primary_key
        return -1
    
    @staticmethod
    def update(database, iduserthu, name, email, department):
        updateStatement = database.statement(User, "update").where(User.__table__.c.iduserthu == iduserthu).values(name = name, email = email, iddepartment = department.iddepartment)
        result = database.execute(updateStatement)
        return result is not None
