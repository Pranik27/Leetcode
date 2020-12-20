# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:58:17 2020

@author: PRANIKP

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

Time Complexity: O(m * n)
Space Complexity: O(n) , call stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def sameTree(n1,n2):
            
            if not n1 and not n2:
                return True
            elif not n1 or not n2 or n1.val != n2.val:
                return False
            else:
                return sameTree(n1.left,n2.left) and sameTree(n1.right,n2.right)
            
        def dfs(root):
            
            if not root:
                return False
            
            if root.val == t.val and sameTree(root,t):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(s)