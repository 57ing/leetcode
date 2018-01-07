#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 3. Longest Substring Without Repeating Characters.py
@time: 2018/1/7 23:21


Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

本题要求找出一个字符串中字母不重复的最长子串，大概思路就是遍历一遍字符串，用be来记录开始位置，并使用一个集合来存储遍历过程中出现的字母，如果出现重复，那么我们就把be指向到从重复字符后一位，每次遍历都计算一次长度len，长度等于目前位置减去be，如果len大于max_len(初始为零)，那么max_len=len
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        be = 0
        max_be = 0
        max_end = 0
        dic = dict()
        max_lens = 0
        if len(s)== 0:
            return 0
        while i <len(s):
            if s[i] not in dic:
                dic[s[i]]=i
                if (i - be +1 ) > max_lens:
                    max_be = be
                    max_end = i
                    max_lens = i - be + 1
            else:
                temp = dic[s[i]]+1
                for k in s[be:temp]:
                    if k in dic:
                        del dic[k]
                be = temp
                dic[s[i]] = i
            i += 1
        return max_end-max_be+1
