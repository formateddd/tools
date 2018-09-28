# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import sys
sys.path.append('..')

import requests
from peewee import fn
from lxml import etree
# from tenacity import retry
# from fake_useragent import UserAgent

from .pipeline import Setting, multi
from .model import Proxy_IP

# from .dumblog import dlog
# logger = dlog(__file__)


def crawler(url, r='', pro=None, ua='', method='get', data={}):
    print(url)

    if ua == 'mobile':
        UA = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
    elif :
        if Setting.ua == '':
            print('using default User Agent')
            # UA = UserAgent(verify_ssl=False).random
            UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        else:
            UA = Setting.ua


    headers = {
        'Cookie': Setting.Cookie,
        'User-Agent': UA,
        'Host': Setting.Host,
        'Referer': Setting.Referer,
    }

    function = {
        'get': requests.get,
        'post': requests.post,
    }
    req = function.get(method)

    item = {
        'url': url,
        'req': req,
        'r': r,
        'pro': pro,
        'headers': headers,
        'data': data,
    }
    if pro:
        response = proxy_crawler(item)
    else:
        response = normal_crawler(item)

    if isinstance(response, str) or response.status_code != 200:
        time.sleep(int(Setting.sleep_max))
        print('return error : %s' % item.get('url'))
        return
        # return crawler(url, r, pro)

    ret = {
        '': response,
        'content': response.content,
        'text': response.text,
        'lxml': etree.HTML(response.text),
        'con-lxml': etree.HTML(response.content),
    }

    return ret.get(r)


def proxy_crawler(item):
    # print(item)
    try:
        proxyip = Proxy_IP.select().where(Proxy_IP.status == '1').order_by(fn.random()).get()
    except Exception as err:
        print(err)
        return crawler(item.get('url'), item.get('r'))
    proxies = {
        proxyip.http_s.strip(): proxyip.http_s + '://' + proxyip.ip.strip(),
    }

    try:
        response = item.get('req')(
            item.get('url'),
            headers=item.get('headers'),
            data=item.get('data'),
            timeout=20,
            proxies=proxies)
    except Exception as err:
        multi(update_ip, proxyip)
        # update_ip(proxyip)
        return proxy_crawler(item)
    print(
        'proxies ip: %s, status_code: %s' % (proxyip.ip, response.status_code))
    time.sleep(0.3)
    return response


def normal_crawler(item):
    try:
        response = item.get('req')(
            item.get('url'),
            headers=item.get('headers'),
            data=item.get('data'),
            timeout=15)
    except Exception as err:
        print(err)
        time.sleep(300)
        return item.get('url')
    print('status_code : %s' % response.status_code)
    time.sleep(random.randint(int(Setting.sleep_min), int(Setting.sleep_max)))
    if response.status_code != 200:
        time.sleep(int(Setting.sleep_max))
        print('return error : %s' % item.get('url'))
        return item.get('url')
    else:
        return response


def get_proxy_ip():
    try:
        proxyip = Proxy_IP.select().where(Proxy_IP.status == '1').order_by(fn.random()).get()
        return proxyip
    except Exception as err:
        print(err)
        return


def update_ip(proxyip):
    url = 'https://www.baidu.com/'
    proxies = {
        proxyip.http_s.strip(): proxyip.http_s + '://' + proxyip.ip.strip(),
    }
    try:
        resp = requests.get(url, proxies=proxies)
        if resp.status_code == 200:
            print('crawl baidu proxy ip:%s, %s' % (proxyip.ip, resp.status_code))
            return

        q = Proxy_IP.update(status='0').where(Proxy_IP.ip == proxyip.ip)
        q.execute()
        print('proxy update success %s' % str(proxyip.ip))
    except Exception as err:
        print(err)


def _filter(lis, word=''):
    if len(lis) == 0:
        return ''
    elif len(lis) == 1:
        if lis[0] == '':
            return ''
        else:
            return lis[0].strip()
    elif len(lis) > 1:
        return word.join(lis).replace('  ', '').replace('\r', '').replace('\n', '').strip()
