#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 8:34
# @Author  : legend
import os

# 显示当前Python程序占用的内存大小
import psutil as psutil


# psutil 即 process and system utilities廖的教程中有

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {}MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    # global a 设置a为全局变量时后，函数返回后，列表的引用依然存在，所以并不会被回收
    a = [i for i in range(10000000)]
    show_memory_info('after a created')
    # return a
    # a = fuc()
    # 如果返回列表，在主程序中接收那么引用依然存在，垃圾回收就不会被触发


func()
show_memory_info('finished')

# initial memory used: 25.7265625MB
# after a created memory used: 413.00390625MB
# finished memory used: 25.890625MB
# 函数内部声明的列表a 是局部变量，函数返回后，局部变量的引用会注销掉，
# 此时列表a所知带的对象引用为0，Python便会执行垃圾回收
