#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 46. Permutations.py
@time: 2018/3/10 16:12
题目要求找出一个不重复数列的所有排列和组合，我的思路是原来做过一题要求是找出一个数列的下一个顺序排列数，也就是leetcode的第122题。比如[1,2,3,4]的下一个是[1,2,4,3]，那么就可以在这一题的
基础上做，首先对给的数列排序，排序完成以后不断调用122题的算法就行
例如，数组[3,2,1,4]
我们先将其排序为[1,2,3,4]
然后调用122题的next permutatuion算法，得到[1,2,4,3]
不断调用,
[1,3,2,4]->[1,3,4,2]->[1,4,2,3]->[1,3,2,4]…………最后直到[4,3,2,1]
中间的这些不重复序列就是所有的排列组合
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        re = []
        re.append(nums[:])
        f = self.nextPermutation(nums)
        for i in f:
            re.append(i[:])
        return re

    def nextPermutation(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while True:
            if len(num) == 0 or len(num) == 1:
                return num
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
                        return num
            yield num
so = Solution()
print(so.permute([1,2,3,4,5]))
