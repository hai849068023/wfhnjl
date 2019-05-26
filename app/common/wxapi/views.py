# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/24 11:28'
from . import wx
import requests, re, time
from app import db
from app.models.wxapi_models import Accesstoken


@wx.route('/')
def wxapi():
    # 获取微信access_token
    wxtoken = Accesstoken.query.get(1)
    now_time = int(time.time())
    timeout = now_time - wxtoken.add_time
    if wxtoken == None or timeout > 7200:
        wxapi = requests.get(
            'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx17b229a0cf9c5219&secret=150c4cfe90bb04bd53400c387512a78f')
        data = wxapi.text
        access_token = re.search('"access_token":"(.*?)"', data).group(1)
        # 存入数据库
        now_time = int(time.time())
        accesstoken = Accesstoken(access_token=access_token, add_time=now_time)
        db.session.add(accesstoken)
        db.session.commit()
    else:
        accesstoken = Accesstoken.query.get(1)
        access_token = accesstoken.access_token
    return access_token
