#!/usr/bin/env python
# coding=utf-8

from tools import crawler, proxy, _try, multi

# crwaler函数接受的参数
# url: 需要爬的url
# r: return的类型
# pro: 如不用代理为空，否则pro='p'
# 详情参见crawler.py

# 关于解析内容和保存
# 解析可选xpath，网上可以搜到很多，ex：https://blog.csdn.net/zgkli6com/article/details/17491479
# 关于保存到数据库，我选择用peewee，大致用法参见model.py；或者调用sql语句直接存储

# 关于redis
# redis_url = RedisQueue('url', host=Setting.redis_ip, port=Setting.redis_port, password=Setting.redis_pass, db=Setting.redis_db)
# 需要往redis存时， redis_url.put(url)
# 需要拿出时，调用pipe，且函数的参数必须为param

def test_crawler():
    url = 'https://www.baidu.com'
    rep = crawler(url, r='', pro='')
    print(rep.status_code)


def test():
    for i in range(3):
        print(i)
    print(j)


if __name__ == '__main__':
    test_crawler()
    _try(test())
    multi(proxy)
