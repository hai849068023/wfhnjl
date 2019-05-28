# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/27 9:40'
from  flask import render_template, request
from . import home
from app.models.product_models import Classification,Products,Orders


@home.route('/', methods=['GET', 'POST'])
def index():
    method = request.method
    if method == 'GET':
        classification = Classification.query.all()
        return render_template('wap/index.html')
    else:
        pass