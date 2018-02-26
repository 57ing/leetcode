#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 17. Letter Combinations of a Phone Number.py
@time: 2018/2/26 15:36
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        pre = self.letterCombinations(digits[:-1])
        add = self.letterCombinations(digits[-1])
        return [s + c for s in pre for c in add]
digits = '233'
so = Solution()
print(so.letterCombinations(digits))
