"""
主方法，用于执行爬虫
"""
import os
import re
import threading

from flask import Flask
from flask_apscheduler import APScheduler

from com.xgz.gheaders.conn import read_yaml
from com.xgz.gheaders.ti import fast_forward
from com.xgz.jd.jd_filter import jd_sql
from com.xgz.tg.getTG import tg_judge
from com.xgz.txt.txt_compared import txt_main, add_null
from com.xgz.txt.txt_zli import tx_revise
from web import web, add

app = Flask(__name__)

app.register_blueprint(web.app, url_prefix='/')
app.register_blueprint(add.app, url_prefix='/sql')
# 下面是定时任务
scheduler = APScheduler()
yml = read_yaml()


@scheduler.task('interval', id='tk', hours=12)
def tc():
    """
    店铺签到tk定时检测
    :return:
    """
    jd_sql('jd_tk')


@scheduler.task('interval', id='mai', minutes=read_yaml()['time'])
def tire():
    ts1 = tg_judge()
    # # 判断返回的值是否为非-1
    # # 获取时间用于判断
    ti = fast_forward()
    # 当数据为空或者时间为凌晨时，执行爬虫
    if ts1 != -1 or ti[0] <= yml['js'][0][2] <= ti[1]:
        ts2 = tx_revise()
        if ts2 != -1:
            txt_main()
    else:
        # 如果没有内容，则添加空的数据
        add_null()


def main():
    """
    如果没保存数据的文件则创建
    :return:
    """
    pa = re.findall('(.*?)/\w+\.\w+', yml['htmltx'])
    if pa:
        if not os.path.exists(pa[0]):  # 判断日志存储文件夹是否存在，不存在，则新建
            os.makedirs(pa[0])
    scheduler.start()
    tire()
    jd_sql('jd_tk')


# 主方法
if __name__ == '__main__':
    t1 = threading.Thread(target=main, args=())
    t1.start()
    app.run(host='0.0.0.0', port=5000, debug=False)
