#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 15:40
# @Author  : legend


# isinstance(object, classinfo)
# object实例对象
# classinfo可以是直接或间接类名，基本类型或者他们组成的元组
a = 3
isinstance(a, str)


class A:
    pass


class B(A):
    pass


# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False
