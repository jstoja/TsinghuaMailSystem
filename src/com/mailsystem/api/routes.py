#!/usr/bin/env python
# coding: utf-8

from json import dumps

from bottle import static_file, response, Bottle, request, hook
# from src.com.mailsystem.services.DepartmentService import DepartmentService
from src.com.mailsystem.services.UserService import UserService
from src.com.mailsystem.orm import User, Department


app = Bottle()


@hook('after_request')
def enable_cors():
    r = response
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    r.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With,'
    ' Content-Type, Accept'
    r.content_type = 'text/json; charset=utf-8'


@app.route('/test')
def server_static():
    response.content_type = 'text/json; charset=utf-8'
    return static_file("mini-last.json", root='./data')


@app.route('/mail/:id')
def get_mail(id):
    pass


@app.route('/mail/dep/:id')
def get_dep_mails(id):
    pass


@app.route('/mail/user/:id')
def get_user_mails(id):
    pass


@app.route('/mail/update/:id', method='POST')
def update_mail():
    pass


@app.route('/mail', method='POST')
def create_mail():
    pass


@app.route('/user/all')
def get_all_users():
    users = UserService.listAll(app.dbs['users'])
    if users is None:
        return ""
    us = []
    for user in users:
        u = {'name': user.name, 'email': user.email,
             'department': user.iddepartment}
        us.append(u)
    response.content_type = 'text/json; charset=utf-8'
    return dumps(us)


@app.route('/user/:id')
def get_user(id):
    user = UserService.selectById(app.dbs['users'], id)
    print user.name, user.email, user.iddepartment
    print user
    if user is None:
        return ""
    u = {'name': user.name, 'email': user.email,
         'department': user.iddepartment}
    response.content_type = 'text/json; charset=utf-8'
    return dumps(u)


@app.route('/user/update/:id', method='POST')
def update_user(id):
    name = request.forms.get('name')
    email = request.forms.get('email')
    department = request.forms.get('department')
    print name, email, department
    print request.body.read()
    return UserService.update(
        app.dbs['users'],
        id,
        name,
        email,
        department
    )


@app.route('/user', method='POST')
def create_user():
    name = request.forms.get('name')
    email = request.forms.get('email')
    department = request.forms.get('department')
    print name, email, department
    UserService.add(app.dbs['users'], name, email, department)


@app.route('/dep/:id')
def get_dep(id):
    pass


@app.route('/dep/all')
def get_all_deps():
    # deps = DepartmentService.listAll(app.dbs['LAW'])
    pass


@app.route('/dep/update/:id', method='POST')
def update_dep():
    pass


@app.route('/dep', method='POST')
def create_dep():
    pass
