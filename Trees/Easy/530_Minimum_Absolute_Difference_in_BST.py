# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:42:03 2020

@author: PRANIKP

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Time Complexity: O(n)
Space Complexity: O(n) , considering the depth of recursion.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root,low,hi):
            
            if not root:
                return hi - low
            
            left = dfs(root.left,low,root.val)
            right = dfs(root.right,root.val,hi)
            return min(left,right)
        
        return dfs(root,float('-inf'),float('inf'))
