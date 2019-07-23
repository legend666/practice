#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 15:02
# @Author  : legend
from basics.point.ListNode import ListNode


class Solution(object):
    def removeNthfromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy
        for i in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next
