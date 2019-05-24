# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 11:28'
from flask import json
from . import wx
import requests, re


@wx.route('/')
def wxapi():
    wxapi = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx17b229a0cf9c5219&secret=150c4cfe90bb04bd53400c387512a78f')
    data = wxapi.text
    access_token = re.search('"access_token":"(.*?)"', data).group(1)
    return 'api'