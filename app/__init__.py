# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/17 9:42'
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/wfhnjl'

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
