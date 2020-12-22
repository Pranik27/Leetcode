# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 03:02:09 2020

@author: PRANIKP

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

Time Complexity: O(logn + k ) TC where logn is the time taken to convet from decimal to binary and 'k' is the time taken by count method for binary no of k bits
Space Complexity: Constant Space
"""

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        if n < 0:
            return False
        else:
            return s.count('1') == 1 and s.count('0')%2 == 0