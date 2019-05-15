#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 11:28
# @Author  : legend


# 作者：hitsunbo
# 链接：https://www.jianshu.com/p/144db81341a3
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

# need_change 为需要找零的金额，
# currency_list 为该国货币的面值列表，
# num_list 为需要找零的最少货币数目, num_list的长度至少为(need_change+1)
# used_list 为需要找零的最少货币数目, 长度与num_list相同
# class Change(object):
    # def giveChange(self,need_change, currency_list, num_list, used_list):
        # for change in range(need_change + 1):
            # for currency in currency_list:
                # if (change - currency >= 0) and #（看看在敲吧）