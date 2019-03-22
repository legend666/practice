#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 15:23
# @Author  : legend

# 用个递归
class Solution(object):
    def plusOne(self, digits):
        if digits == []:
            return [1]
        if digits[:-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            return self.plusOne(digits[:-1]) + [0]