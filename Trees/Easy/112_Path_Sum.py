# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:05:29 2020

@author: PRANIKP

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        self.isSum = False
        
        def dfs(root,sum,curr_sum):
            
            if not root.left and not root.right and (curr_sum + root.val) == sum:
                self.isSum = True
                
            curr_sum += root.val
            
            if root.left:
                dfs(root.left,sum,curr_sum)
                
            if root.right:
                dfs(root.right,sum,curr_sum)

        dfs(root,sum,0)
        
        return self.isSum