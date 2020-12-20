# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:39:11 2020

@author: PRANIKP

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        out_list = []
        
        def bfs(root,level):
            
            if not root:
                return
            
            if len(out_list) < level + 1:
                out_list.append([])
                
            bfs(root.left,level+1)
            bfs(root.right,level+1)
            out_list[level].append(root.val)
            
        
        bfs(root,0)
        
        return out_list[::-1]