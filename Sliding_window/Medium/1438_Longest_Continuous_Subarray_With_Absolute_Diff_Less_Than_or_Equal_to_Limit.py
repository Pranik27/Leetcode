# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:06:33 2020

@author: PRANIKP

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9

Time Complexity:O(n)
Space Complexity:O(n)
"""
import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        minq = deque()
        maxq = deque()
        
        first = 0
        last = 0
        max_len = 0
        
        while last < len(nums):
            
            while len(minq) > 0 and nums[last] <= nums[minq[-1]]:
                minq.pop()
                
            while len(maxq) > 0 and nums[last] >= nums[maxq[-1]]:
                maxq.pop()
                
            
            minq.append(last)
            maxq.append(last)
            
            if abs(nums[maxq[0]] - nums[minq[0]]) > limit:
                
                if first >= minq[0]:
                    minq.popleft()
                    
                if first >= maxq[0]:
                    maxq.popleft()
                    
                first += 1
            else:
                
                max_len = max(max_len, last -first + 1)
                last += 1
                
        return max_len