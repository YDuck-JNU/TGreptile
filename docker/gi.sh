# shellcheck disable=SC2164
if [ -d "/TGreptile" ];then
  cd /TGreptile
else
  echo "检测到文件存在不再拉取新项目"
  cd /
fi
git clone https://github.com/XgzK/TGreptile.git
# shellcheck disable=SC2046
kill -9 $(netstat -nlp | grep :5000 | awk '{print $7}' | awk -F'/' '{ print $1 }')
echo 杀死了端口5001等待自动启动