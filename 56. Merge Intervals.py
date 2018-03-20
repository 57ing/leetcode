#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 56. Merge Intervals.py
@time: 2018/3/19 10:42
'''
class Interval:
    def __init__(self, s=0, e=0, data = 0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key =lambda x:x.start)
        i = 1
        while i < len(intervals):
            if intervals[i-1].end >= intervals[i].start:
                intervals[i-1].end = max(intervals[i-1].end,intervals[i].end)
                del intervals[i]
            else:
                i += 1
        return intervals

so = Solution()
s = [Interval(1,4),Interval(0,2),Interval(3,5),Interval(15,18)]
print([[i.start,i.end] for i in so.merge(s)])

