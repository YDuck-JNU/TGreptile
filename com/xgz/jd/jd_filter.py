"""
此页面主要用于筛选京东需要的数据
"""
from com.xgz.gheaders.log import LoggerClass
from com.xgz.jd.dp import shop_sign
from com.xgz.sql.sign import to_select, to_delete

logger = LoggerClass('debug')


def jd_sql(txt=None):
    """
    用于查询和执行sql语句
    :return:
    """
    try:
        # 用于拼接
        str1 = ''
        # 查询数据库中的数据
        sesql = to_select()
        # 循环查询结果
        for i in sesql:
            # 把i[0]拼接到str1中
            str1 += i[0] + '&'
            # 如果不是None则表示检测店铺签到
            if txt is not None:
                shop = shop_sign(i[0])
                # 返回0表示修改成功，1表示修改失败
                if shop == 402 or shop == -1:
                    logger.write_log(f"删除失效店铺签到: {i[0]}")
                    to_delete(i[0])
                continue
        # 检查str1是否为空
        if str1 != '':
            # 如果不为空，则去掉最后一个&
            return '"' + str1[:-1] + '"'
        else:
            return -1
    except Exception as e:
        logger.write_log("jd_sql,异常信息: " + str(e))
        return -1
