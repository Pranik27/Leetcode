# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:07:52 2020

@author: PRANIKP

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
Accepted

Time Complexity:O(n)
Space Complexity:O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    ans = troot = TreeNode()
    def inorder(self,Rroot):
        
        if Rroot:
            self.inorder(Rroot.left)
            Rroot.left = None
            self.troot.right = Rroot
            self.troot = Rroot
            self.inorder(Rroot.right)
        

        return Rroot
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """


        
        self.inorder(root)
        

        return self.ans.right