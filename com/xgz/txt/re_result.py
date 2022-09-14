from com.xgz.gheaders.log import LoggerClass
from com.xgz.txt.deal_with import export_https, export_txt, https_txt
logger = LoggerClass('debug')

def re_exht(file_new, exht, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的export_https的内容
    :param file_new: 文件对象
    :param exht: 匹配到的内容
    :param marks: 去重用的标记
    :return: 正常返回marks, 否则返回-1
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
        # 把带参数用于标记
        return marks
    except Exception as e:
        logger.write_log('re_exht 出错了: ' + str(e))
        return -1


def re_extx(file_new, extx, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的export_txt的内容
    :param file_new: 文件对象
    :param extx: 文本内容
    :param marks: 去重用的标记
    :return: 正常返回marks, 否则返回-1
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
        return marks
    except Exception as e:
        logger.write_log('re_extx 出错了: ' + str(e))
        return -1


def re_htt(file_new, htttx, marks):
    """
    用与修改文本,只保留关键字到文本，处理的是txt_zli.py中的https_txt的内容
    :param file_new: 文件对象
    :param htttx: 匹配到的内容
    :param marks: 去重用的标记
    :return: 正常返回marks, 否则返回-1
    """
    try:
        # 使用这个循环是防止有人不换行把内容都放在一行
        for ht in htttx:
            htt = https_txt(ht)
            if htt != -1:
                # 把htt分隔
                separate = htt.split('=')
                # 保证一行只能存在一个相同参数
                if separate[0] not in marks:
                    file_new.write(htt)
                    marks.append(separate[0])
                else:
                    file_new.write('\n' + htt)
        return marks
    except Exception as e:
        logger.write_log('re_htt 出错了: ' + str(e))
        return -1