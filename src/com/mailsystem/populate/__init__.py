#!/usr/bin/env python
# coding: utf-8

'''
Created on 8 juin 2014

@author: julienbordellier
'''

import random
from datetime import date
from src.com.mailsystem.orm import Department, User, Address, UserAddress, State, Mail, MailStateHistory
from src.com.mailsystem.orm.Database import Database
from src.com.mailsystem.services.UserService import UserService
from src.com.mailsystem.services.AddressService import AddressService
from src.com.mailsystem.services.DepartmentService import DepartmentService
from src.com.mailsystem.services.UserAddressService import UserAddressService
from src.com.mailsystem.services.StateService import StateService
from src.com.mailsystem.services.MailService import MailService

departments = [
    "LAW",
    "CS",
    "ART",
    "ENV"#,
#     Department(name="PHY"),
#     Department(name="CH"),
#     Department(name="FI"),
#     Department(name="ECO"),
#     Department(name="ADM")
]
#"physics", "chemistry", "law", "finance", "computer science", "economy", "art", "environment", "administration"]

states = [
    "Deposited",
    "Post-Transit",
    "Waiting at address",
    "Received"
]

chinese_names = [
    "张伟", "王伟","王芳","李伟","王秀英","李秀英","李娜","张秀英","刘伟","张敏",
    "李静","张丽","王静","王丽","李强","张静","李敏","王敏","王磊","李军","刘洋",
    "王勇","张勇","王艳","李杰","张磊","王强","王军","张杰","李娟","张艳","张涛",
    "王涛","李明","李艳","王超","李勇","王娟","刘杰","王秀兰","李霞","刘敏","张军",
    "李丽","张强","王平","王刚","王杰","李桂英","刘芳"
]

adresses = [
    "Zijing 1",
    "Zijing 2",
    "Zijing 3",
    "Zijing 4",
    "Zijing 5",
    "Zijing 6",
    "Zijing 7",
    "Zijing 8",
    "Zijing 9",
    "Zijing 10",
    "Zijing 11",
    "Zijing 12",
    "Zijing 13",
    "Zijing 14",
    "Zijing 15",
    "Zijing 16",
    "Zijing 17",
    "Zijing 18",
    "Zijing 19",
    "Zijing 20",
    "Zijing 21",
    "Zijing 22",
    "Zijing 23",
    "Zijing 24",
    "Lab of PHY",
    "Lab of CH",
    "Lab of LAW",
    "Lab of FI",
    "Lab of CS",
    "Lab of ECO",
    "Lab of ART",
    "Lab of ENV",
    "Lab of ADM"
]

def populate_user_db(user_database, ids):
    email_shift = 0
    ids['address'] = {}
    ids['department'] = {}
    ids['user'] = {}
    ids['useraddress'] = []
    for adress in adresses:
        ids['address'][adress] = AddressService.add(user_database, adress)
    for department in departments:
        ids['department'][department] = DepartmentService.add(user_database, department)
        for username in chinese_names:
            mail = "w_" + str(email_shift) + "@mail.tsinghua.edu.cn"
            ids['user'][username] = UserService.add(user_database, email_shift, username.decode('utf8'), mail, ids['department'][department]) 
            email_shift = email_shift + 1
            for _ in random.randint(1, 3):
                addr_num = random.randint(0, len(adresses) - 1)
                ids['useraddress'].append(UserAddressService.add(user_database, ids['address'][adresses[addr_num]], ids['user'][username]))
#             for adress in adresses:
#                 ids['useraddress'].append(UserAddressService.add(user_database, ids['address'][adress], ids['user'][username]))

def populate_departments_dbs(departments_dbs, ids):
    ids['state'] = {}
    for db_name in departments_dbs:
        if db_name == 'users':
            continue
        else:
            for state in states:
                ids['state'][state] = StateService.add(departments_dbs[db_name], state)
    for idsender in ids['useraddress']:
        for idreceiver in ids['useraddress']:
            #print ids['useraddress'][sender], ids['useraddress'][receiver]
            MailService.add(departments_dbs, 0, idsender, idreceiver)

def populate_db(databases):
    ids = {}
    populate_user_db(databases['users'], ids)
    populate_departments_dbs(databases, ids)
    print "Finish populating the DBs"
