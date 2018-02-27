#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 21. Merge Two Sorted Lists.py
@time: 2018/2/26 17:06
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        front = ListNode(None)
        tem = front
        while l1 and l2:
            if l1.val >= l2.val:
                tem.next = l2
                l2 = l2.next
            else:
                tem.next = l1
                l1 = l1.next
            tem = tem.next
        tem.next = l1 or l2
        return front.next
