#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 20:48
# @Author  : legend

# (1)_xxx "单下划线"开始的成员边浪叫做保护变量，即只有类实例和子类实例
# 能访问这些到这些变量，需通过类提供的接口进行访问：不能用"from module import"
# (2)__xxx 类中有私有变量/方法名(Python的函数也是对象，所以成员方法称为成员变量也行得通)
#         "双下划綫"开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据
# (3)__xxx__系统定义的名字，前有均有一个"双下划线"代表Python里特殊方法专用的标识
#     如__int__()代表类的构造函数。


# -*- coding:utf-8 -*-

class A(object):

    def __init__(self):  # 系统定义方法
        self.string = 'A string'
        self._string = 'A _string'
        self.__string = 'A __string'  # 私有变量

    def fun(self):
        return self.string + ' fun-A'

    def _fun(self):
        return self._string + '  _fun-A'

    def __fun(self):  # 私有方法
        return self.__string + ' __fun-A'

    def for__fun(self):  # 内部调用私有方法
        return self.__fun()


class B(A):

    def __init__(self):  # 系统定义方法
        self.string = 'B string'


a = A()
print(a.string)
print(a._string)
# print a.__string 不可访问

print(a.fun())
print(a._fun())
# print (a.__fun()) 不可访问
print(a.for__fun())

b = B()
print(b.fun())
print(b.fun().__len__())  # 系统定义函数
