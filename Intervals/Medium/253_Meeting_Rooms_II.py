# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 01:05:17 2021

@author: PRANIKP

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        start_timings = []
        end_timings = []
        
        for x,y in intervals:
            start_timings.append(x)
            end_timings.append(y)
            
        start_timings.sort()
        end_timings.sort()
        
        used_rooms = 0
        
        s_ptr = 0
        e_ptr = 0
        
        while s_ptr < len(intervals):
            
            if start_timings[s_ptr] >= end_timings[e_ptr]:
                
                used_rooms -= 1
                e_ptr += 1
            
            used_rooms += 1
            s_ptr += 1
        
        return used_rooms
        
            
            
        