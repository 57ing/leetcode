#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 10. Regular Expression Matching.py
@time: 2018/2/2 22:18
1.处理*通配符需要使用递归来进行
2.为了防止递归次数过多，需要对匹配的表达式进行优化
'''
class Solution:
    def __init__(self):
        self.flag = True
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if self.flag:
            temp = ''
            n = 0
            if len(p) > 2:
                i = 0
                while i < len(p):
                    while i < len(p)-3 and p[i+1] == p[i+3] == '*' and p[i] == p[i+2]:
                        i += 2
                    while len(p)-1 > i > 2 and p[i+1] == '*' and temp[n-2:n] == '.*':
                        i += 2
                    if i < len(p):
                        temp += p[i]
                        n += 1
                    i += 1
                p = temp
            self.flag = False
        s_i = 0
        p_i = 0
        if len(p) == 0:
            if len(s) > 0:
                return False
            if len(s) == 0:
                return True
        p += '='
        s += '='
        while s_i < len(s):
            if s[s_i] == '=':
                break
            if p[p_i] == '=':
                if s[s_i] == '=':
                    return True
                else:
                    return False
            if 'a' <= p[p_i] <= 'z':
                if p[p_i+1] == '*':
                    temp = p_i
                    if self.isMatch(s[s_i:len(s)-1], p[p_i+2:len(p)-1]):
                        return True
                    while s[s_i] == p[p_i]:
                        s_i += 1
                        if self.isMatch(s[s_i:len(s)-1], p[p_i+2:len(p)-1]):
                            return True
                    p_i += 2
                else:
                    if p[p_i] == s[s_i]:
                        p_i += 1
                        s_i += 1
                    else:
                        return False
            elif p[p_i] == '.':
                if p[p_i+1] == '*':
                    p_i += 2
                    if p[p_i] == '=':
                        return True
                    for k in range(len(s)-2, s_i-1, -1):
                        if self.isMatch(s[k:len(s)-1], p[p_i:len(p)-1]):
                            return True
                    return False
                else:
                    s_i += 1
                    p_i += 1
        while p_i < len(p)and p[p_i] != '=':
            if 'a' <= p[p_i] <= 'z' or p[p_i] == '.':
                if p[p_i+1] == '*':
                    p_i += 2
                else:
                    return False
        return True
