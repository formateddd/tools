### 把常用包安装到python环境（最好是已经建好的虚拟环境）里
### 避免在项目文件里引用时出现的路径问题
```sh
pip install git+https://github.com/killmymates/tools
```

### 新建settings.yaml文件，写入以下内容，设置对应的参数
```yaml

Cookie :

time_sleep : 2

sleep_min : 1
sleep_max : 5

host : ''
user :
password :
database :

mysql_host :
mysql_user :
mysql_passwd : ''
mysql_db :

redis_ip: 127.0.0.1
redis_port: 6379
redis_pass:
redis_db: 1

queue_timeout: 5

```
### 详细用法参见test_tools.py
