# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:35:26 2020

@author: PRANIKP

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= nums.length <= 3 * 104
-1000 <= nums[i] <= 1000
nums is sorted in increasing order.
-1000 <= target <= 1000

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        last = len(numbers) - 1
        out_list = []
        
        while first < last:
            
            if numbers[first] + numbers[last] == target:
                out_list.append(first + 1)
                out_list.append(last + 1)
                return out_list
            elif numbers[first] + numbers[last] < target:
                first += 1
            else:
                last -= 1
