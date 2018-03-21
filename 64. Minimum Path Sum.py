#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 64. Minimum Path Sum.py
@time: 2018/3/21 10:52
这一题在62题的基础上加上了每个点的权值，要求其最短路径大小，同样使用dp
首先我们计算最后一行和最后一列的每个点到终点的最短距离
假设最后一行为[3,2,1]，由于最后一行的每一个点向终点移动的方向只有向右移动，所以只要向左累加就可以计算出最后一行个个点到终点的最短距离
在此处计算后距离为[6,3,1]
同理以及计算最后一列个点距离终点的最短距离
计算完毕后，我们可以根据已知的最后一行和最后一列的最短距离，计算出剩余点的最短距离。
'''
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2,-1,-1):
            grid[i][n-1] += grid[i+1][n-1]                      #计算最后一行的各个点的最短距离
        for i in range(n-2,-1,-1):
            grid[m-1][i] += grid[m-1][i+1]                      #计算最后一列的各个点的最短距离
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] += min(grid[i+1][j],grid[i][j+1])    #计算其余点的最短距离
        return grid[0][0]                                       #返回起点到终点的最短距离
so = Solution()
print(so.minPathSum([[1,3],
 [1,5],
 [4,2]]))
