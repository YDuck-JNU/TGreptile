from flask import Blueprint, request, render_template

from com.xgz.sql.JD_ql import select_data, insert_data, delete_one_data

app = Blueprint('sql', __name__)


@app.route('/add', methods=['GET', 'POST'])
def register():
    # id, jd_name, jd_js, jd_value1, jd_value2=None, jd_value3=None, jd_url=None, jd_re=None
    if request.method == 'POST':
        id = select_data()
        print("获取ID", id)
        print('===================================')
        jd_name = request.form.get('jd_name')
        jd_js = request.form.get('jd_js')
        jd_value1 = request.form.get('jd_value1')
        jd_value2 = request.form.get('jd_value2')
        jd_value3 = request.form.get('jd_value3')
        jd_url = request.form.get('jd_url')
        jd_re = request.form.get('jd_re')
        sun = 0
        for i in id:
            if i[0] != sun:
                break
            else:
                sun += 1
        if sun == len(id) and sun != 0:
            sun += 1
        print(sun)
        # 开始校验是否符合要求
        if jd_name != '' and jd_js != '' and jd_value1 != '':
            sql = insert_data(sun, jd_name, jd_js, jd_value1, jd_value2, jd_value3, jd_url, jd_re)
            if sql == 0:
                return '插入成功'
            else:
                return str(sql)
        else:
            return '请传入正确的参数'
    return render_template('add.html')


@app.route('/del', methods=['GET', 'POST'])
def dele():
    if request.method == 'POST':
        str1 = ''
        id = request.form.get('ID')
        id = id.split(" ")
        for i in id:
            de = delete_one_data('id', i)
            if de != 0:
                str1 += str(de) + "删除失败 ID是" + str(i) + '<br>'
        if len(str1) == 0:
            return "删除成功"
        else:
            return str1 + "删除失败"
    else:
        return render_template('del.html')
