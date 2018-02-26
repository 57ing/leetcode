#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 15.3Sum.py
@time: 2018/2/25 16:14
先排序，完成排序后遍历一遍数组，对于遍历过程中的每一个a，设定a+1位置为左（l），末尾位置为右（r），计算a，了l，r位置对应数值的和s，再根据和s的大小进行移动：
1.s<0,l右移
2.s>0,r左移
3.s=0，找到一组三元组，为避免输出重复三元组，如果l+1位置处的数值和l处相同，那么将l右移到不相同的地方，r同理
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    re = list([nums[i],nums[l],nums[r]])
                    L.append(re)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return L
nums = [-1, 0, 1, 2, -1, -4]
so = Solution()
print(so.threeSum(nums))
