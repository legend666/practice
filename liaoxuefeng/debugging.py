#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 16:09
# @Author  : legend

# 第一种查看变量值等基本都是print
"""第二种，断言，assert"""
import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    print(10 / n)


"""启动Python解释器的时可以用‘-0’参数来关闭assert
    关闭后，就可以吧所有的assert当成pass了"""

"""第三种就是logging，logging不会抛出的错误"""

s = '4'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)  # 没成。。。不知道哪里出问题了，之后用到logging的时候在多看看吧

"""第四种Python的调试器pdb
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000#0
"""