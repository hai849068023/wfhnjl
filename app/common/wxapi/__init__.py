# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 11:28'
from flask import Blueprint

wx = Blueprint('wx', __name__)

from . import views