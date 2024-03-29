# test.py

import os
import unittest

from app import app, db
from app.models import User
#from views import app, db 
#from models import User 
from config import basedir

# generic example: class TestCase(unittest.TestCase):
# place your test functions here

TEST_DB = 'test.db'

class Users(unittest.TestCase):
	# this is a special method that is executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True 
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
			os.path.join(basedir, TEST_DB) 
		self.app = app.test_client()
		db.create_all()

	# this is a special method that is executed after each test
	def tearDown(self): 
		db.drop_all()

	# each test should start with 'test'
	def test_users_can_register(self): 
		new_user = User("mherman","michael@mherman.org","michaelherman") 
		db.session.add(new_user)
		db.session.commit()
		test = db.session.query(User).all()
		for t in test:
			t.name
		assert t.name == "mherman"


if __name__ == '__main__': 
	unittest.main()