#views.py 

from flask import Flask, flash, redirect, render_template, request, \
session, url_for, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from forms import AddTask

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import FTasks

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid login and/or password! please try again'
		else:
			session['logged_in'] = True
			return redirect(url_for('tasks'))
	return render_template('login.html', error=error)

@app.route('/tasks/')
@login_required #wrap
def  tasks():
	open_tasks = db.session.query(FTasks).filter_by(status='1').order_by(FTasks.due_date.asc())
	closed_tasks = db.session.query(FTasks).filter_by(status='0').order_by(FTasks.due_date.asc())
	return render_template('tasks.html',form = AddTask(request.form), open_tasks = open_tasks, closed_tasks = closed_tasks) 
	# query db for open, closed tasks and pass them to tasks.html

#add new tasks
@app.route('/add/', methods=['GET', 'POST'])
@login_required
def  new_task():
	form = AddTask(request.form, csrf_enabled=False)
	print form.errors
	if form.validate_on_submit():
		#print form.errors
		new_task = FTasks(form.name.data, form.due_date.data, form.priority.data, '1')
		db.session.add(new_task)
		db.session.commit()
		flash('New entry successfully posted, thanks!')
	else:
		#print form.errors
		flash('unsuccessful. why?!')
		error = error
	return redirect(url_for('tasks'))

#mark tasks as complete:
@app.route('/complete/<int:task_id>/',)
@login_required
def complete(task_id):
	new_id = task_id
	db.session.query(FTasks).filter_by(task_id=new_id).update({"status":"0"})
	db.session.commit()
	flash('the task was marked as complete')
	return redirect(url_for('tasks'))

# delete tasks:
@app.route('/delete/<int:task_id>/',)
@login_required
def delete_entry(task_id):
	new_id = task_id
	db.session.query(FTasks).filter_by(task_id=new_id).delete()
	db.session.commit()
	flash('the task was deleted')
	return redirect(url_for('tasks'))

@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	flash('You are logged out. Bye!')
	return redirect (url_for('login'))
