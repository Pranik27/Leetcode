# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:24:09 2020

@author: PRANIKP

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        first = 0
        end = len(A) - 1
        out_list = [0] * len(A)
        n = len(A) -1
        
        while first <= end:
            
            if abs(A[first]) > abs(A[end]):
                out_list[n] = A[first]**2
                first += 1
            else:
                out_list[n] = A[end]**2
                end -= 1
                
            n -= 1
                
        return out_list

