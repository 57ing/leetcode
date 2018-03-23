#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 70. Climbing Stairs.py
@time: 2018/3/22 12:53
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        countList = [0] * n
        if n > 0:
            countList[0] = 1
        if n > 1:
            countList[1] = 2
        for i in range(2,n,1):
            countList[i] = countList[i-1] + countList[i-2]
        return countList[-1]
