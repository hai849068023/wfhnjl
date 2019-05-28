# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/28 9:48'
from flask import Blueprint

admin = Blueprint('admin',__name__)

from . import views