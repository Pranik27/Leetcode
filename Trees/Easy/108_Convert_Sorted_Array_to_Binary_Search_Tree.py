# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:29:42 2020

@author: PRANIKP

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def newBST(nums,left,right):
            
            if left > right:
                return None
            
            mid = (left + right)//2
            
            curr_node = TreeNode(nums[mid])
            curr_node.left = newBST(nums,left,mid -1 )
            curr_node.right = newBST(nums,mid + 1,right)
            
            return curr_node
       
        return newBST(nums,0,len(nums) -1 )
        