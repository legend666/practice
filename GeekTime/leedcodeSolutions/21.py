#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 10:55
# @Author  : legend

class ListNode(object):
    def __int__(self,data):
        self.val = data
        self.next = None
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next
# if __name__ == '__main__':
#     mergeLists = Solution()
#     result = mergeLists.mergeTwoLists([1,2,2,3,5],[1,3,6,9,10,34])