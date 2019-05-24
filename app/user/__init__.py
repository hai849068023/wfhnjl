# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 11:12'
from flask import Blueprint

user = Blueprint('user', __name__)

from . import views