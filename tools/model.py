# !/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from peewee import *

path = 'ip.sqlite'
db = SqliteDatabase(path)


class BaseModel(Model):
    class Meta:
        database = db


class Proxy_IP(BaseModel):
    ip = CharField(primary_key=True, max_length=25, verbose_name='ip地址')
    http_s = CharField(default='http', verbose_name='协议')
    status = CharField(default='1', verbose_name='状态')
    created = DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'ip'


if __name__ == '__main__':
    try:
        Proxy_IP.create_table()
        print('created success, path is %s' % path)
    except Exception as err:
        print(err)
