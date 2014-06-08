#!/usr/bin/env python
# coding: utf-8

import sys
import json
import argparse

from bottle import run

import src.com.mailsystem.api.routes as api
from src.com.mailsystem.orm.Database import Database


def read_config(setup_file):
    try:
        with open(setup_file) as f:
            setup = json.load(f)
    except Exception as e:
        print(
            "Can't process setup file '{}' : {}", setup_file, e
        )
        sys.exit(1)
    return setup


def connect_dbs(setup):
    databases = {}
    databases['users'] = Database(
        'users',
        setup['users']['user'],
        setup['users']['password'],
        setup['users']['host'],
        setup['users']['port']
    )
    for db in setup['departments']:
        infos = setup['departments'][db]
        if db not in databases:
            databases[db] = Database(
                db,
                infos['user'],
                infos['password'],
                infos['host'],
                infos['port']
            )
    return databases

if __name__ == '__main__':
    parser = argparse.ArgumentParser("thumail")
    parser.add_argument(
        '--setup', default='setup.json',
        help="A JSON file with DB's configuration (defaults to setup.json)"
    )
    args = parser.parse_args()

    setup_file = args.setup
    setup = read_config(setup_file)
    dbs = connect_dbs(setup)
    api.app.dbs = dbs
    run(api.app, host='0.0.0.0', port=8080)
