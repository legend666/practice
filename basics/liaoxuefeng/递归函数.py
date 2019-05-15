#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 14:38
# @Author  : legend
"""
在函数内部，可以调用其他函数，如果一个函数在内部调用自身本身，这个函数就是递归函数
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


"""
在计算机中，函数调用时通过栈（stack）这种数据结构实现的，每当进入一个函数调用时，栈就会加一层栈帧
每当函数返回，栈就会建一层栈帧，栈的大小不是无限的，所以调用过多，会导致栈溢出
"""
print(fact(1000))  # RecursionError: maximum recursion depth exceeded in comparison