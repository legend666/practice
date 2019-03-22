#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 10:03
# @Author  : legend
class Solution(object):
    def isValid(self,s):
        leftp = '([{'
        rightp = ')]}'
        stack = []
        for char in s:
            if char in leftp:
                stack.append(char)
            if char in rightp:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('[]{}{'))
