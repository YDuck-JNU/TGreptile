"""
此页面主要用于筛选京东需要的数据
"""
from com.xgz.gheaders.log import LoggerClass
from com.xgz.jd.dp import shop_sign
from com.xgz.sql.sign import to_select, to_delete

logger = LoggerClass('debug')


def jd_sql(txt=None):
    """
    用于查询和执行sql语句,None默认执行不检测
    :return: 返回数组
    """
    try:
        # 存储多个分开数据
        str1 = []
        # 查询数据库中的数据
        sesql = to_select()
        # 用于拼接和记录次数
        st = ''
        sun = 1
        # 循环查询结果
        for i in sesql:
            if sun != 6:
                # 把i[0]拼接到str1中
                st += i[0] + '&'
                # 每次加一
                sun += 1
            else:
                # 添加数组并取消最后一个&
                str1.append(st[:-1])
                # 初始化
                sun = 1
                st = ''
            # 如果不是None则表示检测店铺签到
            if txt is not None:
                shop = shop_sign(i[0])
                # 返回0表示修改成功，1表示修改失败
                if shop == 402 or shop == -1:
                    logger.write_log(f"删除失效店铺签到: {i[0]}")
                    to_delete(i[0])
                continue
                # 如果是数组里面最后一个不满足一组则
        if st != '':
            str1.append(st[:-1])
        # 检查str1是否为空
        if len(str1) != 0:
            return str1
        else:
            return []
    except Exception as e:
        logger.write_log("jd_sql,异常信息: " + str(e))
        return []
