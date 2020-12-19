# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:30:09 2020

@author: PRANIKP

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Time Complexity: O(k) , where is the no of bits 
Space Complexity: O(1)
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return bin(x^y)[2:].count('1')