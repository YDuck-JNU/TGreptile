import re

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
                    # 处理特殊数据，根据链接获取ct
                    jdht = re.findall(r'.*?href="(https://u\.jd\.com/.*?)"', j, re.S)
                    if len(jdht) > 0:
                        logger.write_log(
                            '活动链接手动添加: ' + str(j))
                        # 把获取的链接传入jd_Activity函数
                        # jdtoc = jd_Activity(jdht[0])
                        # 判断是否有数据
                        # if jdtoc != -1:
                        #     shopsign += jdtoc + '&'
                        #     to_insert(jdtoc)
                        # 跳过本次循环
                        continue
                    # 处理特殊数据直接获取ct
                    # 筛选非https开头和export开头的数据
                    # 为了应付带空格的
                    cs = j.split('=')
                    for v in cs:
                        D = v.split(' ')
                        for d in D:
                            jdtx = re.findall(r'^(?!https:|export)([a-zA-Z0-9]{30,40})$', d, re.S)
                            if len(jdtx) > 0 and jdtx[0] not in '_' and jdtx[0] not in 'jd':
                                insert = to_insert(jdtx[0])
                                if insert[0] == -1:
                                    logger.write_log('插入 ' + str(jdtx[0]) + '失败, 完整信息是 ' + str(j) + ' 异常信息是 ' + str(insert[1]))
                                    continue
                                shopsign += jdtx[0] + '&'
                                logger.write_log('插入成功 ' + str(jdtx[0]))
                            # 跳过本次循环
                            continue
                    exht = re.findall('.*?(export \w+="<a href="https://.*?")', j, re.S)
                    extx = re.findall(r'.*?(export \w+="?\w+"?)', j, re.S)
                    htttx = re.findall(r'.*?href="(https://.*?)"', j, re.S)

                    # 如果开头是export =后面有"https://则添加到文本中
                    if exht:
                        ht = re_exht(file_new, exht, marks)
                        if ht == -1:
                            # 跳过本次循环
                            continue
                        ft = 0
                        # 把标记添加到数组中
                        for k in range(len(ht)):
                            marks.append(ht[k])
                        continue
                    # 如果开头是export或https://开头 =后面没有"https://则添加到文本中
                    else:
                        if len(extx) > 0:
                            tx = re_extx(file_new, extx, marks)
                            if tx == -1:
                                continue
                            ft = 0
                            # 把标记添加到数组中
                            for k in range(len(tx)):
                                marks.append(tx[k])
                            continue
                        # 判断获取的htttx是否为空，如果不为空则进入
                        if len(htttx) > 0:
                            htt = re_htt(file_new, htttx, marks)
                            if htt == -1:
                                continue
                            ft = 0
                            # 把标记添加到数组中
                            for k in range(len(htt)):
                                marks.append(htt[k])
                            continue
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
