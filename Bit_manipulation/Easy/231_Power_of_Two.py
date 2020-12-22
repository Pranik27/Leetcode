# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 02:37:17 2020

@author: PRANIKP

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
 

Constraints:

-231 <= n <= 231 - 1

Time Complexity: O(logn + k ) TC where logn is the time taken to convet from decimal to binary and 'k' is the time taken by count method for binary no of k bits
Space Complexity: Constant space
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            return bin(n)[2:].count('1') == 1
        else:
            return False