import re
from urllib import parse

from com.xgz.gheaders.conn import read_txt, read_yaml
from com.xgz.gheaders.log import LoggerClass
from com.xgz.sql.sign import to_insert
from com.xgz.txt.re_result import re_exht, re_extx, re_htt

logger = LoggerClass('debug')


def tx_revise():
    """
    用与修改文本,只保留关键字到文本
    :return: 正常返回200, 否则返回-1
    """
    try:
        # 读取内容
        yml = read_yaml()
        lines = read_txt(yml['path'])
        # 修改内容
        file_new = open(yml['path'], 'w+', encoding="utf-8")
        # 用于拼接店铺签到
        shopsign = ''
        # 用做标记如果是空格则不换行,1为不换行，0为换行
        # ft = 1
        for i in lines:
            try:
                # 用做标记如果是空格则不换行,1为不换行，0为换行
                ft = 1
                # 创建数组用于记录每行值是否同行的export XX是一样的，如果一样就换行
                marks = []
                # 以<br/>分割，这样就可以处理同行问题
                line = i.split('<br/>')
                # 同行内容循环
                for j in line:
                    j = parse.unquote(j).replace('&quot;', '"').replace('&amp;', "&")
                    # 处理特殊数据，启用
                    jdht = re.findall(r'.*?href="(https://u\.jd\.com/.*?)"', j, re.S)
                    if len(jdht) > 0:
                        # logger.write_log('活动链接手动添加: ' + str(j))
                        # 跳过本次循环
                        continue
                    # 处理特殊数据直接获取ct
                    # 筛选非https开头和export开头的数据
                    # 京东店铺签到
                    # 为了应付带空格的
                    for v in j.split('='):
                        for d in v.split(' '):
                            jd_tx = re.findall(r'^(?!https:|export)([a-zA-Z0-9]{30,40})$', d, re.S)
                            if len(jd_tx) > 0 and jd_tx[0] not in '_' and jd_tx[0] not in 'jd':
                                insert = to_insert(jd_tx[0])
                                if insert[0] == -1:
                                    logger.write_log(
                                        '插入 ' + str(jd_tx[0]) + '失败, 完整信息是 ' + str(j) + ' 异常信息是 ' +
                                        insert[1])
                                    continue
                                shopsign += jd_tx[0] + '&'
                                logger.write_log('插入成功 ' + str(jd_tx[0]))
                            # 跳过本次循环
                            continue
                    ex_ht = re.findall('.*?(export [0-9a-zA-Z_]+="(?:<a href=")?https://.*?&?.*?")', j, re.S)
                    ex_tx = re.findall(r'.*?(export [0-9a-zA-Z_]+="?[A-Za-z0-9&_]+"?)', j, re.S)
                    ht_tx = re.findall(r'(https://.*?&?.*?)"', j, re.S)
                    # 如果开头是export =后面有"https://则添加到文本中
                    if ex_ht:
                        ht = re_exht(file_new, ex_ht, marks)
                        if len(ht) > 0:
                            ft = 0
                            # 把标记添加到数组中
                            for k in range(len(ht)):
                                marks.append(ht[k])
                        # continue
                    # 如果开头是export或https://开头 =后面没有"https://则添加到文本中
                    elif ex_tx:
                        if len(ex_tx[0].split('=')[-1]) > 7:
                            tx = re_extx(file_new, ex_tx, marks)
                            if len(tx) > 0:
                                ft = 0
                                # 把标记添加到数组中
                                for k in range(len(tx)):
                                    marks.append(tx[k])
                                    # continue
                    # 判断获取的ht_tx是否为空，如果不为空则进入,https的链接
                    if len(ht_tx) > 0:
                        htt = re_htt(file_new, ht_tx, marks)
                        if len(htt) > 0:
                            ft = 0
                            # 把标记添加到数组中
                            for k in range(len(htt)):
                                marks.append(htt[k])
                            # continue
                # 处理好一行后换行
                if ft == 0:
                    file_new.write('\n')
                # 清空marks
                marks.clear()
            except Exception as e:
                logger.write_log("对比发生异常事件: " + str(e))
        # 判断是否有店铺签到
        if shopsign != '':
            file_new.write(str(yml['js'][0][1]) + '="' + shopsign[:-1] + '"')
        file_new.close()
        return 200
    except Exception as e:
        logger.write_log("tx_revise,异常问题: " + str(e))
        return -1
