# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:11:23 2021

@author: PRANIKP

Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

Time Complexity: O(n)
Space Complexity:O(n)
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        count = 0
        dp = [True for i in range(0,n + 1)]
        
        for idx in range(2,n):
            
            if dp[idx]:
                for i in range(idx,n,idx):
                    dp[i] = False
                count +=1
        
        return count
