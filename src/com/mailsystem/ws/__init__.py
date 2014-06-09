from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database

from src.com.mailsystem.services.AddressService import AddressService
from src.com.mailsystem.services.DepartmentService import DepartmentService
from src.com.mailsystem.services.MailService import MailService
from src.com.mailsystem.services.MailStateHistoryService import MailStateHistoryService
from src.com.mailsystem.services.StateService import StateService
from src.com.mailsystem.services.UserAddressService import UserAddressService
from src.com.mailsystem.services.UserService import UserService
import src.com.mailsystem.codes as codes

db_users = Database('mailsystem_users')
db_d1 = Database('mailsystem_d1')
databases = { 'users': db_users,
              'D1': db_d1 }

codes.codes = { "01": "D1" }
codes.rev_codes = { "D1": "01" }


a1 = AddressService.add(db_users, "A1")
a2 = AddressService.add(db_users, "A2")
d1 = DepartmentService.add(db_users, "D1")
s1 = StateService.add(db_users, "S1")
s2 = StateService.add(db_users, "S2")
s3 = StateService.add(db_users, "S3")
u1 = UserService.add(db_users, 2013400576, "U1", "u1@u1.u1", d1)
ua1 = UserAddressService.add(db_users, a1, u1)
ua2 = UserAddressService.add(db_users, a2, u1)
bc = MailService.add(databases, s1, ua1, ua2)

las = UserAddressService.listByUser(db_users, u1)

print las

print a1
print d1
print s1
print u1
print ua1
print bc

print MailService.update(databases, bc, s2)
print MailService.update(databases, bc, s3)
print MailService.update(databases, bc, s1)

#db1.update(Department, Department.__table__.c.idDepartment == d1.idDepartment, name = "CS")
#db1.insert(UserAddress, idAddress = 1, idUser = 1)
#db1.execute(db1.statement(Department, "update").where(Department.__table__.c.idDepartment == d1.idDepartment).values(name = "CS"))
#db1.execute(db1.statement(UserAddress, "insert").values(idaddress = 1, iduser = 1))
#ins = db1.getStatement(UserAddress, 'insert').values(idAddress = 1, idUser = 1)
#db1.execute(ins)