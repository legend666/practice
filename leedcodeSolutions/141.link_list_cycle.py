#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 9:56
# @Author  : legend
class Solution(object):
    def hasCycle(self, head):
        """:type head :ListNode
            :retype :bool
        """
        if not head:
            return False
        lookup = {}
        while head:
            if head in lookup:
                return True
            head = head.next
        return False


# 快指针和满指针，如果有环，快指针会和慢指针相遇（相等），所以有环
class Solution2(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            show = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
