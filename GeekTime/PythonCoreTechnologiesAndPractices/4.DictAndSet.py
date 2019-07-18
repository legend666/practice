#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 16:06
# @Author  : legend

"""
字典是一些列无序元素的组合，大小长度可变，一对键（key）和值（value）的配对，查找添加删除比list更优
字典和集合，无论是键和值，都可以是混合类型，s = {1,'hello',5.0}

什么是可散列的数据类型：流畅的Python，P55
https://docs.python.org/3/glossary.html#term-hashiable
"""
# 创建方式
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
# True
print(d1 == d2 == d3 == d4)
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)


# 取值
d1['name']  # 不存在，抛出异常
d1.get('name')  # 不存在返回null
