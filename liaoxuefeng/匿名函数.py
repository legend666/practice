#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 10:52
# @Author  : legend

def multipliers():
    return [lambda x: i * x for i in range(4)]

for m in multipliers():
    print(m)

