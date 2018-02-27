#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 22. Generate Parentheses.py
@time: 2018/2/27 11:18
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        re = []
        s = ''
        def backtrack(s, open, close):
            if len(s) == 2*n:
                re.append(s)
            else:
                if open < n:
                    backtrack(s + '(', open+1, close)
                if close < open:
                    backtrack(s + ')', open, close+1)
        backtrack(s,0,0)
        return re
so = Solution()
print(so.generateParenthesis(3))
