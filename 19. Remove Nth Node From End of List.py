#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 19. Remove Nth Node From End of List.py
@time: 2018/2/26 16:07
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        front = ListNode(0)
        front.next = head
        tem = front
        count = -1
        while tem:
            count += 1
            tem = tem.next
        tem = head
        cur = front
        while tem:
            if count == n:
                cur.next = tem.next
                break
            else:
                cur = tem
                tem = tem.next
                count -= 1
        return front.next
head = ListNode(1)
head.next = ListNode(2)
n = 2
so = Solution()
print(so.removeNthFromEnd(head,n))
