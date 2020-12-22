# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:52:28 2020

@author: PRANIKP

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Time Complexity: O(n)
Space Complexity: O(n + 1) , where n is the no of nodes of the bigger list
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    res = None
    temp = None
    def makeList(self,node):
        
        if not self.res:
            self.res = node
            self.temp = self.res
        else:
            self.res.next = node
            self.res = self.res.next
        
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        
        while l1 and l2:
            
            if l1.val + l2.val + carry > 9:
                node_val = (l1.val+l2.val + carry) % 10
                carry = 1
            else:
                node_val = l1.val + l2.val + carry
                carry = 0
                
            self.makeList(ListNode(node_val))
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            while l1:
                if l1.val + carry > 9:
                    carry = 1
                    node_val = (l1.val + carry) % 10
                else:
                    node_val = l1.val  + carry
                    carry = 0
                
                self.makeList(ListNode(node_val))
                l1 = l1.next
                
        elif l2:
            while l2:
                if l2.val + carry > 9:
                    carry = 1
                    node_val = (l2.val + carry) % 10
                else:
                    node_val = l2.val +carry
                    carry = 0
                
                self.makeList(ListNode(node_val))
                l2 = l2.next
                
                
        if carry > 0:
            self.makeList(ListNode(carry))
            
        return self.temp

