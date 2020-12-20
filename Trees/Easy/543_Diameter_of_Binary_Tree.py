# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:54:24 2020

@author: PRANIKP

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

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
    
    def height(self,root):
        
        if root == None:
            return 0
        
        if root:
            left = self.height(root.left)
            right = self.height(root.right)
            
            return (1 + max(left,right))
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)
        
        return max(left_height + right_height , max(left_dia,right_dia))