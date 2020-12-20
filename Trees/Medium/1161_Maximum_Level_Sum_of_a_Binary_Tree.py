# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:08:38 2020

@author: PRANIKP

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

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
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        curr_lvl = 0
        max_val = root.val
        max_lvl = 1
        
        while queue:
            
            curr_val = 0
            curr_lvl += 1
            
            for x in range(len(queue)):
                
                temp = queue.pop(0)
                curr_val += temp.val
                
                if temp.left:
                    queue.append(temp.left)
                    
                if temp.right:
                    queue.append(temp.right)
            
            if curr_val > max_val:
                max_val = curr_val
                max_lvl = curr_lvl

                
        return max_lvl