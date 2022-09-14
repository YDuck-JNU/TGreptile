#!/bin/sh
while true
do
    # 停止返回0 正常返回1
    # shellcheck disable=SC2009
    # shellcheck disable=SC2126
    stillRunning=$(ps -ef |grep app.py  |grep -v "grep" |wc -l)
    if [ "$stillRunning" ]; then
      echo 程序死亡开始执行
       cd /TGreptile && python3 app.py
    else
      echo 请等待3000秒后执行;
      sleep 3000;
    fi
done