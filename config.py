#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @author: Ivo Dai
    @Contact: ivo_d@icloud.com
    @File: config.py
    @Time: 2018/9/6 23:08
    @Software: PyCharm Community Edition
    @Environment:
    @Description: 
    @Update:
'''


class PubConfig(object):
    MYSQL_DEFAULT_URI = 'mysql+pymysql://dsw:asdf@shao5.net:13306/web?charset=utf8mb4'


class DevConfig(PubConfig):
    MYSQL_DEFAULT_URI = 'mysql+pymysql://dsw:asdf@shao5.net:13306/web?charset=utf8mb4'


config = {
    "development": DevConfig,
    "default": DevConfig
}
