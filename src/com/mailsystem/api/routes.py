#!/usr/bin/env python
# coding: utf-8

from bottle import static_file, response, Bottle, request, hook
from src.com.mailsystem.services import DepartmentService, UserService


app = Bottle()


#
# Je crois que c'est ce qui permets d'envoyer à tous les sites qui demandent de l'AJAX :) (à tester)
#
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'

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


@app.route('/user/:id')
def get_user(id):
    db = app.dbs['users']
    UserService.selectById(db, id)
    return id


@app.route('/user/update/:id', method='POST')
def update_user():
    pass


@app.route('/user', method='POST')
def create_user():
    name = request.forms.get('name')
    email = request.forms.get('email')
    address = request.forms.get('address')
    department = request.forms.get('department')
    print name, email, address, department
    pass


@app.route('/dep/:id')
def get_dep(id):
    pass


@app.route('/dep/all')
def get_all_deps():
    pass


@app.route('/dep/update/:id', method='POST')
def update_dep():
    pass


@app.route('/dep', method='POST')
def create_dep():
    pass
