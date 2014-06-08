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
def server_static2(id):
    return static_file("mini-last.json", root='./data')


@app.route('/sender/:username')
def sender(username):
    pass


@app.route('/receiver/:username')
def receiver(username):
    pass


@app.route('/mail/:id/update', method='POST')
def udpate(id):
    pass


@app.route('/mail/new', method='POST')
def new_mail():
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
