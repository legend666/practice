#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 14:18
# @Author  : legend
# 学过的都喂了狗...再写一遍吧
# dict和list比，查询和插入的速度极快，但是需要占用大量内存
# https://www.cnblogs.com/anita-harbour/p/9328614.html
# key必须是可散列的，不可变的都是可以散列的
dic = {}
dic['adam'] = 777
dic['legend'] = 666
print(dic.keys())  # dict_keys(['adam', 'legend'])
print(dic.pop('adam'))  # 777
print(dic.clear())
