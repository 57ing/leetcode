#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 49. Group Anagrams.py
@time: 2018/3/13 15:32
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for i in strs:
            s = tuple(sorted(i))
            if s not in ans:
                ans[s]=[i]
            else:
                ans[s].append(i)
        re = []
        for i in ans:
            re.append(ans[i])
        return re
so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
