#encoding=utf-8
import os
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()

app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG') or 'default'

app.config.from_object(config[config_name])
config[config_name].init_app(app)

db.init_app(app)

login_manager = LoginManager(app)

login_manager.session_protection = "strong"
login_manager.login_view = 'home.login'
login_manager.login_message = u'系统必须登录，请登录您的平台账号！'







