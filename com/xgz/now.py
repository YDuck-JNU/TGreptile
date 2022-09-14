import os

from com.xgz.gheaders.conn import read_yaml, revise_yaml

yam = read_yaml()


def update_time(time):
    """
    修改爬虫爬取时间
    :return:
    """
    revise_yaml(f'time: {time}', yam['Label']['time'])
    os.system("kill -9 $(netstat -nlp | grep :5000 | awk '{print $7}' | awk -F'/' '{ print $1 }')")
