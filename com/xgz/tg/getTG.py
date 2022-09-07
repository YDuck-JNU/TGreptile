import re

import requests

from com.xgz.gheaders.conn import read_yaml, empty_txt, read_txt
from com.xgz.gheaders.get_headers import tg_header
from com.xgz.gheaders.log import LoggerClass
from com.xgz.gheaders.ti import datetimeS

logger = LoggerClass('debug')
"""
"""
# 设置代理
proxies = {
    'http': 'socks5://127.0.0.1:10808',
    'https': 'socks5://127.0.0.1:10808'
}


def get_tele(url, headers, cookie):
    """
    获取电报网页
    :return:返回的是个数组，[状态码,html内容]
    """
    prox = read_yaml()

    cookies = {
        'cookie': cookie
    }
    # 拼接网址
    url = "https://t.me/s/" + str(url)
    try:
        if prox['acting'][0]['enable'] == 0:
            proxy = prox['acting']
            acting = [proxy[1]['proxy'], proxy[2]['port'], proxy[3]['type']]
            proxies = {
                'http': f'{acting[0]}://{acting[1]}:{acting[2]}',
                'https': f'{acting[0]}://{acting[1]}:{acting[2]}'
            }
            # 设置代理
            output = requests.get(url, headers=headers, proxies=proxies, cookies=cookies, timeout=20)
        else:
            output = requests.get(url=url, headers=headers, cookies=cookies, timeout=20)
        # 设置编码
        output.encoding = 'utf-8'
        return [output.status_code, output.text]
    except Exception as e:
        logger.write_log("get_tele,获取电报" + str(url) + "网页异常: " + str(e))


def re_filter(path, te_text):
    """
    用于获取到自己需要的写入文件,如果获取不到自己需要的则不创建文件
    :param te_text: 获取到的电报网页的内容
    :param path: 获取文件保存路径
    :return: 如果没有数据返回-1,如果有数据没有可添加的返回200
    """""
    try:
        # 记录时间
        times = datetimeS()
        dd = re.findall(
            '<div class="tgme_widget_message_wrap js-widget_message_wrap">(.*?</time>)</a></span>\s*</div>\s*</div>\s*</div>',
            te_text, re.S)
        # 诺长度为0表示没有数据直接退出执行返回-1
        if len(dd) == 0:
            return -1
        f = open(path, mode='a+', encoding='utf-8')
        for i in range((len(dd) - 1), -1, -1):
            # 获取的是时间
            ti = re.findall('<time datetime="(\w{4}-\w{2}-\w{2})T(\w{2}:\w{2}).*?" class="time">\w{2}:\w{2}</time>',
                            dd[i], re.S)
            # # 获取的是所有的内容
            tes = re.findall('<div class="tgme_widget_message_text js-message_text" dir="auto">(.*?)</div>', dd[i],
                             re.S)
            # # 判获取是否为空，诺不为空打开文件
            if len(tes) == len(ti):
                ti1 = ti[0][0] + " " + ti[0][1]
                # print("快的时间：" + times[2])
                # print("消息时间：" + str(ti1))
                # print("慢时间：" + times[0])
                # 对比时间，如果时间大于等于上次的时间就获取数据
                if times[2] >= ti1 >= times[0]:
                    # 写入文件把所有&quot;替换成"
                    logger.write_log("添加: " + str(tes[0]) + " 内容成功")
                    f.write(tes[0].replace("&quot;", "\"") + '\n')
                else:
                    # 因为是倒序所以如果时间小于规定的时间就结束
                    f.close()
                    return 200
        f.close()
        return 200
    except Exception as e:
        logger.write_log("re_filter,异常问题: " + str(e))
        return -1


def tg_judge():
    """
    执行TG有关的，主要是获取TG数据然后存储
    :return: 正常返回200不正常返回-1
    """
    try:
        ymltx = read_yaml()
        # 清空文件内容
        empty_txt(ymltx['path'])
        # log_ip("清空文件内容完毕")
        # 用于记录每次状态码
        # 根据conn.yml文件里的TG频道决定执行次数
        for i in range(len(ymltx['url'])):
            # 获取TG的请求头
            tg_h = tg_header(ymltx['url'][int(i)])
            get_te = get_tele(ymltx['url'][i], tg_h, ymltx['cookie'])
            # 判断状态码是否为200
            if get_te[0] == 200:
                re_filter(ymltx['path'], get_te[1])
                # 如果获取到的状态码是200就记录下来
            else:
                logger.write_log(f"获取 {ymltx['url'][int(i)]} 数据失败")
        # 判断文件是否为空，如果为空则返回-1
        if len(read_txt(ymltx['path'])) > 0:
            return 200
        else:
            logger.write_log("添加的文件为空,不执行后面筛选")
            return -1
    except Exception as e:
        logger.write_log("tg_judge,异常问题: " + str(e))
        return -1
