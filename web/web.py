# -*- coding: utf-8 -*-
import os

from flask import request

from com.xgz.gheaders.conn import read_yaml
from com.xgz.gheaders.log import rz
from com.xgz.now import update_time
from com.xgz.sql.JD_ql import select_data
from flask import Blueprint, render_template

app = Blueprint('web', __name__)
ql = read_yaml()


@app.route("/qlcs", methods=['GET', 'POST'])
def qlcs():
    if request.environ['REMOTE_ADDR'] in ql['black']:
        return "你已经被拉入黑名单"
    else:
        return read_yaml(ql['htmltx'])


@app.route('/log', methods=['GET'])
def log():
    """
    日志
    :return:
    """
    return render_template('log.html', rz=rz())


@app.route("/sql", methods=['GET', 'POST'])
def sql():
    if request.method == 'GET':
        name = select_data()
        return render_template('hello.html', name=name)
    else:
        name = select_data()
        return name


@app.route('/renew', methods=['GET', 'POST'])
def renew():
    os.system("sh /TGreptile/docker/gi.sh")
    return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
def ine():
    if request.method == 'POST':
        urls = request.form.get('url')
        update_time(urls)
    return render_template('index.html')
