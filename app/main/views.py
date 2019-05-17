# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/17 9:47'
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/article/<id>')
def article(id):
    data = {}
    return render_template('article.html', data=data)


@main.route('/pages/<page>')
def pages(page):
    data = {}
    return render_template('article.html', data=data)
