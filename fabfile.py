from fabric.api import local, settings, abort 
from fabric.contrib.console import confirm
# prepare for deployment

def test():
	with settings(warn_only=True):
		result = local("python test.py -v", capture=True) #&& python test_users.py -v
	if result.failed and not confirm("Tests failed. Continue?"): 
		abort("Aborted at user request.")

def commit():
	message = raw_input("Enter a git commit message: ") 
	local("git add . && git commit -am '{}'".format(message))

def push():
	local("git push origin master")

def prepare(): 
	test()
	commit() 
	push()

def pull():
	local("git pull origin master")

def heroku():
	local("git push heroku master")

def deploy(): 
	pull()
	test() 
	commit() 
	heroku() 
	heroku_test()

#def prepare():
	#pull() #pull latest from github. I dont really want to do that
#	test()  #test
#	commit()  # comitt it localy
#	heroku() #commit to heroku
	#push()

def rollback():
	local("heroku rollback")