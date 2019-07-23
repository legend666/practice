#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 16:21
# @Author  : legend
"""
https://www.cnblogs.com/tootooman/p/8990633.html
1、作用域
全局名称空间：常见的存储“变量名与值的关系”的空间
局部名称空间：在函数运行中开辟的临时空间
内置名称空间：内置名称空间中存放了Python解释器为我们提供的名字：input，print，str，list，tuple等
拿过来就可以直接用的
2、Python中的作用域分为四种
L：local，局部作用域，即函数中定义的变量
E:enclosing，嵌套的父级函数的局部作用域，即包含次函数的上级函数的局部作用域，但是不是全局的（闭包中常见）
G：global，全局变量，就是模块级别定义的变量
B:built—in，系统固定模块里面的变量，比如int，bytearray
加载变量的优先级顺序依次是：py 内置作用域>当前模块中的全局（文件从上而下读取）>外层作用域>局部作用域
搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。
当然，local 和 enclosing 是相对的，enclosing 变量相对上层来说也是 local 。
"""
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
# list1 = [10, 'a']
# list2 = [123]
# list3 = [10, 'a']