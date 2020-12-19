# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:52:53 2020

@author: PRANIKP

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

Example 1:

Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
Example 3:

Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 

Constraints:

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
The start point of each interval is unique.

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

class Solution(object):
    
    def binary_search(self,arr,key):
        if arr[len(arr) - 1][0][0] < key:
            return -1
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            if key <= arr[mid][0][0]:
                right = mid -1
            else:
                left = mid + 1
                
        return arr[left][1]
    
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        
        [[3,4],[2,3],[1,2]]
        
        [[[1,2],2],[[2,3],1],[[3,4],0]]
        """
        sorted_list =[]
        out_list = []
        
        for i,x in enumerate(intervals):
            sorted_list.append([x,i])
            
        sorted_list.sort()
        
        for idx in range(len(intervals)):
            
            out_list.append(self.binary_search(sorted_list,intervals[idx][1]))
            
        return out_list
