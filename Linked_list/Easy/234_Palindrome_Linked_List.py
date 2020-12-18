# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:00:01 2020

@author: PRANIKP

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

Time Complexity: O(n)
Space Complexity:O(1) , if we don't consider the spcae the recusrion takes on the stack.
                 If we are considering the space taken by internal stack then we can perfrom 
                 linked list reversal by 3 pointer technique.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverse(self,node):
        
        if not node.next:
            return node
        
        rev_head = self.reverse(node.next)
        
        node.next.next = node
        node.next = None
        
        return rev_head
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        rev_head = self.reverse(slow)
        
        while rev_head:
            
            if rev_head.val != head.val:
                return False
            
            rev_head = rev_head.next
            head = head.next
            
        return True
