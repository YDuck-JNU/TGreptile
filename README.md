# 获取TG的活动的脚本
国外环境使用

```text
/ 调整时间更新项目
/qlcs 活动接口
/sql 数据库
/sql/add 添加
/sql/del 删除
```
```shell
docker run -dit \
  -p 5000:5000 \
  -e TZ=Asia/Shanghai \
  --name tgs \
  --restart unless-stopped \
  xgzk/tgreptile:latest
```