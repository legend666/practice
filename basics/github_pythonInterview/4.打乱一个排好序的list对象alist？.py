#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 10:08
# @Author  : legend

import random

a_list = [1, 2, 3, 4, 5, 6]
random.shuffle(a_list)  # 讲序列a_list打乱
random.randint(1, 10)  # 1到10的一个整数型随机数
random.random()  # 0到1的一哥随机浮点数
random.uniform(1.2, 5.4)  # 区间内之间的随机浮点数，区间可以不是整数
random.choice('tomorrow')  # 从序列随机选取一个数
print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
