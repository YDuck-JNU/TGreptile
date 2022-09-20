from com.xgz.gheaders.log import LoggerClass
from com.xgz.txt.deal_with import export_https, export_txt, https_txt

logger = LoggerClass('debug')


def re_exht(file_new, exht, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的export_https的内容
    :param file_new: 文件对象
    :param exht: 匹配到的内容
    :param marks: 去重用的标记
    :return: 正常返回数组, 否则返回[]
    """
    try:
        # 使用这个循环是防止有人不换行把内容都放在一行
        for exhtx in exht:
            exhtx = exhtx.replace('%3D', '=')
            exhtx = exhtx.replace('%22', '"')
            exhtx = exhtx.replace('%20', ' ')
            exhtx = exhtx.replace('%3A', ':')
            exhtx = exhtx.replace('%3F', '?')
            exhtx = exhtx.replace('%26', '&')
            # 把exht分隔
            separate = exhtx.split('=')
            # print(separate)
            # 保证一行只能存在一个相同参数
            if separate[0] not in marks:

                # 把带 export 后面是链接的直接写入文本
                file_new.write(export_https(exhtx))
                marks.append(separate[0])
            else:
                # 如果存在相同参数,则在写入文本前加上\n
                file_new.write('\n' + export_https(exhtx))
        file_new.write('\n')
        # 把带参数用于标记
        return marks
    except Exception as e:
        logger.write_log('re_exht 出错了: ' + str(e))
        return []


def re_extx(file_new, extx, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的export_txt的内容
    :param file_new: 文件对象
    :param extx: 文本内容
    :param marks: 去重用的标记
    :return: 正常返回数组, 否则返回[]
    """
    try:
        # 使用这个循环是防止有人不换行把内容都放在一行
        for ext in extx:
            # 把extx分隔
            separate = ext.split('=')
            # 保证一行只能存在一个相同参数
            if separate[0] not in marks:
                ex = export_txt(ext)
                # 返回的值不是-1则写入文本
                if ex != -1:
                    # 写入文件
                    file_new.write(ex)
                    # 把带参数写入字符串用于标记
                    marks.append(separate[0])
            else:
                # 如果存在相同参数,则在写入文本前加上\n
                file_new.write('\n' + export_txt(ext))
        # file_new.write('\n')
        return marks
    except Exception as e:
        logger.write_log('re_extx 出错了: ' + str(e))
        return []


def re_htt(file_new, httx, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的https_txt的内容
    :param file_new: 文件对象
    :param httx: 匹配到的内容
    :param marks: 去重用的标记
    :return: 正常返回数组, 否则返回[]
    """
    try:
        # 使用这个循环是防止有人不换行把内容都放在一行
        for ht in httx:
            htt = https_txt(ht)
            # 判断返回的是不是数组
            if type(htt) == list:
                # 遍历数组的值
                for li in htt:
                    # 把htt分隔
                    for i in li:
                        separate = i.split('=')
                        # 保证一行只能存在一个相同参数
                        if separate[0] not in marks:
                            file_new.write(i)
                            marks.append(separate[0])
                        else:
                            file_new.write('\n' + i)
                    # 执行结束换行
                    file_new.write('\n')
        file_new.write('\n')
        return marks
    except Exception as e:
        logger.write_log('re_htt 出错了: ' + str(e))
        return []
