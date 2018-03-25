#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 75. Sort Colors.py
@time: 2018/3/25 11:18
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        be = 0
        for i in range(2):
            be = self.run(nums,be,i)
        print(nums)

    def run(self,nums,be,target):
        be = be
        i = len(nums)-1
        while be < i:
            while be<len(nums) - 1 and nums[be] == target:
                be += 1
            if nums[i] == target:
                nums[be], nums[i] = nums[i], nums[be]
                be += 1
            while be<len(nums) - 1 and nums[be] == target:
                be += 1
            i -= 1
        return be
so = Solution()
so.sortColors([1,0,0])
