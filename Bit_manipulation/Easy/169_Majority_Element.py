# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:38:10 2020

@author: PRANIKP

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

Time Complexity:O(n)
Space Complexity:O(n)
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt ={}
        
        for x in nums:
            
            if x in dt:
                dt[x] += 1
            else:
                dt[x] = 1
        
        for x in dt:
            
            if dt[x]> len(nums)//2:
                return x