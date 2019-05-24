# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 14:37'
from app import db
from datetime import datetime
import time


class Accesstoken(db.Model):
    __tablename__ = 'wfhrj_accesstoekn'
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(512), unique=True, nullable=False)
    add_time = db.Column(db.Integer, default=int(time.time()))

