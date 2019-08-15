#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 10:36
# @Author  : legend
from fun.MoviesDataSetFrombiggorilla import extractingTheInformation
import pandas as pd

genres_data = extractingTheInformation.genres_data()
# print(type(genres_data)) <class 'pandas.core.frame.DataFrame'>
ratings_data = extractingTheInformation.ratings_data()
kaggle_data = pd.read_csv('./data/kaggle_dataset.csv')


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
genres_data
