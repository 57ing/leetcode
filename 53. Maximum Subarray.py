#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 53. Maximum Subarray.py
@time: 2018/3/14 14:16
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        maxm = nums[0]
        count = 0
        flag = False
        for i in nums:
            count += i
            if count > maxm:
                maxm = count
            if count < 0:
                count = 0
        return maxm
so = Solution()
print(so.maxSubArray([-10,-2]))
