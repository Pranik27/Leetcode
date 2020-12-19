# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:55:38 2020

@author: PRANIKP

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

Time Complexity: O(logn) where n is the no of nodes in the BST
Space Complexity: Constant space , if we ignore the functional stack else O(logn)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    max_sum = 0
    
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        if not root:
            return 0
        
        if root.val >= L and root.val <= R:
            self.max_sum += root.val
            
        if root.val > L:
            self.rangeSumBST(root.left,L,R)
            
        if root.val < R:
            self.rangeSumBST(root.right,L,R)
            
        return self.max_sum