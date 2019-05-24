# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 10:53'
from app import db
from datetime import datetime


#用户表
class Users(db.Model):
    __tablename__ = 'whfrj_users'
    id = db.Column(db.Integer, primary_key=True)
    wxname = db.Column(db.String(20), nullable=False) #微信昵称
    truename = db.Column(db.String(5), nullable=True) #真实姓名
    tel = db.Column(db.String(10), nullable=True) #电话
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))