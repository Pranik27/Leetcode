# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:11:54 2020

@author: PRANIKP

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

Time Complexity: O(m+n)
Space Complexity: O(m + n)
"""

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []
        
        
        first = 0
        second = 0
        out_list = []
       
        while first < len(A) and second < len(B):
            
            if B[second][0] <= A[first][1] and B[second][1] >= A[first][0]:
                left = max(A[first][0],B[second][0])
                right = min(A[first][1],B[second][1])
                out_list.append([left,right])
                
                
            if A[first][1] <= B[second][1]:
                first += 1
            else:
                second += 1
                
        return out_list



