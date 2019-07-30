#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:39
# @Author  : legend
import gzip
import os
from urllib import request

# imdb_url_prefix = 'ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/frozendata/'
# imdb_files_list = ['genres.list.gz', 'ratings.list.gz']
# for name in imdb_files_list:
#     if not os.path.exists('./data/' + name):
#         response = request.urlretrieve(imdb_url_prefix + name, './data/' + name)
#         request.urlcleanup()
#         with gzip.open('./data/' + name) as comp_file, open('./data/' + name[:-3], 'w') as reg_file:
#             file_content = comp_file.read()
#             reg_file.write(file_content)

with gzip.open('./data/ratings.list.gz', encoding='utf-8') as comp_file, open('./data/ratings.list', 'w') as reg_file:
    file_content = comp_file.read()
    reg_file.write(file_content)
