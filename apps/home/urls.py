#encoding=utf-8

from .views import *
from .views import home

home.add_url_rule('/',view_func=IndexView.as_view('index'))
home.add_url_rule('/login',view_func=LoginView.as_view('login'))
home.add_url_rule('/logout',view_func=LogtView.as_view('logout'))
home.add_url_rule('/interface',view_func=InterfaceView.as_view('interface'))
home.add_url_rule('/sql',view_func=SqlListView.as_view('sql_statement'))
home.add_url_rule('/task',view_func=TaskView.as_view('task'))
home.add_url_rule('/tc',view_func=TestCaseView.as_view('test_case'))
home.add_url_rule('/ts',view_func=TestSuiteView.as_view('test_suite'))
