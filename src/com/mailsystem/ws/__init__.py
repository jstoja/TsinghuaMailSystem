from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database

db1 = Database('mailsystem_1')

'''
d1 = Department(name="CS")
d2 = Department(name="PHY")
s1 = State(name = "Deposited")
s2 = State(name = "Post-Transit")
s3 = State(name = "Waiting at address")
s4 = State(name = "Received")
u1 = User(name="u1", email="u1@cs.cs", department=d1)
u2 = User(name="u2", email="u2@cs.cs", department=d1)
u3 = User(name="u3", email="u3@cs.cs", department=d1)
u4 = User(name="u4", email="u4@cs.cs", department=d1)
u5 = User(name="u5", email="u5@phy.phy", department=d2)
u6 = User(name="u6", email="u6@phy.phy", department=d2)
u7 = User(name="u7", email="u7@phy.phy", department=d2)
u8 = User(name="u8", email="u8@phy.phy", department=d2)
a1 = Address(name="CS lab")
a2 = Address(name="PHY lab")
a3 = Address(name="Zijing 19")
a4 = Address(name="Zijing 20")
ua1 = UserAddress(address = a1, user = u1)
ua2 = UserAddress(address = a1, user = u2)
ua3 = UserAddress(address = a1, user = u3)
ua4 = UserAddress(address = a1, user = u4)
ua5 = UserAddress(address = a2, user = u5)
ua6 = UserAddress(address = a2, user = u6)
ua7 = UserAddress(address = a2, user = u7)
ua8 = UserAddress(address = a2, user = u8)
ua9 = UserAddress(address = a3, user = u1)
ua10 = UserAddress(address = a4, user = u2)
ua11 = UserAddress(address = a3, user = u3)
ua12 = UserAddress(address = a4, user = u4)
ua13 = UserAddress(address = a3, user = u5)
ua14 = UserAddress(address = a4, user = u6)
ua15 = UserAddress(address = a3, user = u7)
ua16 = UserAddress(address = a4, user = u8)

s = db1.session()
s.add(d1)
s.add(d2)
s.add(s1)
s.add(s2)
s.add(s3)
s.add(s4)
s.add(u1)
s.add(u2)
s.add(u3)
s.add(u4)
s.add(u5)
s.add(u6)
s.add(u7)
s.add(u8)
s.add(a1)
s.add(a2)
s.add(a3)
s.add(a4)
s.add(ua1)
s.add(ua2)
s.add(ua3)
s.add(ua4)
s.add(ua5)
s.add(ua6)
s.add(ua7)
s.add(ua8)
s.add(ua9)
s.add(ua10)
s.add(ua11)
s.add(ua12)
s.add(ua13)
s.add(ua14)
s.add(ua15)
s.add(ua16)

s.commit()
'''

ins = db1.getStatement(UserAddress, 'insert').values(idAddress = 1, idUser = 1)
db1.execute(ins)