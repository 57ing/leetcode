#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 39. Combination Sum.py
@time: 2018/3/7 10:15
'''
class Solution:
    def __init__(self):
        self.res = []
        self.re = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.run(candidates,target,len(candidates)-1)
        return (self.res)


    def run(self,candidates,target,i):
        n = 0
        while target > 0:
            if i>=1:
                self.run(candidates,target,i-1)
            target -= candidates[i]
            self.re.append(candidates[i])
            n += 1
        if target == 0:
            self.res.append(self.re[:])
        for i in range(n):
            self.re.pop()
so = Solution()
so.combinationSum([1,2,3,6,7],7)
print(so.res)
