from src.com.mailsystem.orm import User


class UserService:
    @staticmethod
    def listAll(database):
        return database.session().query(User).all()

    @staticmethod
    def selectById(database, id):
        return database.session().query(User).get(id)
