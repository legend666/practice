#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 14:55
# @Author  : legend
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s) - 1:
            if lookup[s[i]] >= lookup[s[i + 1]]:
                result += lookup[s[i]]
                i += 1
            else:
                result += lookup[s[i + 1]] - lookup[s[i]]
                i += 2
        print(s[len(s) - 2])
        print(s[len(s) - 1])
        if lookup[s[len(s) - 2]] >= lookup[s[len(s) - 1]]:
            result += lookup[s[len(s) - 1]]
        return result


if __name__ == "__main__":
    solution = Solution()
    res = solution.romanToInt('CCCI')
    print(res)
