#encoding=utf-8
from flask import current_app
from apps import db
from werkzeug.security import check_password_hash,generate_password_hash

class Permisson:#这里的权限我是复制flask开发博客里面的，可以根据需求去修改
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTRATOR = 0xff

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(), nullable=True, unique=True)
    default = db.Column(db.Boolean(), default=False)
    permissions = db.Column(db.Integer())
    users = db.relationship('User', backref='itsrole')

    @staticmethod
    def insert_roles():
        roles = {
            'User':(Permisson.FOLLOW|Permisson.COMMENT|
                    Permisson.WRITE_ARTICLES, True),
            'Administrator':(0xff, False)}
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

class Work(db.Model):
    __tablename__='works'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    name=db.Column(db.String(),unique=True)
    user= db.relationship('User', backref='works', lazy='dynamic')

    def __repr__(self):
        return  self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username=db.Column(db.String(63),unique=True)
    password=db.Column(db.String(252))
    user_email=db.Column(db.String(64),unique=True)
    status=db.Column(db.Integer(),default=0)
    work_id=db.Column(db.Integer(),db.ForeignKey('works.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))

    def __repr__(self):
        return  self.username

    def can(self, permissions):
        return self.itsrole is not None and \
               (self.itsrole.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permisson.ADMINISTRATOR)

    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
        return  check_password_hash(self.password,password)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):# 昵称
        return False
    def get_id(self):
        return self.id

class ProjectManage(db.Model):

    __tablename__ = 'project_manage'

    id = db.Column(db.Integer(),primary_key=True,autoincrement=True) # 项目id
    project_name = db.Column(db.String(200),unique=True)
    project_description = db.Column(db.String(255))

class ModelManage(db.Model):

    __tablename__ = 'project_model'

    id = db.Column(db.Integer(),primary_key=True,autoincrement=True) # 模块id
    model_name = db.Column(db.String(200))
    model_description = db.Column(db.String(255))
    project_id = db.Column(db.Integer(),db.ForeignKey('project_manage.id')) # 项目id


class InterfaceDetail(db.Model):
    __tablename__ = 'interface_detail'

    id = db.Column(db.Integer(),primary_key=True,autoincrement=True) # 接口id
    interface_name = db.Column(db.String(255)) # 接口名称
    interface_type = db.Column(db.String(50))  # 接口请求方法
    host = db.Column(db.String(255))  # 接口host
    url = db.Column(db.String(255))   # 接口url
    is_sign = db.Column(db.Boolean()) # 是否使用请求签名
    header = db.Column(db.String(255)) #请求头
    cookie = db.Column(db.String(255))  # 请求cookie

    request_sample = db.Column(db.String(500))  # 接口data示例数据

    def __repr__(self):
        return self.interface_name


class TestCaseInfo(db.Model):
    __tablename__ = 'testcase_info'  # 测试用例

    tc_id = db.Column(db.Integer(),primary_key=True, autoincrement=True)  # 测试用例 id
    tc_name = db.Column(db.String(200))  # 用例名称
    tc_description = db.Column(db.String(255))  # 测试用例描述

    def __repr__(self):
        return self.tc_name

class TestCase(db.Model):

    __tablename__ = 'testcase_detail'  # 测试用例 设计

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  # 自增id
    tc_id = db.column(db.Integer(),db.ForeignKey('testcase_info.tc_id')) # 测试用例 id
    interface_id = db.column(db.Integer(),db.ForeignKey('interface_detail.id'))  # 请求接口 Id
    test_data = db.Column(db.String(255))  # 测试数据 json数据
    expect_result = db.Column(db.String(255))  # 每个接口对应预期结果  key=？


class DBVerify(db.Model):
    __tablename__ = 'sql_statement'   # 数据库Select校验

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  # 自增id
    sql_description = db.Column(db.String(255))  # sql语句描述
    sql_statement = db.Column(db.String(255))  # sql语句
    expect_result = db.Column(db.String(100))  # 预期结果
    type = db.Column(db.String(50),default='SELECT')  #  默认为select语句

    def __repr__(self):
        return self.sql_description

class TestCaseDB(db.Model):

    __tablename__ = 'tc_db_relative'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  # 自增id
    tc_id = db.Column(db.Integer(),db.ForeignKey('testcase_info.tc_id')) #测试用例id
    sql_id = db.Column(db.Integer(),db.ForeignKey('sql_statement.id'))  #sql语句id


class TestSuiteInfo(db.Model):

    __tablename__ = 'testsuite_info'

    ts_id = db.Column(db.Integer(),primary_key=True) #   测试套件id
    ts_name = db.Column(db.String(200))
    ts_description = db.Column(db.String(200))  # 测试套件描述
    def __repr__(self):
        return self.ts_name


class TestSuiteDetail(db.Model):
    __tablename__ = 'testsuite_detail'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  # 自增id
    ts_id  = db.Column(db.Integer(),db.ForeignKey('testsuite_info.ts_id'))  #测试套件Id
    ts_name = db.Column(db.String(200),db.ForeignKey('testsuite_info.ts_name'))
    tc_id = db.Column(db.Integer(),db.ForeignKey('testcase_info.tc_id'))  # 一个测试用例集，可以关联多个测试用例
    tc_name = db.Column(db.String(200),db.ForeignKey('testcase_info.tc_name'))

    def __repr__(self):
        return self.ts_name
