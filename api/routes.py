#!/usr/bin/env python
# coding: utf-8

from bottle import route, run, static_file, response


@route('/test')
def server_static():
    response.content_type = 'text/json; charset=utf-8'
    return static_file("mini-last.json", root='./data')


@route('/mail/:id')
def server_static2(id):
    return static_file("mini-last.json", root='./data')


@route('/sender/:username')
def sender(username):
    pass


@route('/receiver/:username')
def receiver(username):
    pass


@route('/mail/:id/update', method='POST')
def udpate(id):
    pass


@route('/')
def index():
    return '''
        <form action="/img" method="post">
            identifiant:    <input type="text" name="identifiant" />
            <input type="submit" value="identifiant" />
        </form>
    '''

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
