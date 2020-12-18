# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:49:21 2020

@author: PRANIKP

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

Time Complexity:O(m+n)
Space Complexity:O(m+n)
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        
        p1 = l1
        p2 = l2
        res = ListNode()
        temp = res
        while p1 or p2:
            
            if not p1:
                res.next = p2
                break
                
            if not p2:
                res.next = p1
                break
                
            if p1.val <= p2.val:
                res.next = p1
                p1 = p1.next
            else:
                res.next = p2
                p2 = p2.next
                
            res = res.next
        
        return temp.next

