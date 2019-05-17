# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/17 9:47'
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from . import views