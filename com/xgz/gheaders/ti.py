# -*- coding: utf-8 -*-
import time
from datetime import datetime
from datetime import timedelta
from datetime import timezone

from com.xgz.gheaders.conn import read_yaml


def dates():
    """
    获取%Y-%m-%d日期
    :return tim: 返回现在日期%Y-%m-%d
    """
    tim = time.strftime('%Y-%m-%d', time.gmtime(time.time()))
    return tim


def datetimeS():
    """
    返回%Y-%m-%d %H:%M:%S，国际时间
    :return: 返回数组 [延迟time分钟, 现在时间，快进time分钟]
    """
    times = read_yaml()
    # 获取现在日期 时间 设置误差秒数%Y-%m-%d %H:%M:%S
    delay = time.strftime('%Y-%m-%d %H:%M', time.gmtime(time.time() - ((times['time'] * 60) + times['error'])))
    now = time.strftime('%Y-%m-%d %H:%M', time.gmtime(time.time()))
    fast_forward = time.strftime('%Y-%m-%d %H:%M', time.gmtime(time.time() + ((times['time'] * 60) + times['error'])))
    return [delay, now, fast_forward]


def AS():
    """
    获取当前时间中国时区的时间
    :return:
    """
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    return beijing_now.strftime('%Y-%m-%d %H:%M:%S')


def fast_forward():
    """
    获取东八时区的时间，并且调快进或者调慢速度
    :return:
    """
    # 获取国内日期时间
    ti = AS()
    # 获取程序运行间隔
    times = read_yaml()
    sj = times['time']
    # 把sj转换为秒数并且除2
    sj = (sj * 60) / 2
    # 把ti转换成时间戳
    ti = time.mktime(time.strptime(ti, '%Y-%m-%d %H:%M:%S'))
    # 把ti转换成时间格式
    # 慢了程序间隔的一半
    tislow = time.strftime('%H:%M:%S', time.localtime(ti - (sj)))
    # 快了程序间隔的一半
    tiquick = time.strftime('%H:%M:%S', time.localtime(ti + (sj)))
    return [tislow, tiquick]
