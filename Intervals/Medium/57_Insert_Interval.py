# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:56:23 2020

@author: PRANIKP

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

Time Complexity: O(logn)
Space Complexity:O(1)
"""

class Solution(object):
    
    def binary_search1(self,arr,key):
        
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            
            mid = (start + end)//2
            
            if key[0] <= arr[mid][1]:
                end = mid -1
            else:
                start = mid + 1
                
        return start
    
    def binary_search2(self,arr,key):
        
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start+end)//2
            if key[1] < arr[mid][0]:
                end = mid -1
            else:
                start = mid + 1
        return start - 1
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return [newInterval]
        
        
        ind1 = self.binary_search1(intervals,newInterval)
        ind2 = self.binary_search2(intervals,newInterval)
        
        if ind1 > ind2:
            return intervals[:ind1] + [newInterval] + intervals[ind2 + 1:]
        else:
            x = min(intervals[ind1][0] ,newInterval[0])
            y = max(intervals[ind2][1] ,newInterval[1])
            
            return intervals[:ind1] + [[x,y]] + intervals[ind2 + 1:]
