#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 14:41
# @Author  : legend
# import pandas as pd
#
# kaggle_data = pd.read_csv('./data/kaggle_dataset.csv')
# genres_data = pd.read_csv('./data/genres_data')
# kaggle_data = pd.read_csv('./data/kaggle_dataset.csv')
# print ('Number of movies in kaggle_data: {}'.format(kaggle_data.shape[0]))
# print ('Number of movies in genres_data: {}'.format(genres_data.shape[0]))
# print ('Number of movies in ratings_data: {}'.format(ratings_data.shape[0]))


with open("./data/ratings.list", errors='ignore') as myfile:
    head = [next(myfile) for x in range(38)]
print(''.join(head[28:38]))
# skipping the first 28 lines as they are descriptive headers
