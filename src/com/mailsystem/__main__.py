#!/usr/bin/env python
# coding: utf-8

import sys
import json
import argparse

from bottle import run

import src.com.mailsystem.api.routes as api
import src.com.mailsystem.codes as codes
from src.com.mailsystem.orm.Database import Database
from src.com.mailsystem.populate import populate_db


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
        'thumailusers',
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
    parser.add_argument(
        '--populate', action='store_true', default=False,
        help="Generate data to populate the databases"
    )
    args = parser.parse_args()

    setup_file = args.setup
    populate = args.populate

    setup = read_config(setup_file)
    dbs = connect_dbs(setup)
    api.app.dbs = dbs
    codes.codes = setup['codes']
    codes.rev_codes = {v: k for k, v in setup['codes'].items()}
    if populate:
        populate_db(dbs)
    run(api.app, host='0.0.0.0', port=8080)
