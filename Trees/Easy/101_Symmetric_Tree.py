# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:56:35 2020

@author: PRANIKP

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        queue = []
        
        queue.append(root)
        queue.append(root)
        
        while queue:
            
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            
            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
            
        return True
    
    

#Recursive


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        def isMirror(a,b):
            
            if not a and not b:
                return True
            
            if (a and not b) or (not a and b) or a.val != b.val:
                return False
            
            if not isMirror(a.left,b.right):
                return False
            
            if not isMirror(a.right,b.left):
                return False
            
            return True
            
            
            
        return isMirror(root.left,root.right)