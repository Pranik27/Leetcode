# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:52:30 2021

@author: PRANIKP

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 

Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        
        sum = 0
        res = 0
        dt = {}
        
        for idx,val in enumerate(hours):
            
            if val > 8:
                sum += 1
            else:
                sum -= 1
            
            if sum > 0:
                res = idx + 1
            
            if sum - 1 in dt:
                res = max(res,idx - dt[sum - 1])
                
            dt.setdefault(sum, idx)
        
        return res