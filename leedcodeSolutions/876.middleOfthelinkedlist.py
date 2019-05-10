#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 10:10
# @Author  : legend
class Solution:
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


n1 = Node("n1", None)
n2 = Node("n2", n1)
n3 = Node("n3", n2)
n4 = Node("n4", n3)
n5 = Node("n5", n4)
n6 = Node("n5", n5)
n7 = Node("n5", n6)

head = n6  # 链表的头节点
p1 = p2 = head
while p2.next is not None and p2.next.next is not None:
    p2 = p2.next.next
    p1 = p1.next
print(p1.data)
