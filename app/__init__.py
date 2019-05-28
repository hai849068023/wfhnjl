# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 8:56'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap3 import Bootstrap

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/wfhrj?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_DOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)

from .user import user as user_blueprint
from .common.wxapi import wx as wx_blueprint
from .wap.home import home as home_blueprint
from .admin import admin as admin_blueprint

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(wx_blueprint, url_prefix='/wx')
app.register_blueprint(home_blueprint, url_prefix='/home')
app.register_blueprint(admin_blueprint, url_prefix='/admin')