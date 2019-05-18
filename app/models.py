# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/18 9:09'
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_migrate import Migrate, MigrateCommand
from app import app
from flask_script import Manager

db = SQLAlchemy(app)
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)

    banner = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(12))
    content = db.Column(db.Text, nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
