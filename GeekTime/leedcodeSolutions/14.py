#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 9:33
# @Author  : legend

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        print(type(strs))
        if not strs:
            return ''
        dp = [strs[0]]*len(strs)
        for i in range(1,len(strs)):
            while not strs[i].startswith(dp[i-1]):
                dp[i-1] = dp[i-1][:-1]
            dp[i] = dp[i-1]
        return dp[-1]
if __name__ == "__main__":
    lcp = Solution()
    print(lcp.longestCommonPrefix(["flower","flow","flight"]))