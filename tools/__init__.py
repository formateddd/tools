# from gevent import monkey
# monkey.patch_all()

from .crawler import crawler, _filter
from .dumblog import dlog
from .pipeline import pipe, _try, multi, Setting
from .redisq import RedisQueue

# if use proxy, cp proxy.py to your file
# from .proxy import proxy

__author__ = 'jinlong'
__all__ = ['crawler', '_filter', 'dlog', 'pipe', '_try', 'multi', 'RedisQueue', 'Setting']

# setting.yaml :

# Cookie :

# time_sleep : 1

# sleep_min : 1
# sleep_max : 2

# host : ''
# user :
# password :
# database :

# mysql_host :
# mysql_user :
# mysql_passwd : ''
# mysql_db :

# redis_ip: 127.0.0.1
# redis_port: 6379
# redis_pass:
# redis_db: 1

# queue_timeout: 5
