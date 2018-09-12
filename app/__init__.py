#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @author: Ivo Dai
    @Contact: ivo_d@icloud.com
    @File: __init__.py
    @Time: 2018/9/6 22:42
    @Software: PyCharm Community Edition
    @Environment:
    @Description: 
    @Update:
'''

import logging.config
import os

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from itsdangerous import TimedJSONWebSignatureSerializer

from config import config

SETTINGS = config["default"]

app_path = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.join(app_path, "static")


def create_app():
    logging.config.fileConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "logging.conf"))
    app = Flask(__name__, static_folder='./static')
    UPLOAD_FOLDER = os.path.join(app_path, "uploads")
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    Limiter(key_func=get_remote_address, headers_enabled=True, default_limits=["1000/minute"]).init_app(app)
    from app.onecity_v2 import v2_blueprint
    app.register_blueprint(
        v2_blueprint,
        url_prefix='/onecity/v2'
    )
    return app
