#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 10. Longest Valid Parentheses.py
@time: 2018/3/3 11:15
'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxm = 0
        stack = []
        c = [1] *len(s)
        count = 0
        flag = False
        pro = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append([s[i],i])
            elif s[i] == ')':
                if len(stack) > 0 and stack[-1][0]  == '(':
                    one, po = stack.pop()
                    c[i] = c[po] = 0
        i = 0
        count = 0
        for i in range(len(c)):
            if c[i] == 0:
                count += 1
                maxm = count if count >maxm else maxm
            else:
                count =0

        return maxm
so = Solution()
print(so.longestValidParentheses(')))()(())'))
