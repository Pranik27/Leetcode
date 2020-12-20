# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:49:42 2020

@author: PRANIKP

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

Time Complexity: O(n)
Space Complexity: O(n) , call stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        
        def bfs(root,flag):
            
            if not root:
                return
            
            
            if not root.left and not root.right and flag == True:
                    self.sum += root.val
                
            bfs(root.left,True)
            bfs(root.right,False)
        
        bfs(root,False)
        return self.sum