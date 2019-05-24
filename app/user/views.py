# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 11:13'
from . import user

@user.route('/')
def user():
    return 'hello user'