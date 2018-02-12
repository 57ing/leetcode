#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 5. Longest Palindromic Substring.py
@time: 2018/2/2 20:04
遍历一遍字符串，对每个字符进行判断，注意需要特别考虑s[i]=s[i+1]的情况
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        be = 0
        end =0
        j=0
        i = 0
        for i in range(0,len(s),1):
            b,e = self.find(i,i,s)
            if e-b+1 > max:
                max = e-b+1
                be = b
                end = e
            if i<len(s)-1 and s[i]==s[i+1]:
                j = i+1
                b,e = self.find(i,j,s)
                if e-b+1 > max:
                    max = e-b+1
                    be = b
                    end = e
        return s[be:end+1]
    def find(self,i,j,s):
        n=0
        while (i-n)>=0 and (j+n)<len(s):
            if s[i-n]==s[j+n]:
                n+=1
            else:
                break
        n=n-1
        return i-n,j+n
so = Solution()
print(so.longestPalindrome('aaaa'))
