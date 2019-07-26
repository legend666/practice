#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:00
# @Author  : legend
import urllib
from urllib import request

import bs4
from bs4 import BeautifulSoup


def get_html(url):
    html = urllib.request.urlopen(url)
    content = html.read
    html.close()
    soup = BeautifulSoup(content, "lxml")
    table = soup.find('tbody')
    count = 0
    lst = []
    for tr in table.children:n hhh
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')
            if count >= 2:
                lst.append()
    print(table)


if __name__ == '__main__':
    url = 'http://gaokao.xdf.cn/201702/10612921.html'
    get_html(url)
