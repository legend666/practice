#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 16:22
# @Author  : legend


from basics.point import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode.ListNode()
        dummy.next = head
        p = dummy
        q = dummy

        for i in range(n):
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next
        return dummy.next


#
# class ListNode_handle:
#     def __init__(self):
#         self.cur_node = None
#
#     def add(self, data):
#         # add a new node pointed to previous node
#         node = ListNode()
#         node.val = data
#         node.next = self.cur_node
#         self.cur_node = node
#         return node
#
#     def print_ListNode(self, node):
#         while node:
#             print
#             '\nnode: ', node, ' value: ', node.val, ' next: ', node.next
#             node = node.next
#
#     def _reverse(self, nodelist):
#         list = []
#         while nodelist:
#             list.append(nodelist.val)
#             nodelist = nodelist.next
#         result = ListNode()
#         result_handle = ListNode_handle()
#         for i in list:
#             result = result_handle.add(i)
#         return result

if __name__ == '__main__':
    solution = Solution()
    solution.removeNthFromEnd([1, 2, 43, 6, 78, 9, 3, 5, 8, 2, 8, 9], 3)
