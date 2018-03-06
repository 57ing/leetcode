#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 122. Next Permutation.py
@time: 2018/3/2 11:26
'''
class Solution:
    def nextPermutation(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(num) == 0 or len(num) == 1:
            pass
        else:
            i = len(num)-1
            if num[i]>num[i-1]:
                num[i], num[i-1] = num[i-1], num[i]
            else:
                while i-1>=0 and (num[i] < num[i-1] or num[i] == num[i-1]):
                    i -= 1
                if i > 0:
                    for j in range(len(num)-1,i-1,-1):
                        if num[j] > num[i-1]:
                            num[j],num[i-1] = num[i-1],num[j]
                            break
                    b = num[i:]
                    b.reverse()
                    num[i:] = b
                else:
                    num.reverse()
so = Solution()
n = [5,1,1]
so.nextPermutation(n)
print(n)
