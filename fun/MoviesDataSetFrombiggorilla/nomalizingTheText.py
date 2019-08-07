#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 10:36
# @Author  : legend
import fun.MoviesDataSetFrombiggorilla.extractingTheInformation

def preprocess_title(title):
    # 转换字符串中所有大写字符为小写
    title = title.lower()
    title = title.replace(',', ' ')
    title = title.replace("'", '')
    title = title.replace('&', '')
    title = title.replace('?', '')
    title = title.decode('utf-8', 'ignore')
    return title.strip()
