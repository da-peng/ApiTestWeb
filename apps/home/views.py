#encoding=utf-8
from flask import (
    render_template,
    request,
    flash,
    session,
    redirect,
    url_for
)
# 导入蓝本 home
from . import home
from flask.views import MethodView
from apps.models import *
from apps.form import *
from apps import login_manager
from flask_login import (
    login_user,
    logout_user,
    login_required
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginView(MethodView):#登录
    def get(self):
        form=LoginFrom()
        return render_template('login.html', form=form)

    def post(self):
        form=LoginFrom()
        username=request.form.get('username')
        password=request.form.get('password')
        if username =='':
            flash(u'用户名不能为空')
            return render_template('login.html', form=form)
        if password =='':
            flash(u'密码不能为空！')
            return render_template('login.html', form=form)
        user=User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password=password) is True:
                if user.status==0: # 0 正常
                    login_user(user)
                    session['username']=username
                    next =request.args.get('next')
                    return  redirect(next or url_for('home.index'))
                flash(u'用户冻结，请联系管理员')
                return render_template('login.html', form=form) # 有问题返回重新渲染页面
            flash(u'用户名密码错误')
            return render_template('login.html', form=form)
        flash(u'用户名不存在')
        return  render_template('login.html', form=form)

class LogtView(MethodView):#退出
    def get(self):
        session.clear()
        logout_user()
        return redirect(url_for('home.login'))


class IndexView(MethodView):
    @login_required
    def get(self):

        return render_template('home/index.html')

PageShow = 30

class InterfaceView(MethodView):
    @login_required
    def get(self,page=1):
        pagination=InterfaceDetail.query.order_by('-id').paginate(page, per_page=int(PageShow),error_out=False)
        inter=pagination.items
        return  render_template('home/interface.html', inte=inter, pagination=pagination)


class SqlListView(MethodView):
    @login_required
    def get(self):
        return render_template('home/sql_statement.html')

class TaskView(MethodView):
    @login_required
    def get(self):
        return render_template('home/task.html')

class TestSuiteView(MethodView):
    @login_required
    def get(self):
        return render_template('home/test_suite.html')

class TestCaseView(MethodView):
    @login_required
    def get(self):
        return render_template('home/test_case.html')

