# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:33:44 2021

@author: PRANIKP

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort()
        
        for idx in range(1,len(intervals)):
            
            if intervals[idx][0] < intervals[idx -1][1]:
                return False
        
        return True