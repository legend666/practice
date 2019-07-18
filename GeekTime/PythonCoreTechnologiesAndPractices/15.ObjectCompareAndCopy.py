#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 16:17
# @Author  : legend

"""is 和  ==  的比较"""
a = 1257
b = 1257
print(id(a))
print(id(b))
print(a is b)
# python开辟一块内存，然后变量同时只想这块内存区域，所以 a == b ,a is b 都是true
# ？教程中说  a = b 只符合-5到256的数字，试了并没有，Python估计该进了吧

"""is 和 == 的效率问题
is操作不能被重载，所以Python就不需要去寻找程序中其他地方重载了比较操作符，并去调用。
执行is操作知识比较两个变量的id而已
但是，== 是执行 a.__eq__(b),Python中大部分的数据类型都会去重载__eq__这个函数，这个函数会去遍历列表中的元素，
比较顺序和值是否相等
"""
# 对于不变的元素，也需要比较，比如tuple虽然是不可变得，但是tuple中嵌套一个list，就是可变的了
# 所以在必要的地方不能省略条件检查

# Shallow copy and deep copy

l1 = [1, 2, 3, 4]
l2 = list(l1)
l1 == l2  # true
l1 is l2  # false

#  还可以通过切片操作 ‘：’完成浅拷贝 ，Python中相应的函数是copy.copy()
import copy

l3 = copy.copy(l1)
print(l3)
t1 = (1, 2, 3, 4)
t2 = tuple(t1)
print(type(t1), type(t2))
