#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 23. Merge k Sorted Lists.py
@time: 2018/2/28 10:18
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            for i in range(1,len(lists),1):
                lists[0] = self.mergeTwoLists(lists[0],lists[i])
        return lists[0]

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

from queue import PriorityQueue

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
