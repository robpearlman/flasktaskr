#config.py 

import os

#get where folder sits

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

#get full path for db

DATABASE_PATH = os.path.join(basedir, DATABASE)

