#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:25
# @Author  : legend

"""
list是动态的，长短大小不固定,元素随意增删改 mutable
tuple是静态的，长度大小固定，无法增删改 immutable
        如果想改变tuple，就创建一个新的tuple，然后把之前的添加进去
"""
"""
list和tuple都支持负数索引，-1表示最后一个元素
还都支持切片操作
可以随意嵌套
l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表
tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一元组
"""
l = [1, 2, 3, 4]
tup = (1, 2, 3, 4)
new_tup = tup + (5,)
l.append(5)
# print(new_tup)
# print(type( (5) ))  # int
# print(type( (5,) ))  # tuple
# list和tuple相互转换
list((1, 2, 3, 4))
tuple([1, 2, 3, 4])
# 常用内置函数
li = [3, 2, 3, 7, 8, 1]
li.count(3)  # 统计item出现的次数
li.index(7)  # 返回item第一次出现的索引
li.reverse()  # 原地倒转列表（元组没有内置这个函数）
li.sort()  # 排序（元组没有内置这个函数）
tupl = (3, 2, 3, 7, 8, 1)
tupl.count(3)

# reversed() 和 sorted() 同样表示对列表/元组进行倒转和排序
# 但是返回一个倒转后或排好序的列表/元组

list(reversed(tupl))
sorted(tupl)

"""存储方式"""
l1 = [1, 2, 3, 4, 5]
print(l1.__sizeof__())
# 48 56 64 72 80
tup1 = (1, 2, 3, 4, 5)
print(tup1.__sizeof__())
# 32 40 48 56 64
# 差了16个字节，
