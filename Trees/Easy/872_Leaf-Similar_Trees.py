# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:24:04 2020

@author: PRANIKP

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

Time Complexity:O(n+m) , wheren n and m are the no of nodes in both the trees respectively.
Space Complexity:O(n+m) , wheren n and m are the no of nodes in both the trees respectively.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        li1 = []
        out_list = []
        
        def leafSeq(root):
            
            if not root:
                return
            
            if root.left and root.right:
                leafSeq(root.left)
                leafSeq(root.right)
            elif not root.left and not root.right:
                out_list.append(root.val)
            elif root.left:
                leafSeq(root.left)
            elif root.right:
                leafSeq(root.right)
                
        leafSeq(root1)
        li1 = out_list
        out_list = []
        leafSeq(root2)

        if li1 == out_list:
            return True
        
        return False