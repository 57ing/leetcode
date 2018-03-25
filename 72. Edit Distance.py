#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 72. Edit Distance.py
@time: 2018/3/23 11:44
编辑距离问题
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m  < 1 or n < 1:
            return max(m,n)                                     #处理边界条件
        edit = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            edit[i][0] = i
        for i in range(n+1):
            edit[0][i] = i
        for i in range(1, m+1, 1):
            for j in range(1, n+1, 1):
                if word1[i-1] == word2[j-1]:
                    edit[i][j] = edit[i-1][j-1]
                else:
                    edit[i][j] = 1 + min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1])
        return edit[m][n]
# so = Solution()
# print(so.minDistance('ab','a'))

# # read = int(input())
# read = 12
# count = 0
# while True:
#     while read % 2 == 0:
#         read = read // 2
#         count += 1
#     while read % 3 == 0:
#         read = read // 3
#         count += 2
#     if read % 2 == 0 or read % 3 == 0:
#         continue
#     elif read == 1:
#         print(count)
#         break
#     else:
#         print(count + read -1)
#         break




# def magic(s1,s2,up,down):
#     flag = False
#     minm = up
#     po = 0
#     for i in range(len(s1)):
#         if down < s1[i] < up:
#             flag = True
#             if s1[i] < minm:
#                 minm = s1[i]
#                 po = i
#     s2.append(minm)
#     del s1[po]
#     return flag
#
#
# # read = input().split(' ')
# # a = int(read[0])
# # b = int(read[1])
# # list_a = list(map(int,input().split(' ')))
# # list_b = list(map(int,input().split(' ')))
# #
# list_a = [1,3,4,4,4,4,6]
# list_b = [2,3,4,5]
#
# average_a = float(sum(list_a)/len(list_a))
# average_b = float(sum(list_b)/len(list_b))
# flag = True
# count = 0
# while flag:
#     if average_a > average_b:
#         flag = magic(list_a,list_b,average_a,average_b)
#     elif average_a < average_b:
#         flag = magic(list_b,list_a,average_b,average_a)
#     else:
#         flag = False
#     if flag:
#         count += 1
#     average_a = float(sum(list_a)/len(list_a))
#     average_b = float(sum(list_b)/len(list_b))
# print(count)


read = list(map(int,input().split(' ')))
N, K, H =read[0], read[1], read[2]
# N, K, H = 3, 3, 3
jump = []
# jump = [1,3,6,8]
for i in range(N):
    jump.append(int(input()))
jump.sort()
height = 0
now = 0
i = 0
while K>0:
    while i<(len(jump)) and (now + H) >= jump[i]:
        i += 1
    i -= 1
    now += 2 * (0 if jump[i] - now < 0 else jump[i] - now)
    K -= 1
print(now)
