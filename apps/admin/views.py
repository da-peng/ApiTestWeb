#encoding=utf-8
from flask import render_template
from flask.views import MethodView

from . import  admin

from flask_login import (
    login_required
)


class ProjectView(MethodView):
    @login_required
    def get(self):

        return render_template('admin/project.html')

class RoleView(MethodView):
    @login_required
    def get(self):

        return render_template('user/role.html')

class UserView(MethodView):
    @login_required
    def get(self):

        return render_template('user/user.html')