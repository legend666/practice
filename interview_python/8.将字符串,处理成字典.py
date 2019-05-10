#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 10:55
# @Author  : legend

str1 = "k:1|k1:2|k2:3|k3:4|k4:5"


def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key, value = iterms.split(':')
        dict1[key] = value
    return dict1


# 字典推导式 d = {key:value for (key,value) in iterable}
d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
print(d)
