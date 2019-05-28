# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/27 9:40'
from flask import Blueprint

home = Blueprint('home', __name__)

from . import views