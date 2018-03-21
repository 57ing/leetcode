#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 62. Unique Paths.py
@time: 2018/3/20 11:17
使用动态规划算法，由最后的终点反着倒推前面每一个点到终点有多少路线
这一题的模型实质上来说可以抽象成求解杨辉三角形上指定位置的数的大小的问题，可以直接套用杨辉三角的求解公式进行计算
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        table = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            table[i][n-1] = 1
        for i in  range(n):
            table[m-1][i] = 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                table[i][j] = table[i+1][j] + table[i][j+1]
        return table[0][0]
so = Solution()
print(so.uniquePaths(3,7))

