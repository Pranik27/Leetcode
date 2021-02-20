# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:20:45 2021

@author: PRANIKP

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

Time Complexity: O(sqrt(N))
Space Complexity:Constat Space
"""

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        count = 1
        n = 2
        
        target = math.sqrt(2*N)
        
        while n < target:
            
            if (N - n*(n-1)/2) % n == 0:
                count += 1
            
            n += 1
  
        return count