# -*- coding: utf-8 -*-
from flask import request

from com.xgz.gheaders.conn import read_yaml
from com.xgz.gheaders.log import rz
from com.xgz.sql.JD_ql import select_data
from flask import Blueprint, render_template

app = Blueprint('web', __name__)
ql = read_yaml()


@app.route("/qlcs")
def qlcs():
    if request.environ['REMOTE_ADDR'] in ql['black']:
        return "你已经被拉入黑名单"
    else:
        return read_yaml(ql['htmltx'])


@app.route("/log")
def qlrz():
    return rz()


@app.route("/sql")
def sql():
    name = select_data()
    return render_template('hello.html', name=name)


@app.route("/")
def index():
    print(request.environ['REMOTE_ADDR'])
    return "你好本程序运行正常运行"
