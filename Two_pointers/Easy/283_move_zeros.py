# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:32:26 2020

@author: PRANIKP

Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        first = 0
        second = 0
        
        while second < len(nums) and first < len(nums):
            
            if nums[first] != 0 and nums[second] != 0:
                first += 1
                second += 1
            elif nums[first] == 0 and nums[second] == 0:
                second += 1
            elif nums[first] != 0 and nums[second] == 0:
                first += 1
            else:
                nums[first],nums[second] = nums[second],nums[first]                
            

                
        return nums