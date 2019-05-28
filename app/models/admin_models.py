# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/28 9:51'
from app import db
from datetime import datetime


class Admin(db.Model):
    __tablename__ = 'wfhrj_admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_login = db.Column(db.Integer, default=0)
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class Users(db.Model):
    __tablename__ = 'whfrj_users'
    id = db.Column(db.Integer, primary_key=True)
    wxname = db.Column(db.String(20), nullable=False)  # 微信昵称
    truename = db.Column(db.String(5), nullable=True)  # 真实姓名
    tel = db.Column(db.String(10), nullable=True)  # 电话
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
