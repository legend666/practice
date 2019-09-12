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
# shape[第一维度的长度，就是有多少条信息]
# print('Number of movies in kaggle_data:{}'.format(kaggle_data.shape[0]))
# print('number of movies in genres_data:{}'.format(genres_data.shape[0]))
# print('number of movies in retings_data:{}'.format(ratings_data.shape[0]))

# Number of movies in kaggle_data:5043
# number of movies in genres_data:2658930
# number of movies in retings_data:789414
"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
DataFrame.duplicated(self, subset=None, keep='first')
return boolean series denoting duplicate rows,optionally only considering certain columns
返回布尔级数，表示重复的行，只考虑某些列
parameters:
keep:{'first', mark duplicated as true except for the first occurrence 除第一次出现外，标记复制为true
    'last', mark duplicated as true expect for the last occurrence
    'False'  mark all duplicated as true
    }
returns:series
"""
# print('Number of duplicates in kaggle_data: {}'.format(
#     sum(kaggle_data.duplicated(subset=['movie_title', 'title_year'], keep=False))))
# print('Number of duplicates in genres_data: {}'.format(
#     sum(genres_data.duplicated(subset=['movie', 'year'], keep=False))))
# print('Number of duplicates in ratings_data: {}'.format(
#     sum(ratings_data.duplicated(subset=['movie', 'year'], keep=False))))

# Number of duplicates in kaggle_data: 241
# Number of duplicates in genres_data: 2031345
# Number of duplicates in ratings_data: 342819
# Number of movies in kaggle_data:5043
# number of movies in genres_data:2658930
# number of movies in retings_data:789414
kaggle_data = kaggle_data.drop_duplicates(subset=['movie_title', 'title_year'], keep='first').copy()
genres_data = genres_data.drop_duplicates(subset=['movie', 'year'], keep='first').copy()
ratings_data = ratings_data.drop_duplicates(subset=['movie', 'year'], keep='first').copy()
print('Number of drop_duplicates in kaggle_data:{}'.format(kaggle_data.shape[0]))
print('number of drop_duplicates in genres_data:{}'.format(genres_data.shape[0]))
print('number of drop_duplicates in retings_data:{}'.format(ratings_data.shape[0]))


# Number of drop_duplicates in kaggle_data:4919
# number of drop_duplicates in genres_data:1398367
# number of drop_duplicates in retings_data:465510

def preprocess_title(title):
    # 转换字符串中所有大写字符为小写
    title = title.lower()
    title = title.replace(',', ' ')
    title = title.replace("'", '')
    title = title.replace('&', '')
    title = title.replace('?', '')
    title = title.decode('utf-8', 'ignore')
    return title.strip()


kaggle_data['norm_movie_title'] = kaggle_data['movie_title'].map(preprocess_title)
genres_data['norm_movie'] = genres_data['movie'].map(preprocess_title)
ratings_data['norm_movie'] = ratings_data['movie'].map(preprocess_title)
