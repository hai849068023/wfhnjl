# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/17 9:47'
from flask import render_template, request, jsonify

from app.models import Article
from . import main


@main.route('/')
@main.route('/<int:page>')
def index(page=1):
    pagination = Article.query.order_by(Article.id.desc()).paginate(page, per_page=2)
    articles = pagination.items
    return render_template('index.html', articles=articles, pagination=pagination)


@main.route('/article/<int:uid>')
def article(uid):
    article_data = Article.query.filter_by(id=uid).first()
    data = {
        'title': article_data.title,
        'author': article_data.author,
        'add_time': article_data.add_time
    }
    return render_template('article.html', data=data)

