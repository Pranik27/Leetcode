# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:10:53 2020

@author: PRANIKP

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = [root]
        out_list = []
        
        
        while queue:
            
            tmp_var = queue[0]
            max_val = tmp_var.val
            tmp_arr = []
            for idx in range(len(queue)):
                
                tmp = queue.pop(0)
                max_val = max(max_val,tmp.val)
                
                if tmp.left:
                    tmp_arr.append(tmp.left)
                    
                if tmp.right:
                    tmp_arr.append(tmp.right)
                    
            out_list.append(max_val)
            queue = tmp_arr
            
        return out_list