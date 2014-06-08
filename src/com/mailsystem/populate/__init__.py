'''
Created on 8 juin 2014

@author: julienbordellier
'''


# coding=utf8
from datetime import date
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
        
chinese_names = [
    "张伟", "王伟","王芳","李伟","王秀英","李秀英","李娜","张秀英","刘伟","张敏",
    "李静","张丽","王静","王丽","李强","张静","李敏","王敏","王磊","李军","刘洋",
    "王勇","张勇","王艳","李杰","张磊","王强","王军","张杰","李娟","张艳","张涛",
    "王涛","李明","李艳","王超","李勇","王娟","刘杰","王秀兰","李霞","刘敏","张军",
    "李丽","张强","王平","王刚","王杰","李桂英","刘芳"
] 

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

def populate_user_db(user_database, session):
    email_shift = 0
    users = []
    for adress in adresses:
        session.add(adress)
    for department in departments:
        session.add(department)
        for username in chinese_names:
            mail = "w_" + str(email_shift) + "@mail.tsinghua.edu.cn"
            email_shift = email_shift + 1
            u = User(name=username.decode('utf8'), email=mail, department=department)
            users.append(u)
            session.add(u)
            for adress in adresses:
                session.add(UserAddress(address=adress, user=u))
    return users
    

def create_states(db, users):
    s = db.session()
    for state in states:
        s.add(state)
    s.commit()
    
def add_mail(db_sender, db_receiver, sender, receiver, state):
    s = db_sender.session()
    s.add(Mail(state=state, destination=receiver, sender=sender))
    s.commit()
    s = db_receiver.session()
    s.add(Mail(state=state, destination=receiver, sender=sender))
    s.commit()

def add_history(db_sender, db_receiver, state, mail, date):
    s = db_sender.session()
    s.add(Mail(state=state, mail=mail, date=date))
    s.commit()
    s = db_receiver.session()
    s.add(Mail(state=state, mail=mail, date=date))
    s.commit()

def populate_departments_dbs(departments_dbs, users):
    for db_name, db in departments_dbs:
        if db_name == 'users':
            continue
        else:
            create_states(db)
    for sender in users:
        for receiver in users:
            sender_db = departments_dbs[sender.department]
            receiver_db = departments_dbs[receiver.department] 
            m = add_mail(sender_db, receiver_db, sender, receiver, states[0])
            for state in states:
                if state == states[0]:
                    continue
                else:
                    add_history(sender_db, receiver_db, state, m, date.today())

def populate_db(databases):
    s = db_users.session()
    users = populate_user_db(databases['users'], s)
    populate_departments_dbs(databases, users)
    s.commit()
    print "Finish populating the DBs"
