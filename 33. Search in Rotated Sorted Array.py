#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 33. Search in Rotated Sorted Array.py
@time: 2018/3/4 14:26
'''
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1
