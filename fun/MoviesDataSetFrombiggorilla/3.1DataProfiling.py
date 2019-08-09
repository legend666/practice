#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:53
# @Author  : legend

import pandas as pd
# 引用其他py文件
from fun.MoviesDataSetFrombiggorilla import extractingTheInformation

genres_data = extractingTheInformation.genres_data()
# print(type(genres_data)) <class 'pandas.core.frame.DataFrame'>
ratings_data = extractingTheInformation.ratings_data()
kaggle_data = pd.read_csv('./data/kaggle_dataset.csv')
print('Number of movies in kaggle_data:{}'.format(kaggle_data.shape[0]))
print('number of movies in genres_data:{}'.format(genres_data.shape[0]))
print('number of movies in retings_data:{}'.format(ratings_data.shape[0]))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html

print('Number of duplicates in kaggle_data: {}'.format(
    sum(kaggle_data.duplicated(subset=['movie_title', 'title_year'], keep=False))))
print('Number of duplicates in genres_data: {}'.format(
    sum(genres_data.duplicated(subset=['movie', 'year'], keep=False))))
print('Number of duplicates in ratings_data: {}'.format(
    sum(ratings_data.duplicated(subset=['movie', 'year'], keep=False))))

# Number of movies in kaggle_data:5043
# number of movies in genres_data:2658930
# number of movies in retings_data:789414
# Number of duplicates in kaggle_data: 241
# Number of duplicates in genres_data: 2031345
# Number of duplicates in ratings_data: 342819
