# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:19:27 2020

@author: PRANIKP

Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 1
        n = len(nums)
        
        for i,x in enumerate(nums):
            
            if x <= 0 or x > n:
                nums[i] = 0
        
        for a,num in enumerate(nums):
            
            correct_no = abs(num)
            
            if correct_no > 0:
                
                if nums[correct_no - 1] > 0:
                    nums[correct_no - 1] *= -1
                elif nums[correct_no - 1] ==  0:
                    nums[correct_no - 1] *= float('-inf')
        
        
        for x,num in enumerate(nums):
            
            if num >= 0:
                return x + 1
        
        return n + 1