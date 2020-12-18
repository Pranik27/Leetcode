# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:54:31 2020

@author: PRANIKP

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Time Complexity:O(n)
Space Complexity:O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next:
            return head
        
        
        curr_head = self.deleteDuplicates(head.next)
        
        if curr_head.val == head.val:
            head.next = head.next.next
            
        return head