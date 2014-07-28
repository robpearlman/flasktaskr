#db_create.py 

from views import db
from models import FTasks
from datetime import date


#cr db and db table
db.create_all()

#insert data

db.session.add(FTasks("Finish this tutorial", date(2014, 3, 13), 10, 1))
db.session.add(FTasks("Finish Real Python", date(2014, 3, 13), 10, 1))

db.session.commit()

