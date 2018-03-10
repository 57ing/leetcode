#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 42. Trapping Rain Water.py
@time: 2018/3/9 9:56
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = 0
        n = len(height)
        left = 0
        right = n-1
        top = 0
        le_height = 0
        ri_height = 0
        while left < right:
            if height[left] >= le_height:
                le_height = height[left]
            else:
                count += le_height - height[left]

            if height[right] >= ri_height:
                ri_height = height[right]
            else:
                count += ri_height - height[right]

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return count
so = Solution()
print(so.trap([5,4,1,5]))
