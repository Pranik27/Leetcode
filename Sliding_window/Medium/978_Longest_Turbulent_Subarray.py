# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:03:28 2020

@author: PRANIKP

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109

Time Complexity:O(n)
Space Complexity:O(1)
"""

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr_len = 0
        max_len = 0
        
        for k in range(0,len(A)):
            
            if k >= 2 and (A[k-2] < A[k-1] > A[k] or A[k -2] > A[k-1] < A[k]):
                curr_len += 1
            elif k >= 1 and A[k-1]!= A[k]:
                curr_len = 2
            else:
                curr_len = 1
                
            max_len = max(max_len,curr_len)
        

        return max_len