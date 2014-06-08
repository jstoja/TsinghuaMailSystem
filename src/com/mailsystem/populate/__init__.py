# coding=utf8
from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database

departments = [
    Department(name="PHY"),
    Department(name="CH"),
    Department(name="LAW"),
    Department(name="FI"),
    Department(name="CS"),
    Department(name="ECO"),
    Department(name="ART"),
    Department(name="ENV"),
    Department(name="ADM")
]
#"physics", "chemistry", "law", "finance", "computer science", "economy", "art", "environment", "administration"]

states = [
    State(name = "Deposited"),
    State(name = "Post-Transit"),
    State(name = "Waiting at address"),
    State(name = "Received")
]
        
# chinese_names = [
#     "张伟", "王伟","王芳","李伟","王秀英","李秀英","李娜","张秀英","刘伟","张敏",
#     "李静","张丽","王静","王丽","李强","张静","李敏","王敏","王磊","李军","刘洋",
#     "王勇","张勇","王艳","李杰","张磊","王强","王军","张杰","李娟","张艳","张涛",
#     "王涛","李明","李艳","王超","李勇","王娟","刘杰","王秀兰","李霞","刘敏","张军",
#     "李丽","张强","王平","王刚","王杰","李桂英","刘芳"
# ] 

chinese_names = ["lina","mia","lifei","hefei"]

adresses = [
    Address(name="Zijing 1"), 
    Address(name="Zijing 2"),
    Address(name="Zijing 3"),
    Address(name="Zijing 4"),
    Address(name="Zijing 5"),
    Address(name="Zijing 6"),
    Address(name="Zijing 7"),
    Address(name="Zijing 8"),
    Address(name="Zijing 9"),
    Address(name="Zijing 10"),
    Address(name="Zijing 11"),
    Address(name="Zijing 12"),
    Address(name="Zijing 13"),
    Address(name="Zijing 14"),
    Address(name="Zijing 15"),
    Address(name="Zijing 16"),
    Address(name="Zijing 17"),
    Address(name="Zijing 18"),
    Address(name="Zijing 19"),
    Address(name="Zijing 20"),
    Address(name="Zijing 21"),
    Address(name="Zijing 22"),
    Address(name="Zijing 23"),
    Address(name="Zijing 24"),
    Address(name="Lab of PHY"),
    Address(name="Lab of CH"),
    Address(name="Lab of LAW"),
    Address(name="Lab of FI"),
    Address(name="Lab of CS"),
    Address(name="Lab of ECO"),
    Address(name="Lab of ART"),
    Address(name="Lab of ENV"),
    Address(name="Lab of ADM")
]


db_users = Database('thumailusers', 'thumail', 'thumail', 'localhost', 5432)
s = db_users.session()
for adress in adresses:
    s.add(adress)

email_shift = 0
for department in departments:
    s.add(department)
    for username in chinese_names:
        mail = "w_" + str(email_shift) + "@mail.tsinghua.edu.cn"
        email_shift = email_shift + 1
        u = User(name=username.decode('utf8'), email=mail, department=department)
        s.add(u)
        for adress in adresses:
            s.add(UserAddress(address=adress, user=u))
s.commit()
print "Finish"
