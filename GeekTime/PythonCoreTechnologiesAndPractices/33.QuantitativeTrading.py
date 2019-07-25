#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 10:46
# @Author  : legend

# 选择要获取的数据时间段
import pandas as pd
import matplotlib.pyplot as plt
import requests

periods = '3600'

# 通过http抓取btc历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                    params={'periods': periods})
data = resp.json()

df = pd.DataFrame(data['result'][periods],
                  columns=['CloseTime',
                           'OpenPrice',
                           'HighPrice',
                           'LowPrice',
                           'ClosePrice',
                           'Volume',
                           'NA'])

# print(df.head())
df['ClosePrice'].plot(figsize=(14, 7))