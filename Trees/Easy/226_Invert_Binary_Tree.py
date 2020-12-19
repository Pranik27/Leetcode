# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:22:51 2020

@author: PRANIKP

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

Time Complexity:O(n)
Space Complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        while root:
            
            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left:
                root.right = root.left
                root.left = None
            else:
                root.left = root.right
                root.right = None
        
        
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
            
        return None