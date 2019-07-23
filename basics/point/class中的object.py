#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 10:06
# @Author  : legend
# https://blog.csdn.net/DeepOscar/article/details/80947155
class Person:
    name = "legend"

class Anmial(object):
    name = "chiken"

if __name__ == "__main__":
    x = Person()
    print("person",dir(x))


    y = Anmial()
    print("Animal",dir(y))
# Person ['__doc__', '__module__', 'name']
# Animal ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', 
# '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
# Person类很明显能够看出区别，不继承object对象，只拥有了__doc__ , __module__ 和 自己定义的name变量, 也就是说这个类的命名空间只有三个对象可以操作.
#
# Animal类继承了object对象，拥有了好多可操作对象，这些都是类中的高级特性。
# python 2.7.10版本，实际上在python 3 中已经默认就帮你加载了object了（即便你没有写上object）。