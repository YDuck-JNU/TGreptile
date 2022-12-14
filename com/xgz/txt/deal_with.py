"""
此脚本用于处理txt文件里面的数据，并且二次加工
"""
import re

from com.xgz.gheaders.log import LoggerClass
from com.xgz.sql.JD_ql import select_data
from com.xgz.txt.inquire import fuzzy_query

logger = LoggerClass('debug')


# def export_https(exht):
#     """
#     处理export \w+="<a href="https://.*?"这种格式
#     :param exht: 待处理的数据
#     :return: 处理后的行，异常返回-1
#     """
#     try:
#         # 用来区分有没有"<a href=
#         hre = re.findall('"<a href=',exht)
#         if hre:
#             return exht
#     except Exception as e:
#         logger.write_log("export_https，异常问题: " + str(e))
#         return -1


def export_txt(extx):
    """
    处理export \w+="\w+"这种格式
    :param extx: 待处理的数据
    :return: 处理后的行，异常返回-1
    """
    try:
        # 把extx分隔，去除中间的"="
        # 按=分隔
        separate = extx.split('=')

        # 去除separate[1]前后的",避免有的值有有的没有
        separate[1] = separate[1].replace('"', '')
        # 程序第一个值是不是和自己相识
        sq = select_data(data='jd_value1', value=f'jd_value1="NOT{separate[0]}"')
        # print('查询的结果是', sq)
        if len(sq) > 0:
            # 获取设置得正则表达式
            separate[0] = 'NOT' + separate[0]
        # 把两端重新拼接并且返回
        return str(separate[0]) + '="' + str(separate[1]) + '"'
    except Exception as e:
        logger.write_log("export_txt，异常问题: " + str(e))
        return -1


def https_txt(http):
    """
    处理.*?>(https://.*?\?\w+=\w+)</a>
    :param http: 待处理的数据
    :return: 处理后的二维list，异常返回-1
    """
    try:
        # 先查询是否存有这个链接
        li = fuzzy_query(http)
        # 判断返回的是不是数组类型
        if type(li) == list:
            # 用于存放多个活动值
            lis = []
            for ink in li:
                # 当有正则表达式的时候，使用正则表达式获取需要的值
                if ink[4] is not None and ink[4] != "":

                    try:
                        # 调用正则表达式进行取值
                        htt3 = re.findall(f'{ink[4]}', http)
                        if len(htt3) > 0:
                            # 如果Ink[3] 不为空表示这个链接获取的是三个值
                            if ink[3] is not None and ink[3] != "":
                                lis.append([ink[1] + '="' + htt3[0][0] + '"', ink[2] + '="' + htt3[0][1] + '"',
                                            ink[3] + '="' + htt3[0][2] + '"'])
                            elif ink[2] is not None and ink[2] != "":
                                lis.append([ink[1] + '="' + htt3[0][0] + '"', ink[2] + '="' + htt3[0][1] + '"'])
                            elif ink[1] is not None and ink[1] != "":
                                # 正常不去重复的值都是一个
                                sq = select_data(data='jd_value1', value=f'jd_value1="NOT{ink[1]}"')
                                if len(sq) == 1:
                                    # 获取设置得正则表达式
                                    ink[1] = 'NOT' + ink[1]
                                lis.append([ink[1] + '="' + htt3[0] + '"'])
                        else:
                            logger.write_log("https_txt,正则表达式没有匹配到值:  " + str(http))
                    except Exception as e:
                        logger.write_log(f"https_txt,异常问题:  {str(e)}, 问题活动 {http} 问题脚本 {ink[1]}")
                else:
                    logger.write_log("https_txt,正则表达式没有匹配到值:  " + str(http))
            # 如果有值返回数组,没有返回-1
            return lis if len(lis) != '' else -1
        return -1
    except Exception as e:
        logger.write_log("https_txt,异常问题: " + str(e))
        return -1
