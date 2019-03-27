# @Time : 2019/3/23 23:28
# @Author : legend
import copy

spam = ['a', 'b', 'c', 'd']
cheese = copy.copy(spam)
copy_spam = copy.deepcopy(spam)
print(spam)
type
cheese[1] = 42
print(spam)  # ['a', 'b', 'c', 'd']
print(cheese)  # ['a', 42, 'c', 'd']
# spam和cheese变量指向独立的列表，所以改变cheese中的列表时，只有cheese被改变
# 他们的id指向了独立的列表
print(id(spam))
print(id(cheese))
# 如果要复制的列表中包含了列表，就使用copy.deepcopy函数来代替
# deepcopy函数将同时复制他们内部的列表
var = copy.deepcopy(cheese)