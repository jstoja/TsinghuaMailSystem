from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database

from src.com.mailsystem.services.DepartmentService import DepartmentService
from src.com.mailsystem.services.UserService import UserService

db1 = Database('mailsystem_1')

d1 = DepartmentService.selectById(db1, 1)
print d1
id = UserService.add(db1, "Toto", "toto#t", d1)
print id
u1 = UserService.selectById(db1, id)
print u1

print UserService.update(db1, u1.iduserthu, "blablabla", "blablabla@mail.com", d1)


#db1.update(Department, Department.__table__.c.idDepartment == d1.idDepartment, name = "CS")
#db1.insert(UserAddress, idAddress = 1, idUser = 1)
#db1.execute(db1.statement(Department, "update").where(Department.__table__.c.idDepartment == d1.idDepartment).values(name = "CS"))
#db1.execute(db1.statement(UserAddress, "insert").values(idaddress = 1, iduser = 1))
#ins = db1.getStatement(UserAddress, 'insert').values(idAddress = 1, idUser = 1)
#db1.execute(ins)