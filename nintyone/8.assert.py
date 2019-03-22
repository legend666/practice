#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 20:03
# @Author  : legend

# assert  调试程序服务；检查程序异常或者不恰当的输入
# 语法：assert expression1 [","expression2]
x = 1
y = 2
assert x == y, "not equals"
# 相当于：
if __debug__ and not x == y:
    raise AssertionError("not equals")
# (1) __debug__的值默认值是true，且是只读的，2.7中还无法修改
