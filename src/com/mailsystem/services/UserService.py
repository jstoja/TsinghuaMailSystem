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
        s = database.session()
        user = User(name=name, email=email, department=department)
        s.add(user)
        s.commit()
