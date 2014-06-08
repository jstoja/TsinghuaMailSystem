#!/usr/bin/env python
# coding: utf-8

from bottle import run, static_file, response, Bottle
from src.com.mailsystem.orm.Database import Database


app = Bottle()


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
def update_mail(id):
    pass


@app.route('/mail', method='POST')
def create_mail(id):
    pass


@app.route('/user/:id')
def get_user(id):
    pass


@app.route('/user/update/:id', method='POST')
def update_user(id):
    pass


@app.route('/user', method='POST')
def create_user(id):
    pass


@app.route('/dep/:id')
def get_dep(id):
    pass


@app.route('/dep/update/:id', method='POST')
def update_dep(id):
    pass


@app.route('/dep', method='POST')
def create_dep(id):
    pass


@app.route('/')
def index():
    return '''
        <form action="/img" method="post">
            identifiant:    <input type="text" name="identifiant" />
            <input type="submit" value="identifiant" />
        </form>
    '''

if __name__ == '__main__':
    db = Database('thumail')
    run(app, host='0.0.0.0', port=8080)
