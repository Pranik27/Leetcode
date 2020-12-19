# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:27:09 2020

@author: PRANIKP

Share
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

Time Complexity: O(n) , where n is the no of nodes
Space Complexity: O(h) , where h is the height of the tree or O(n) where n is the no of nodes in the tree . basically max of both. 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        out_list = []
        
        
        while queue:
            
            curr_sum = 0.0
            nodes = len(queue)
            
            for x in range(0,len(queue)):
                
                temp = queue.pop(0)
                curr_sum += temp.val

                
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
            
            out_list.append(curr_sum/nodes)
            
        return out_list