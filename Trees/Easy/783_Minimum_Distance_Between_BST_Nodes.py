# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:45:19 2020

@author: PRANIKP

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Time Complexity: O(n)
Space Complexity: O(n) , recursion depth
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    min_diff = 1
    
    def minDiffInBST(self, root):      
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def bst(root,lo,hi):
            
            if not root:
                return hi - lo
            
            left = bst(root.left,lo,root.val)
            right = bst(root.right,root.val,hi)
            return min(left,right)
        
        return bst(root,float('-inf'),float('inf'))
