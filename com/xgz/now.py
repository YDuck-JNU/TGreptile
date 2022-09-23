import os

from com.xgz.gheaders.conn import read_yaml, revise_yaml

yam = read_yaml()


def update_time(time):
    """
    修改爬虫爬取时间
    :return:
    """
    try:
        if type(time) == int and int(time) >= 2:
            revise_yaml(f'time: {time}', yam['Label']['time'])
            os.system("kill -9 $(netstat -nlp | grep :5000 | awk '{print $7}' | awk -F'/' '{ print $1 }')")
    except Exception as e:
        print("修改时间异常信息", e)