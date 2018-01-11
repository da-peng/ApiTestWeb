#encoding=utf-8
from views import  *

admin.add_url_rule('/role',view_func=RoleView.as_view('role'))
admin.add_url_rule('/user',view_func=UserView.as_view('user'))
admin.add_url_rule('/project',view_func=ProjectView.as_view('project'))