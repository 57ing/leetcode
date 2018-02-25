#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 11. Container With Most Water.py
@time: 2018/2/25 14:17
采用贪心策略，初始两条线选择位置0和len（height）-1，然后每次移动都尽量保证选择的线为最长的线，至于这个问题为什么可以采用贪心策略的证明，我还没有想清楚。
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        be = 0
        ed = len(height)-1
        maxm = ed*min(height[be],height[ed])
        while be < ed:
            if height[be] < height[ed]:
                be += 1
            elif height[be] > height[ed]:
                ed -= 1
            else:
                if height[be+1] >= height[ed-1]:
                    be += 1
                else:
                    ed -= 1
            s = (ed-be)*min(height[be],height[ed])
            maxm = s if s > maxm else maxm
        return maxm
so = Solution()
height = [1,1]
print(so.maxArea(height))

