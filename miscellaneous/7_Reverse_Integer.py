# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:02:58 2020

@author: PRANIKP

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1


Time Complexity: O(logx) , as there are roughly log(x) digits in the number x.
Space Complexity:O(1)
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        d = abs(x)
        new_num = 0
        
        while d:
            
            d,m = divmod(d,10)
            new_num = (new_num * 10) + m
            
        if new_num > 2**31 -1:
            return 0
        
        if x >= 0:
            return new_num
        else:
            return new_num * -1