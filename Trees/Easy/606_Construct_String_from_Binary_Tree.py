# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:36:56 2020

@author: PRANIKP

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Time Complexity: O(n)
Space Complexity: O(n) , considering the functinal stack call 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        
        if not t:
            return ""
        
        res = str(t.val)
        
        if t.left and t.right:
            res += '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'
        elif t.right and not t.left:
            res += '()' +  '(' + self.tree2str(t.right) + ')'
        elif t.left and not t.right:
            res += '(' + self.tree2str(t.left) + ')'
        
        return res