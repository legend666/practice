#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:03
# @Author  : legend

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
# 调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# with open()不用调用try，finally，而且不用.close方法
# 遇到非法编码的字符，可以直接忽略，errors = "ignore"
# with open('',endcoding ='gbk',errors='ignore')
# 模式定义以及含义等看文档
# https://docs.python.org/3/library/functions.html#open
