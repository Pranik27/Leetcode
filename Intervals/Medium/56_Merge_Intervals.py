# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:00:17 2020

@author: PRANIKP

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        
        first = 0
        second = 0
        
        out_list = []
        
        while second < len(intervals):
            
            l_ref,r_ref = intervals[first]
            while second < len(intervals) and intervals[second][0] <= r_ref:
                
                r_ref = max(r_ref, intervals[second][1])
                second += 1
                
            out_list.append([l_ref,r_ref])
            first = second
            
        return out_list
