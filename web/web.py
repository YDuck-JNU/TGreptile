# -*- coding: utf-8 -*-
from flask import Flask, render_template

from com.xgz.gheaders.conn import read_yaml
from com.xgz.gheaders.log import rz
from com.xgz.sql.JD_ql import select_data
from flask import Blueprint, render_template

app = Blueprint('web', __name__)
ql = read_yaml()


@app.route("/qlcs")
def qlcs():
    return read_yaml(ql['htmltx'])


@app.route("/qlrz")
def qlrz():
    return rz()


@app.route("/sql")
def sql():
    name = select_data()
    return render_template('hello.html', name=name)


@app.route("/")
def index():
    return "你好本程序运行正常运行"
