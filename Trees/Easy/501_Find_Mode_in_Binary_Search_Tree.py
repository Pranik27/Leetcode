# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:02:30 2020

@author: PRANIKP

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
     
        self.modes = []
        self.prev = root.val + 1
        self.prev_count = 0
        self.count = 0
        
        def dfs(root):
            
            if not root:
                return
            
            dfs(root.left)
            
            if root.val == self.prev:
                self.prev_count += 1
            else:
                self.prev_count = 1
                self.prev = root.val
                
            if self.count == self.prev_count:
                self.modes.append(root.val)
            elif self.prev_count > self.count:
                
                self.modes = [root.val]
                self.count = self.prev_count
                
            dfs(root.right)
        
        dfs(root)
        return self.modes