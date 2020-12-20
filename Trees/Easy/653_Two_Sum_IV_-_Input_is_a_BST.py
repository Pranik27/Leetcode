# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:32:43 2020

@author: PRANIKP

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.out_list = []
        
        def inorder(root):
            
            if root:
                inorder(root.left)
                self.out_list.append(root.val)
                inorder(root.right)
                
        inorder(root)
        
        first = 0
        last = len(self.out_list) - 1
        
        while first < last:
            if self.out_list[first] + self.out_list[last] == k:
                return True
            elif self.out_list[first] + self.out_list[last] > k:
                last -= 1
            elif self.out_list[first] + self.out_list[last] < k:
                first += 1
        
        return False