#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @author: Ivo Dai
    @Contact: ivo_d@icloud.com
    @File: run.py
    @Time: 2018/9/6 22:41
    @Software: PyCharm Community Edition
    @Environment:
    @Description: 
    @Update:
'''

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8555, debug=True)
