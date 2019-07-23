#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:02
# @Author  : legend
import os
import sys
from urllib import request

# def _progress(block_num, block_size, total_size):
#     '''回调函数
#        @block_num: 已经下载的数据块
#        @block_size: 数据块的大小
#        @total_size: 远程文件的大小
#     '''
#     sys.stdout.write('\r>> Downloading %s %.1f%%' % (filename,
#                      float(block_num * block_size) / float(total_size) * 100.0))
#     sys.stdout.flush()

imdb_url = 'https://anaconda.org/BigGorilla/datasets/1/download/imdb_dataset.csv'
if not os.path.exists('./data/imdb_dataset.csv'):  # avoid downloading if the file exists
    response = request.urlretrieve(imdb_url, './data/imdb_dataset.csv')
# urllib.error.HTTPError: HTTP Error 403: Forbidden
