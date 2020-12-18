# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:41:04 2020

@author: PRANIKP

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

#Iterative

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            cur, prev = temp, cur
        return prev
    

#Recursive

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if not head.next:
            return head
        
        rev_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return rev_head
        