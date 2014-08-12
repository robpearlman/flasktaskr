# manage.py

from flask.ext.script import Manager
from flask import url_for

from app import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

@manager.command
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    manager.run()