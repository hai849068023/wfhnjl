# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/17 9:42'
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app