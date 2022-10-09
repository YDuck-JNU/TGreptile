import json

from com.xgz.gheaders.conn import read_yaml, read_txt
from com.xgz.gheaders.log import LoggerClass
from com.xgz.gheaders.ti import fast_forward
from com.xgz.jd.jd_filter import jd_sql
from com.xgz.sql.JD_ql import select_data
from com.xgz.sql.sign import to_select

logger = LoggerClass('debug')
yml = read_yaml()


def tx_compared():
    """
    用于对比数据，由TG获取的文本对比数据库中的数据
    :return: 返回数组的脚本名称[0]和变量[1],异常返回-1
    """
    try:
        # 用来去重复
        lis = []
        # 读取文件内容
        tx = read_txt(yml['path'])
        # 用来存储脚本名称和变量的
        script = []
        variable = []
        # 获取时间用于判断
        ti = fast_forward()
        # 根据获取的时间判断是否是凌晨
        if ti[0] <= yml['js'][0][2] <= ti[1]:
            # 查询数据库中有没有数据
            sesql = to_select()
            if len(sesql) > 0:
                sessql = jd_sql()
                for i in sessql:
                    script.append(yml['js'][0][0])
                    variable.append(yml['js'][0][1] + '="' + i + '"')
                # 不等于-1说明有数据
                # if sessql != -1:
                #     script.append(yml['js'][0][0])
                #     variable.append(yml['js'][0][1] + '=' + sessql)

        for i in tx:
            # 判断是不是在数组中存在去重复处理
            if not i in lis and len(i) > 7:
                lis.append(i)
            else:
                continue
            # 切割字符串
            if i[0:6:1] == 'export' or i[0:9:1] == 'NOTexport':
                # 把export DPLHTY="b4be"的键和值分开
                tx = i.split('=')
                # 先查询这个值在不在jd_value1中
                value1 = select_data('jd_js', f'jd_value1="{tx[0]}"')
                if len(value1) > 0:
                    # 下面是js和名称
                    script.append(value1[0][0])
                    variable.append(i)
                    # 跳过本次执行
                    continue
                # 再查询这个值在不在jd_value2中
                value2 = select_data('jd_js', f'jd_value2="{tx[0]}"')
                if len(value2) > 0:
                    # 下面是js和名称
                    script.append(value2[0][0])
                    variable.append(i)
                    # 跳过本次执行
                    continue
                # 再查询这个值在不在jd_value3中
                value3 = select_data('jd_js', f'jd_value3="{tx[0]}"')
                if len(value3) > 0:
                    # 下面是js和名称
                    script.append(value3[0][0])
                    variable.append(i)
                    # 跳过本次执行
                    continue
                i = i.replace('\n', '')
                logger.write_log(f'数据库没有找到: {i}')
        # 清空数组
        lis.clear()
        return [script, variable]
    except Exception as e:
        logger.write_log("tx_compared 异常信息: " + str(e))
        return -1


def htm(js, va):
    """
    用脚本名称和变量来传输
    :param js: 脚本名称
    :param va: 需要添加的值
    :return:
    """
    try:
        pathtx = yml['htmltx']
        # 打开并清空写入文件
        a_file = open(pathtx, "w+", encoding="utf-8")
        jsotx = {}
        if js != -1:
            if len(js) > 0:
                for i in range(len(js)):
                    jsotx[i] = js[i] + '\n' + va[i]
                json.dump(jsotx, a_file)
                logger.write_log("对比数据,并且保存json成功,添加的数据有: " + str(jsotx))
            else:
                # 没有数据添加空
                json.dump('{}', a_file)
                logger.write_log("没有脚本名称和变量")
            a_file.close()
        else:
            # 没有数据添加空
            json.dump('{}', a_file)
            logger.write_log("没有脚本名称和变量")
            a_file.close()
    except Exception as e:
        logger.write_log("用脚本名称和变量来传输: " + str(e))


def add_null():
    """
    添加空的数据到json文件
    :return:
    """
    try:
        pathtx = yml['htmltx']
        a_file = open(pathtx, "w", encoding="utf-8")
        json.dump('{}', a_file)
        # log_ip("没有脚本名称和变量")
        a_file.close()
    except Exception as e:
        logger.write_log("用脚本名称和变量来传输: " + str(e))


def txt_main():
    """
    执行对比数据，并且保存json
    :return:
    """
    try:
        txt = tx_compared()
        if txt != -1:
            htm(txt[0], txt[1])
        else:
            htm(txt, ' ')
    except Exception as e:
        logger.write_log('txt_main,异常问题: ' + str(e))
