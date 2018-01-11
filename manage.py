#encoding=utf-8
import os
from apps import db,app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from apps.models import (
    InterfaceDetail,
    TestCaseInfo,
    TestCase,
    DBVerify,
    TestCaseDB,
    TestSuiteInfo,
    TestSuiteDetail
)

from apps.admin import admin as admin_blue_print
from apps.home import home as home_blue_print
from apps.api import api as api_blue_print

app.register_blueprint(api_blue_print)
app.register_blueprint(home_blue_print)
app.register_blueprint(admin_blue_print)


manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():

    return dict(app=app, db=db)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    db.create_all()