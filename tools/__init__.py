#!/usr/bin/env python
# -*- coding: utf-8 -*-

# See details at
# http://192.168.2.3/jinlong/tools

from .crawler import crawler, _filter
from .dumblog import dlog
from .pipeline import pipe, _try, multi, Setting
from .proxy import proxy
from .redisq import RedisQueue

__author__ = 'jinlong'
__all__ = ['crawler', '_filter', 'dlog', 'pipe', '_try', 'multi', 'RedisQueue', 'Setting', 'proxy']

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
