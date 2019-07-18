#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:25
# @Author  : legend

"""
列表和元组，都是一个可以放置任意数据类型的有序集合

list是动态的，长短大小不固定,元素随意增删改 mutable
tuple是静态的，长度大小固定，无法增删改 immutable
        如果想改变tuple，就创建一个新的tuple，然后把之前的添加进去
"""
"""
list和tuple都支持负数索引，-1表示最后一个元素
还都支持切片操作
可以随意嵌套
l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表
tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一元组
"""
l = [1, 2, 3, 4]
tup = (1, 2, 3, 4)
new_tup = tup + (5,)
l.append(5)
# print(new_tup)
# print(type( (5) ))  # int
# print(type( (5,) ))  # tuple
# list和tuple相互转换
list((1, 2, 3, 4))
tuple([1, 2, 3, 4])
# 常用内置函数
li = [3, 2, 3, 7, 8, 1]
li.count(3)  # 统计item出现的次数
li.index(7)  # 返回item第一次出现的索引
li.reverse()  # 原地倒转列表（元组没有内置这个函数）
li.sort()  # 排序（元组没有内置这个函数）
tupl = (3, 2, 3, 7, 8, 1)
tupl.count(3)

# reversed() 和 sorted() 同样表示对列表/元组进行倒转和排序
# 但是返回一个倒转后或排好序的列表/元组

list(reversed(tupl))
sorted(tupl)

"""存储方式"""
l1 = [1, 2, 3, 4, 5]
print(l1.__sizeof__())
# 48 56 64 72 80
tup1 = (1, 2, 3, 4, 5)
print(tup1.__sizeof__())
# 32 40 48 56 64
# 差了16个字节，
"""事实上，由于列表是动态的，所以它需要存储指针，来指向对应的元素（上述例子中，对于 int 型，8 字节）。
另外，由于列表可变，所以需要额外存储已经分配的长度大小（8 字节），这样才可以实时追踪列表空间的使用情况，
当空间不足时，及时分配额外空间。"""  # 还是没理解为啥是8。。。


l = []
l.__sizeof__()  # 空列表的存储空间为 40 字节
40
l.append(1)
l.__sizeof__()
# 72 // 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l.append(2)
l.__sizeof__()
# 72 // 由于之前分配了空间，所以加入元素 2，列表空间不变
l.append(3)
l.__sizeof__()
# 72 // 同上
l.append(4)
l.__sizeof__()
# 72 // 同上
l.append(5)
l.__sizeof__()
# 104 // 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间
"""上面的例子，大概描述了列表空间分配的过程。
我们可以看到，为了减小每次增加 / 删减操作时空间分配的开销，
Python 每次分配空间时都会额外多分配一些，这样的机制（over-allocating）保证了其操作的高效性：
增加 / 删除的时间复杂度均为 O(1)。"""


"""
初始化时间对比
python3 -m timeit 'x=(1,2,3,4,5,6)'
20000000 loops, best of 5: 9.97 nsec per loop
python3 -m timeit 'x=[1,2,3,4,5,6]'
5000000 loops, best of 5: 50.1 nsec per loop


索引操作对比
python3 -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
10000000 loops, best of 5: 22.2 nsec per loop
python3 -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'
10000000 loops, best of 5: 21.9 nsec per loop
"""


"""
使用场景：
1、存储的数据和数量不变，比如经纬度
2、
viewer_owner_id_list = [] # 里面的每个元素记录了这个 viewer 一周内看过的所有 owner 的 id
records = queryDB(viewer_id) # 索引数据库，拿到某个 viewer 一周内的日志
for record in records:
    viewer_owner_id_list.append(record.id)

"""


"""
思考题
python -m timeit 'empty_list = list()'
10000000 loops, best of 3: 0.0829 usec per loop

python -m timeit 'empty_list = []'
10000000 loops, best of 3: 0.0218 usec per loop

python -m timeit 'empty_list = ()'
100000000 loops, best of 3: 0.0126 usec per loop
测试结果，虽然直接创建元组初始化速度最快，但是由于要用list函数转一道反而不如直接创建列表的速度快。
"""