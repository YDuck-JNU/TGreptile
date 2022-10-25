# 获取TG的活动的脚本
国外环境使用
此项目停止维护正式并入活动子端，活动端完美兼容后会删库
```text
/ 调整时间更新项目
/qlcs 活动接口
/sql 数据库
/sql/add 添加
/sql/del 删除
/sql/delt 删除店铺tk
```
```shell
docker run -dit \
  -p 5000:5000 \
  -e TZ=Asia/Shanghai \
  --name tgs \
  --restart unless-stopped \
  xgzk/tgreptile:latest
```
## 版本记录
1.1版本
```text
优化了HTTPS链接的由原来一个结束到现在遍历所有数据库结束
对比方法没有内容统一返回空数组
会获取变量里面的HTTPS链接再自己转换,子端因为有去重复处理暂时不考虑去重复
对本次值进行去重复处理
添加post数据库接口 /sql
取消了店铺签到的定时检测改用手动删除
```
