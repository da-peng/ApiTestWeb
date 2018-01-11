#encoding=utf-8
from flask_wtf import  FlaskForm

from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    validators,
    SelectField,
)
from wtforms.validators import Email
from apps.models import Work

class LoginFrom(FlaskForm):

    username = StringField(u'用户名',
                           [validators.Length(min=4, max=16, message=u'用户名长度在4-16位'),
                            validators.DataRequired()],
                           render_kw={'placeholder': u'请输入用户名'})

    password = PasswordField(u'密码',
                             [validators.length(min=8, max=16, message=u'密码长度8-16位'),
                              validators.DataRequired()],
                             render_kw={'placeholder': u'请输入密码'})
choice_list = []


class RegFrom(FlaskForm):

    # work_list = Work.query.all()
    # for i in range(len(work_list)):
    #     choice_list.append((work_list[i].id, work_list[i].name))
    #
    username = StringField(u'注册用户名',
                           [validators.Length(min=4, max=16, message=u'用户名长度在4-16位'),
                            validators.DataRequired(message=u'请输入用户名')],
                           render_kw={'placeholder': u'请输入用户名'})

    password = PasswordField(u'注册密码',
                             [validators.length(min=8, max=16, message=u'密码长度8-16位'),
                              validators.DataRequired(message=u'请输入密码')],
                             render_kw={'placeholder': u'请输入密码'})

    se_password = PasswordField(u'再次输入密码',
                                [validators.length(min=8, max=16, message=u'密码长度8-16位'),
                                 validators.DataRequired(message=u'请输入确认密码')],
                                render_kw={'placeholder': u'请输入密码'})

    email=StringField(u'输入注册邮箱',
                      [ validators.DataRequired(message=u'请输入邮箱'),
                        Email(message=u'邮箱格式不对')],
                      render_kw={'placeholder': u'请输入邮箱'})

    work=SelectField(u'选择职位',
                     choices=choice_list,
                     coerce=int,
                     validators=[validators.DataRequired(message=u"职位不能为空")])

