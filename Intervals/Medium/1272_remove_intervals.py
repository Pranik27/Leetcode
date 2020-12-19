# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:25:21 2020

@author: PRANIKP

Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] 
represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

Time Complexity: O(n)
Space Complexity: O(m+n)
"""


def remove_intervals(interval,toBeRemoved):
    
    out_list = []
    l_ref,r_ref = toBeRemoved
    
    for l,r in interval:
        
        if l < l_ref:
            out_list.append([l,min(r,l_ref)])
            
        if r > r_ref:
            out_list.append([max(l,r_ref),r])
            
    return out_list


interval = [[11,5], [11,7]]
interval.sort()
print(interval)
toBeRemoved = [2,3]
print(remove_intervals(interval,toBeRemoved))

