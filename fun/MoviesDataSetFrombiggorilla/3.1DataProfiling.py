#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:53
# @Author  : legend

import pandas as pd
# 引用其他py文件
from fun.MoviesDataSetFrombiggorilla import extractingTheInformation

genres_data = extractingTheInformation.genres_data()
ratings_data = extractingTheInformation.ratings_data()
kaggle_data = pd.read_csv('./data/kaggle_dataset.csv')
print('Number of movies in kaggle_data:{}'.format(kaggle_data.shape[0]))
print('number of movies in genres_data:{}'.format(genres_data.shape[0]))
print('number of movies in retings_data:{}'.format(ratings_data.shape[0]))