# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
sys.path.append('..')

import requests
from lxml.etree import HTML
import gevent
from gevent import monkey
monkey.patch_all()

from .crawler import crawler, _filter
from .model import Proxy_IP
from .dumblog import dlog
logger = dlog(__file__)


def xicidaili():
    url = 'http://www.xicidaili.com/nn/'
    html = crawler(url, 'lxml')
    if isinstance(html, str):
        return
    print(type(html))
    for i in range(2, 101):
        ip = _filter(html.xpath('//*[@id="ip_list"]//tr[%s]//td[2]//text()' % str(i)))
        port = _filter(html.xpath('//*[@id="ip_list"]//tr[%s]//td[3]//text()' % str(i)))
        http_s = _filter(html.xpath('//*[@id="ip_list"]//tr[%s]//td[6]//text()' % str(i))).lower()
        save(ip, port, http_s)


def cnproxy():
    urls = ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
    for url in urls:
        html = crawler(url, 'lxml')
        ips = html.xpath('//*[@class="sortable"]/tbody/tr/td[1]/text()')
        https = html.xpath('//*[@class="sortable"]/tbody/tr/td[2]/text()')
        for i in range(len(ips)):
            save(ips[i], https[i], 'http')


def kuaidaili():
    for i in range(1, 10):
        url = 'http://www.kuaidaili.com/free/inha/%s/' % str(i)
        crawlkuaidaili(url)


def crawlkuaidaili(url):
    html = crawler(url, 'lxml')
    tem = html.xpath('//*[@id="list"]//table//tr/td//text()')
    for i in range(len(tem)):
        if len(re.findall('\.', tem[i])) == 3:
            save(tem[i], tem[i + 1], 'http')


def xdaili():
    url = 'http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10'
    rep = crawler(url)
    tem = rep.json().get('RESULT').get('rows')
    for t in tem:
        save(t.get('ip'), t.get('port'), 'http')


def ip66():
    url = 'http://www.66ip.cn/'
    headers = {
        'Referer':
        'http://www.66ip.cn/',
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    rep = requests.get(url, headers=headers)
    html = HTML(rep.content)
    tem = html.xpath('//*[@class="textlarge22"]//li/a/@href')
    print(tem)
    for t in tem:
        if 'http://www.66ip.cn' not in t:
            url = 'http://www.66ip.cn%s' % t
            ip66_detail(url, headers)


def ip66_detail(url, headers):
    rep = requests.get(url, headers=headers)
    html = HTML(rep.content)

    tem = html.xpath('//*[@align="center"]/table/tr')
    for i in range(2, len(tem)):
        ip = _filter(html.xpath('//*[@align="center"]/table/tr[%s]/td[1]/text()' % str(i)))
        port = _filter(html.xpath('//*[@align="center"]/table/tr[%s]/td[2]/text()' % str(i)))
        save(ip, port, 'http')


def save(ip, port, http_s):
    try:
        Proxy_IP.create(
            ip='%s:%s' % (ip, port),
            http_s=http_s,
        )
        logger.info('save success, ip : {}'.format(ip + ':' + port))
    except Exception as err:
        logger.info(err)


def proxy():
    if not os.path.exists('ip.sqlite'):
        Proxy_IP.create_table()
    function = [xicidaili, cnproxy, kuaidaili, xdaili, ip66]
    jobs = [gevent.spawn(func, ) for func in function]
    gevent.joinall(jobs)

    # https://proxy.mimvp.com/free.php?proxy=in_hp pic
    # http://www.goubanjia.com/index1.shtml
    # http://lab.crossincode.com/proxy/

    # */5 * * * * cd $HOME/spider && python common/proxy.py


if __name__ == "__main__":
    proxy()
