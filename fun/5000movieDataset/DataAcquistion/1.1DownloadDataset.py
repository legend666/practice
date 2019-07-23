#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:06
# @Author  : legend
import os
import urllib

# Creating the data folder

if not os.path.exists('./data'):

    os.makedirs('./data')

# Obtaining the dataset using that hosts it
kaggle_url = 'https://github.com/sundeepblue/movie_rating_prediction/raw/master/movie_metadata.csv'
if not os.path.exists('./data/kaggle_dataset.csv'):
    response = urllib.urlretrieve(kaggle_url, './data/kaggle_dataset.csv')
