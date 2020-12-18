# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:59:18 2020

@author: PRANIKP

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

Time Complexity:O(n)
Space Complexity:O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        while head and head.val == val:
            head = head.next
            
        first = head
        
        while first and first.next:
            
            if first.next.val == val:
                first.next = first.next.next
            else:
                first = first.next
            
        return head

