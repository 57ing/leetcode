#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 20. Valid Parentheses.py
@time: 2018/2/26 16:43
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Li = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                Li.append(i)
            elif len(Li) > 0:
                if i == ')' and Li[len(Li)-1] == '(':
                    Li.pop()
                elif i == ']' and Li[len(Li)-1] == '[':
                    Li.pop()
                elif i == '}' and Li[len(Li)-1] == '{':
                    Li.pop()
                else:
                    return False
            else:
                return False
        if len(Li) == 0:
            return True
        else:
            return False
s = '[(])'
so = Solution()
print(so.isValid(s))
