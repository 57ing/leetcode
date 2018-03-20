#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 55. Jump Game.py
@time: 2018/3/15 13:24
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = nums[0]
        i = 0
        while i < len(nums) and i <= end:
            end = i + nums[i] if (i + nums[i]) > end else end
            if end >= (len(nums) - 1):
                return True
            i += 1
        return False
so = Solution()
print(so.canJump([1,0,1]))
