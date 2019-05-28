# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/28 9:48'
from flask import render_template, request

from app.models.admin_models import Admin
from . import admin


@admin.route('/', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        user = Admin.query.filter_by(username=request.form.get('username')).first()
        if user and user.password == request.form.get('password'):
            return '200'
        else:
            return '400'


@admin.route('/products')
def products():
    return render_template('admin/admin_products.html')


@admin.route('/customs')
def customs():
    return render_template('admin/admin_customs.html')