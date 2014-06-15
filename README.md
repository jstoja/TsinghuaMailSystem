TsinghuaMailSystem
==================

## Install

### requirements

- python2
- sqlite, mysql or pgsql

You need 4 python packages to launch TsinghuaMailSystem. They may be installed
with pip.

- bottle
- sqlalchemy
- mysql-connector-repackaged
- pg8000

```pip install -r requirements.txt```

## Usage

Populate the database:

```python -m src.com.mailsystem --populate```

Launch TsinghuaMailSystem:

```python -m src.com.mailsystem```

```
usage: python -m src.com.mailsystem [-h] [--setup SETUP] [--populate]

optional arguments:
    -h, --help     show this help message and exit
    --setup SETUP  A JSON file with DB's configuration (defaults to setup.json)
    --populate     Generate data to populate the databases
```

## Config

The config file is setup.json. For each department, you have to choose an uri to
connect to the database.

For mysql, it will be something like
```"mysql+mysqlconnector://root:root@localhost:3306"```

For sqlite ```"sqlite://"```

