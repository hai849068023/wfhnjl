# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 9:40'
from app import db
from datetime import datetime


# 商品分类表
class Classification(db.Model):
    __tablename__ = 'whfrj_classification'
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(15), nullable=False) #名称
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    products = db.relationship('Products', backref='classification')


# 商品表
class Products(db.Model):
    __tablename__ = 'whfrj_products'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, autoincrement=False)
    name = db.Column(db.String(15), nullable=False) #名称
    image_1 = db.Column(db.String(200)) #图片
    image_2 = db.Column(db.String(200)) #图片
    image_3 = db.Column(db.String(200)) #图片
    image_4 = db.Column(db.String(200)) #图片
    image_5 = db.Column(db.String(200)) #图片
    vedio = db.Column(db.String(200)) #视频
    price = db.Column(db.Float, nullable=False) #价格
    specifications = db.Column(db.String(10)) #商品规格
    line_price = db.Column(db.Float, nullable=True) #划线价
    introduction = db.Column(db.String(50))  # 介绍
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cid = db.Column(db.Integer, db.ForeignKey('whfrj_classification.id'))


# 订单表
class Orders(db.Model):
    __tablename__ = 'whfrj_orders'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False) #付款人id
    name = db.Column(db.String(15), nullable=False) #商品名称
    price = db.Column(db.Float, nullable=False)  #价格
    id_pay = db.Column(db.Integer, nullable=False, default=0) #是否支付
    pay_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #支付时间
    add_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #订单生成时间


