#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 48. Rotate Image.py
@time: 2018/3/11 16:57
要求空间复杂度为O(1)，所以采用从外到里，从左到右的顺寻，每次改变四个数字的位置
'''
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n//2, 1):             #第一层循环，控制从外到里的层数，从最外层开始，一致到最里层
            for j in range(i, n-i-1, 1):        #第二层循环，遍历该层，每次交换四个数字的位置
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
        return matrix
so = Solution()
for i in so.rotate([[1,2,3],[4,5,6],[7,8,9]]):
    print(i)
