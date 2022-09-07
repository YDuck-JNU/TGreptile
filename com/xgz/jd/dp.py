import re
import time

import requests


def shop_sign(token):
    """
    签到
    :param token:
    :return: 返回状态码
    """
    url = 'https://api.m.jd.com/api?appid=interCenter_shopSign&t=' + str(
        time.time()) + '&loginType=2&functionId=interact_center_shopSign_getActivityInfo&body={%22token%22:%22' + token + '%22,%22venderId%22:%22%22}&jsonp=jsonp1000',
    header = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        # "cookie": 'cookie',
        "referer": 'https://h5.m.jd.com/',
        "User-Agent": 'jdapp;iPhone;10.2.2;13.1.2;${randomString(40)};M/5.0;network/wifi;ADID/;model/iPhone8,1;addressid/2308460611;appBuild/167863;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;'
    }
    ss = requests.get(url[0], headers=header)
    # 把ss转换成json格式
    sf = ss.text
    sz = re.findall('errCode:(\d+),', sf)
    ky = re.findall('"code":(\d+),', sf)
    if ky[0] == "200":
        re.findall('"activityName":".*?"', sf)
        return 200
    elif sz[0] == "402":
        re.findall('errMessage:(.*?)",', sf)
        return 402
    else:
        return -1
