# shellcheck disable=SC2164
if [ -d "/TGreptile" ];then
  cd /TGreptile
  git fetch --all
  git reset --hard
  git pull https://github.com/XgzK/TGreptile.git
#else
#  echo "检测到文件不存在拉取新项目"
#  cd /
#  git clone https://github.com/XgzK/TGreptile.git
fi
# shellcheck disable=SC2046
kill -9 $(netstat -nlp | grep :5000 | awk '{print $7}' | awk -F'/' '{ print $1 }')
cd /TGreptile
pip3 install -r requirements.txt
echo 杀死了端口5001等待自动启动