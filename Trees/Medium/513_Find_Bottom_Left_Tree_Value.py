# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:09:46 2020

@author: PRANIKP

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = [root]
        left_val = root.val
        
        while queue:
            
            for idx in range(len(queue)):
                
                temp = queue.pop(0)
                
                if temp.left:
                    queue.append(temp.left)
                    
                if temp.right:
                    queue.append(temp.right)
                    
            if queue:
                node = queue[0]
                left_val = node.val
                
        return left_val
            