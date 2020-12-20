# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:03:39 2020

@author: PRANIKP

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

 

 

Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:


Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
 

Constraints:

The number of nodes in the tree is in the range [1, 25].
1 <= Node.val <= 231 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree.

Time Complexity: O(n)
Space Complexity: O(n) , call stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = -1
        self.min = root.val
        
        def helper(root):
            
            if not root:
                return
            
            if self.ans >= 0 and (root.val < self.ans and root.val > self.min):
                self.ans = root.val
            elif self.ans < 0 and root.val > self.min:
                self.ans = root.val
                
            helper(root.left)
            helper(root.right)
       
                
        helper(root)
        return self.ans