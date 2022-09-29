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
        "cookie": 'pt_key=AAJjKTcHADBWY9sZ2x5bgpylAwEsnu-xqptvYZ8jJIDPlcopNEFZ5J6rfOrkUir-RQXbbFUsPNE; pt_pin=jd_nWrOQHBWquUM;',
        "referer": 'https://h5.m.jd.com/',
        "User-Agent": 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MI 8 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.5.40'
    }
    try:
        ss = requests.get(url[0], headers=header, timeout=30)
        # 把ss转换成json格式
        sf = ss.text
        ky = re.findall('"code":(\d+),', sf)
        if len(ky) > 0:
            if ky[0] == "200":
                # aa = re.findall('"activityName":".*?"', sf)
                # print(aa)
                return 200
        else:
            return -1
    except Exception as e:
        print(e)
        return -1
