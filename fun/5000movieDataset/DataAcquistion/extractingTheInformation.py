#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 10:11
# @Author  : legend
import re
import pandas as pd

# with open("./data/genres.list", 'rb') as genres_file:
#     rew_content = genres_file.readlines()
#     genres_list = []
#     content = rew_content[382:]
#     for line in content:
#         m = re.match(r'"?(.*[^"])"? \(((?:\d|\?){4})(?:/\w*)?\).*\s((?:\w|-)+)', line.strip())
#         genres_list.append([m.group(1), m.group(2), m.group(3)])
#     genres_data = pd.DataFrame(genres_list, columns=['movie', 'year', 'genre'])
#     print(genres_data)

with open("./data/ratings.list") as ratings_file:
    raw_content = ratings_file.readlines()
    ratings_list = []
    content = raw_content[28:]
    for line in content:
        m = re.match(r'(?:\d|\.|\*){10}\s+\d+\s+(1?\d\.\d)\s"?(.*[^"])"? \(((?:\d|\?){4})(?:/\w*)?\)', line.strip())
        if m is None: continue
        ratings_list.append([m.group(2), m.group(3), m.group(1)])
    ratings_data = pd.DataFrame(ratings_list, columns=['movie', 'year', 'rating'])
