#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:00
# @Author  : legend
import urllib
from urllib import request
import MySQLdb
import bs4
from bs4 import BeautifulSoup


def get_html(url):
    html = urllib.request.urlopen(url)
    content = html.read()
    html.close()
    soup = BeautifulSoup(content, "lxml")
    table = soup.find('tbody')
    lst = []
    for tr in table.children:
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')
            university = []
            for i in range(5):
                if td[i].string is not None:
                    university.append(td[i].string.replace('\n', '').replace('\t', ''))
            lst.append(university)
    return lst[1:-2]


if __name__ == '__main__':
    url = 'http://gaokao.xdf.cn/201812/10838484.html'
    universities_list = get_html(url)
    # 建立mysql数据库连接
    db = MySQLdb.connect("localhost", "root", "123456", "university", charset='utf8')
    # 使用cursor方法获取操作游标
    cursor = db.cursor()
    cursor.execute("SET NAMES utf8")
    # 使用execute方法执行SQL语句
    cursor.execute("""create table if not exists university_rank(排名 int(3),高校 varchar(20),总分 decimal(9,2),
                                            星级排名 varchar(8),办学层次 varchar(40)) default charset = utf8""")
    for university in universities_list:
        sql = "insert into university_rank values('%s', '%s', '%s', '%s', '%s')" % (
            university[0], university[1], university[2], university[3], university[4])
        cursor.execute(sql)
    # 提交
    db.commit()
    db.close()
